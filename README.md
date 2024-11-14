# Campus-Assisted Chatbot

Welcome to the **Campus-Assisted Chatbot**, an AI-powered assistant designed to help students and faculty access campus-related information effortlessly. This project utilizes state-of-the-art technologies to deliver accurate and relevant responses based on queries about various campus resources and information.

## Project Overview

The **Campus-Assisted Chatbot** is built using the **LLaMA 3.1 8B model**, a powerful language model fine-tuned for retrieval-augmented generation (RAG). This chatbot is capable of retrieving relevant documents and data scraped from the university's website, with the help of the **FAISS vector database** for efficient similarity search and data retrieval. Additionally, the system implements a cache mechanism to optimize performance and reduce latency during repeat queries.

## Features

- **Advanced RAG Model**: Combines the LLaMA 3.1 8B model with a retrieval mechanism for enhanced response accuracy.
- **Data Scraping**: Periodically scrapes updated information from the campus website to keep the database current and comprehensive.
- **FAISS Vector Database**: Utilizes FAISS (Facebook AI Similarity Search) for high-performance similarity search, enabling the retrieval of relevant data chunks for user queries.
- **Cache System**: Implements a caching layer that stores frequently accessed data, reducing response times for repeated queries and improving overall efficiency.
- **Contextual Responses**: Retrieves up to 5 chunks of information to provide well-contextualized answers.

## System Architecture

1. **Data Collection**: Scrapes data from the campus website and processes it to create a searchable knowledge base.
2. **Vectorization**: Converts text data into dense vector representations and stores them in a FAISS vector database.
3. **Query Processing**:
   - User input is processed and used to query the FAISS database for relevant documents.
   - The retrieved documents are passed to the LLaMA 3.1 8B model to generate a comprehensive response.
4. **Caching**: Frequently queried information is stored in a cache system to improve response time for subsequent similar queries.

## Requirements

To run this chatbot, you will need:

- **Python 3.8+**
- **FAISS** (`faiss-cpu` or `faiss-gpu` for enhanced performance)
- **Transformers** library (Hugging Face)
- **Beautiful Soup** and **Requests** for web scraping
- **Cachetools** or a similar library for caching
- Additional Python packages as specified in `requirements.txt`

