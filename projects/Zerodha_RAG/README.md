# Zerodhat RAG Suite

Zerodhat RAG Suite is an AI-powered support chatbot designed to assist users with queries related to Zerodha, a leading stock brokerage firm. The chatbot leverages a Retrieval-Augmented Generation (RAG) architecture to provide accurate, detailed, and contextually relevant responses using a combination of a Chroma vector retriever and a language model.

## Features

- **Document Retrieval:** Fetch relevant information from a knowledge base for complex or detailed queries.
- **Natural Language Responses:** Generate professional and user-friendly answers to user queries.
- **Multiple Interfaces:** Includes two interfaces for different query workflows:
  - **RAG Overview:** Direct document-based query resolution.
  - **RAG Agent Interface:** Uses a conversation-driven approach to refine responses.
- **Interactive Tabs:** Allows switching between the two interfaces for tailored support.

---

## Demo

### Zerodhat RAG Overview
![Demo of Zerodhat RAG Overview](demo_rag_overview.gif)

### Zerodhat RAG Agent Interface
![Demo of Zerodhat RAG Agent Interface](demo_rag_agent_interface.gif)

---

## Installation

### Prerequisites

1. **Python  3.13.0+**
2. **Pipenv** (or any Python package manager of your choice)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Zerodha_RAG.git
    cd Zerodha_RAG
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Chroma vector store:
    - Ensure your pre-processed Zerodha documents are in the `src/zerodha_db` directory.
    - Verify that the embedding model files and `chroma.sqlite3` are correctly initialized.

4. Start the local Ollama LLM server (if not already running):
    ```bash
    ollama start
    ```

---

## Usage

1. Run the application:
    ```bash
    python src/app.py
    ```

2. Open your browser to the displayed Gradio URL.

3. Interact with the chatbot through the following interfaces:
   - **Zerodhat RAG Overview:** For direct retrieval-based answers.
   - **Zerodhat RAG Agent Interface:** For conversation-driven interactions.

---

## Code Overview

### Key Components

- **Chroma Retriever:** Fetches relevant documentation sections based on user queries.
- **Agent Framework:** Manages interaction between the language model and the retriever.
- **Gradio Interfaces:** Provides a user-friendly web interface with two tabs:
  - **`generate_1` Function:** Handles direct RAG-based queries.
  - **`rag_agent` Function:** Handles conversation-driven queries using message history.

### File Structure

```
Zerodha_RAG/
├── Experiment.ipynb               # Jupyter notebook for experiments
├── requirements.txt               # Project dependencies
└── src/
    ├── Log/
    │   └── Zerodha_RAG.log        # Log file for debugging
    ├── app.py                     # Main application script
    ├── utils.py                   # Utility functions (e.g., logging, examples)
    └── zerodha_db/                # Chroma vector store database
        ├── chroma.sqlite3         # SQLite database for vector embeddings
        └── <model_files>          # Binary files for the database
```

---

## Development

### Adding More Data
1. Prepare Zerodha documents (PDFs, text files, etc.).
2. Pre-process them into embeddings and store them in the `src/zerodha_db` directory.

### Debugging
- Check logs in:
  - `Log/Zerodha_RAG.log`
  - `src/Log/Zerodha_RAG.log`

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
