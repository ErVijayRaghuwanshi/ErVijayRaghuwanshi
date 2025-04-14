import asyncio
import gradio as gr
from pydantic_ai import Agent
from pydantic_ai.tools import RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from utils import get_logger, zerodha_examples
from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

# Create a basic agent with a simple system prompt.
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
# Get logger opbject
logger = get_logger(name = __name__, log_file='Log/Zerodha_RAG.log')

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="BAAI/bge-large-en-v1.5", model_kwargs = {'device': 'cpu'})
logger.debug("Embeddings loaded")

# load from disk
db_zerodha = Chroma(persist_directory="./zerodha_db", embedding_function=embedding_function)

retriever = db_zerodha.as_retriever(search_kwargs={'k': 2})
logger.debug("Zerodha retriever loaded.")

ollama_llm = OpenAIModel(model_name="llama3.1:latest", provider=OpenAIProvider(base_url='http://localhost:11434/v1'))

agent = Agent(
    ollama_llm,
    system_prompt=system_prompt
)

# Define a tool for document retrieval using your Chroma vector retriever
@agent.tool_plain()
async def retrieve_docs(query: str) -> str:
    """Retrieve documentation sections based on a search query.
    
    Args:
        context: The call context.
        search_query: The search query.

    """
    docs = db_zerodha.asearch(query)
    gr.Info(f"retriever docs: {len(docs)} for query: {query}")
    logger.info(f"retriever docs: {len("docs")} for query: {query} {[doc.metadata['source'] for doc in docs]}")
    # Combine the retrieved documents into a single string, including source information if available
    result = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'unknown')}\nContent: {doc.page_content}"
        for doc in docs
    )
    return result

# Define an asynchronous function that streams the response.
async def stream_agent_response(user_input, history):
    logger.info(f"User-input: {user_input}")
    # Start a streaming run of the agent.
    # Note: You can pass history if needed for conversation context.
    async with agent.run_stream(user_input) as stream:
        response = ""
        # Stream the response tokens as they are generated.
        async for chunk in stream.stream_text(delta=True):
            response += chunk
            # Yield the updated response so far.
            yield response
        # logger.info(f"Bot-response: {response}")

# Create a Gradio ChatInterface that uses our async streaming function.
chat_interface = gr.ChatInterface(
    fn=stream_agent_response,
    type="messages",
    title="Pydantic AI Chat Interface",
    save_history=True
)

if __name__ == "__main__":
    chat_interface.launch(show_error=True)
