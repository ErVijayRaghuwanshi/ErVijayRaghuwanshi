from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
import gradio as gr
from pydantic_ai.agent import Agent
from pydantic_ai import RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from utils import get_logger, zerodha_examples, text_generation

llm_model = "llama3.2"
# llm_model = "llama3.2:3b-instruct-fp16"

# Get logger opbject
logger = get_logger(name = __name__, log_file='Log/Zerodha_RAG.log')

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="BAAI/bge-large-en-v1.5", model_kwargs = {'device': 'cpu'})
logger.debug("Embeddings loaded")

# load from disk
db_zerodha = Chroma(persist_directory="./zerodha_db", embedding_function=embedding_function)
system_prompt = "You are a support chatbot for Zerodha, a leading stock brokerage firm. Your goal is to assist users with their queries by providing accurate and detailed information based on the retrieved documents provided. Always cite reference sources when required. If the user's query is not found or is outside the context of Zerodha, respond politely, asking them to rephrase their question within the Zerodha support context.\n\n If the user greeting message (such as 'hi', 'hello', 'hey') starts the conversation, respond with a friendly greeting and ask how you can assist with Zerodha-related queries, without providing detailed information or referencing retrieved documents.\n\n"
system_prompt = """
You are a support chatbot for Zerodha, a leading stock brokerage firm. Your primary goal is to assist users with their queries by providing accurate, concise, and contextually relevant information. 

Key Guidelines:
1. **Use Retrieved Documents:** 
   - If a user's query is complex, specific, or likely to require detailed reference material, use the provided `retrieve_docs` tool to fetch relevant documentation from the vector store.
   - When responding based on retrieved documents, clearly cite the source of the information.

2. **Avoid Retrieval When Not Needed:** 
   - For simple, general, or conversational queries that don't require document references (e.g., greetings or common knowledge questions), respond directly without invoking the document retrieval tool.

3. **Handling Unanswerable or Out-of-Scope Queries:** 
   - If the user's query is unrelated to Zerodha or the required information is unavailable in the retrieved documents, politely explain this and encourage the user to rephrase their question within the Zerodha support context.

4. **Friendly Greeting Protocol:**
   - If the conversation begins with a greeting (e.g., 'hi', 'hello', 'hey'), respond warmly and inquire how you can assist with Zerodha-related queries. Do not reference retrieved documents in this case.

Your tone should always be professional yet approachable, and your responses should prioritize clarity and usefulness.
"""



retriever = db_zerodha.as_retriever(search_kwargs={'k': 2})
logger.debug("Zerodha retriever loaded.")


# Create a RAG agent (here we use OpenAI's GPT-4 model as an example)
ollama_llm = OpenAIModel(model_name=llm_model, provider=OpenAIProvider(base_url='http://localhost:11434/v1'))
# groq_llm = 'groq:llama-3.3-70b-versatile'


from pydantic_ai.models.groq import GroqModel

groq_llm = GroqModel('llama-3.3-70b-versatile')
agent = Agent(groq_llm, system_prompt=system_prompt)

# Define a tool for document retrieval using your Chroma vector retriever
@agent.tool
def retrieve_docs(context: RunContext, query: str) -> str:
    """
    Retrieve documentation sections based on a search query.
    
    When to Use:
    - Use this tool for specific or detailed queries requiring precise information from Zerodha's knowledge base or documentation.
    - Examples include questions about Zerodha's brokerage plans, trading platforms, account opening processes, or advanced troubleshooting.

    Functionality:
    - The tool uses a Chroma vector retriever to search the document database for the most relevant sections based on the provided query.
    - It combines the retrieved documents into a single string for easy processing, including source metadata where available.

    Arguments:
    - `context`: The RunContext instance providing the execution context.
    - `query`: A string representing the user's query to search for in the vector store.

    Returns:
    - A string containing the combined content of the retrieved documents, including source information. 
    - If no documents are found, it returns an empty string.

    Example Output:
    - "Source: Help Center - Account Opening\nContent: To open an account with Zerodha, follow these steps..."
    """
    docs = retriever.invoke(query)
    # gr.Info(f"retriever docs: {len(docs)} for query: {query}")
    logger.info(f"retriever docs: {len(docs)} for query: {query}")
    # Combine the retrieved documents into a single string, including source information if available
    result = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'unknown')}\nContent: {doc.page_content}"
        for doc in docs
    )
    return result

resp = None

def rag_agent(query, history):
    global resp
    logger.info(f"User-input: {query}")
    if resp:
        resp = agent.run_sync(query, message_history=resp.new_messages(), deps=retriever)
    else:
        resp = agent.run_sync(query, deps=retriever)

    logger.info(f"Bot-response: {resp.data}")
    return resp.data

def construct_prompt(query, retrieved_docs):
    prompt = "query" + query
    
    # Append the retrieved documents to the prompt
    prompt += "\n\n[Retrieved Documents for query]\n\n"
    for i, doc in enumerate(retrieved_docs, start=1):
        prompt += f"doc {i}:\n\nsource: {doc.metadata['source']}, page_content: {doc.page_content}\n"
    
    
    return prompt


def generate_1(query, history):
    logger.info(f"User-input: {query}")

    # Retrieve relavant documents
    retrieved_docs = retriever.invoke(query)

    formatted_prompt = construct_prompt(query, retrieved_docs)

    stream = text_generation(formatted_prompt)
    output = ""

    for chunk in stream:
        output += chunk.response
        yield output
    logger.info(f"Bot-response: {output}")
    return output


ZerodhatRAG = gr.ChatInterface(
    fn=generate_1, 
    type="messages",
    stop_btn=True,
    examples=zerodha_examples
)
ZerodhatRAGAgent = gr.ChatInterface(
    # fn=generate_1, 
    fn=rag_agent, 
    type="messages",
    stop_btn=True,
    examples=zerodha_examples
)

gr.TabbedInterface(
    [ZerodhatRAG, ZerodhatRAGAgent],
    ["Zerodhat RAG Overview", "Zerodhat RAG Agent Interface"],
    title="Zerodhat RAG Suite"
).launch(show_error=True)

