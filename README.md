# AnswerPDF

AnswerPDF is a web app that allows users to upload PDF files, and then get answers to questions based on the contents of the PDFs. The app uses Gemini Pro, GenAI Embeddingds by Google and Facebook AI Similarity Search to accomplish this.

This project was made as a part of the GenAI Internship at IGDTUW held in association with Sansoftech in the Summer of 2024.

## Features

- Multiple PDFs support
- PDF Text Extraction
- Text Chunking
- Vector Store Creation using FAISS and Google GenAI Embeddings
- Question Prompt Generation using Gemini Pro
- Interactive Streamlit interface for user input


## Methodology

- The PDF files uploaded by users are processed using the `PyPDF2` library to extract text from each page of the document.
- The extracted text is split into smaller chunks using a recursive character-based text splitter from `LangChain`. This helps in breaking down large texts into more manageable pieces for further processing.
- `Google Generative AI Embeddings` are used to generate embeddings for each text chunk. These embeddings are then used to create a `FAISS` vector store, which enables efficient similarity search.
- A conversational chain is set up using `LangChain` and the `Gemini Pro` model. This chain takes the user's question and context as input and generates a response based on the content of the uploaded PDF files.
- The application provides an interactive web interface using `StreamLit`, where users can upload PDF files, input questions, and receive responses summarizing the content of the files.


## Usage

1. Clone the repository
2. `cd` into the repository
```shell
cd AnswerPDF
```
3. Install the necessary dependencies
```shell
pip install -r requirements.txt
```
2. Create a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
3. Create a `.env` file and add your Google API Key:
```shell
GOOGLE_API_KEY="<your key here>"
```
4. Run the application
```shell
streamlit run app.py
```
5. Open the displayed link
6. Upload PDF files and click Submit
7. Start asking questions about their content!
