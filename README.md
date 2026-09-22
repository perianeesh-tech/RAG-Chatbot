# RAG Chatbot

A local Retrieval-Augmented Generation (RAG) chatbot built with Python, LlamaIndex, Ollama, and Hugging Face embeddings.

## Features

* Load documents from a file, directory, or webpage URL
* Split documents into smaller chunks for retrieval
* Generate embeddings using `BAAI/bge-small-en-v1.5`
* Store and retrieve relevant document information using LlamaIndex
* Generate answers locally using Qwen 2.5 1.5B through Ollama
* Custom prompt to reduce hallucinations and restrict answers to the provided context
* Load and process webpage content directly from a URL

## Requirements

* Python 3.12 or newer
* UV
* Ollama
* Qwen 2.5 1.5B Instruct model

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>

cd rag
```

Create the project environment and install the dependencies:

```bash
uv sync
```

Make sure Ollama is installed and the required model is available:

```bash
ollama pull qwen2.5:1.5b-instruct
```

## Running the Chatbot

Run the chatbot with:

```bash
uv run chatbot
```

The program will ask whether you want to load data from a directory, a single file, or a webpage URL.

```text
Do you want to load data from a directory, a file, or a URL? (d/f/u):
```

* `d` — Load documents from a directory
* `f` — Load a single file
* `u` — Load content from a webpage URL

After the data is loaded and indexed, you can ask questions about the provided information.

## How It Works

The chatbot follows a basic RAG pipeline:

```text
File / Directory / Webpage URL

            ↓

       Document Loading

            ↓

          Chunking

            ↓

         Embeddings

            ↓

       Vector Index

            ↓

  Relevant Context Retrieval

            ↓

       Ollama / Qwen

            ↓

          Answer
```

For files and directories, LlamaIndex loads the provided documents. For webpage URLs, `SimpleWebPageReader` retrieves the webpage content and converts it into documents.

The documents are then split into smaller chunks and converted into numerical vectors using the `BAAI/bge-small-en-v1.5` embedding model.

LlamaIndex stores the resulting embeddings in the vector index and retrieves the chunks that are most relevant to a user's question.

The retrieved context is then provided to the local Qwen 2.5 1.5B model through Ollama, which generates the final answer.

## Project Structure

```text
rag/

├── chatbot.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

The `.venv` directory is created locally by UV and is not included in the Git repository.

## Technologies

* Python
* UV
* Git
* LlamaIndex
* Ollama
* Qwen 2.5 1.5B Instruct
* Hugging Face
* BAAI BGE Small English v1.5
