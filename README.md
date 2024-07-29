# PDF Summarizer using Gemini Pro

In this project, I have implemented a PDF Summarizer web application using the Gemini Pro model from Google Generative AI. The application allows users to upload PDF files and ask questions related to the content of those files. It utilizes various libraries such as Streamlit for creating the web interface, PyPDF2 for reading PDF files, and LangChain for text processing and conversational AI. Users can upload PDF files, input questions, and receive responses summarizing the content of the files. The methodology involves text extraction, chunking, vector store creation, and question answering using the Gemini Pro model. The application provides an interactive interface for easy user interaction.

## Features

#### PDF Upload: 
Users can upload one or multiple PDF files.
#### Question Input: 
Users can input questions related to the content of the uploaded PDF files.
### Text Extraction: 
The application extracts text from the uploaded PDF files.
### Text Chunking: 
Large text is split into smaller, manageable chunks.
### Vector Store Creation: 
A FAISS vector store is created using Google Generative AI embeddings.
### Question Answering: 
The Gemini Pro model is used to generate responses to user questions based on the uploaded PDF content.
### Interactive Interface: 
The application provides an interactive interface powered by Streamlit for easy interaction.


## Methodology

### Text Extraction: 
The PDF files uploaded by users are processed using the PyPDF2 library to extract text from each page of the document.

### Text Chunking: 
The extracted text is split into smaller chunks using a recursive character-based text splitter from LangChain. This helps in breaking down large texts into more manageable pieces for further processing.

### Vector Store Creation: 
Google Generative AI embeddings are used to generate embeddings for each text chunk. These embeddings are then used to create a FAISS vector store, which enables efficient similarity search.

### Question Answering Chain: 
A conversational chain is set up using LangChain and the Gemini Pro model. This chain takes the user's question and context as input and generates a response based on the content of the uploaded PDF files.

### User Interaction: 
The application provides an interactive web interface using Streamlit, where users can upload PDF files, input questions, and receive responses summarizing the content of the files


## Dependencies

### Streamlit: 
For creating the web application interface.
### PyPDF2: 
For reading PDF files and extracting text.
### LangChain: 
For text processing, including text splitting and conversational AI capabilities.
### Google Generative AI: 
Utilized for embeddings, similarity search, and chat-based conversation using the Gemini Pro model.
### dotenv: 
For loading environment variables.


## Usage

1. Install the necessary dependencies using pip install -r requirements.txt.
2. Set up your Google API key in a .env file.
3. Run the application using streamlit run main.py.
4. Upload PDF files and start asking questions about their content.
