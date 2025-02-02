# Local RAG-based Content Engine 
This repository contains a local **RAG**-based Content Engine designed to analyze and compare PDF documents. The engine utilizes a local Large Language Model (LLM), local embeddings, a vector store, and a Streamlit chatbot to generate insights and comparisons.

The system runs entirely locally without relying on any external APIs, ensuring data privacy and security for users. It is implemented using various tools such as Langchain, Ollama, ChromaDB, Streamlit, and PyTorch, providing a robust and scalable solution for document analysis.

## Features
- Local document analysis and comparison using PDF files.
- Insights and comparisons are generated via a chatbot interface built with Streamlit.
- Ensures data privacy by running all processes locally, without using external APIs.
- Built with modern AI Frameworks, including embeddings and local LLMs.

## Tech Stack
- **Python**: Programming language for building the application.
- **Langchain**: Framework for working with language models and integrating with the local environment.
- **Ollama**: Local large language model to generate insights and responses.
- **ChromaDB**: Vector database for managing embeddings and document retrieval.
- **Streamlit**: Interactive UI for the chatbot interface and user interaction.
- **PyTorch**: Framework for machine learning model development and execution.
- **OS Module**: Used for interacting with the file system (e.g., loading PDFs).
- **PyPDF**: Library for parsing and extracting content from PDF documents.

## Data Privacy
This system operates entirely locally, which means that no data is sent to external servers or APIs. All processes, including the analysis of PDF documents, embedding generation, and the chatbot's responses, occur within your local environment.

