import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Constants
CHUNK_SIZE = 10000
CHUNK_OVERLAP = 1000
EMBEDDING_MODEL = "models/embedding-001"
CHAT_MODEL = "gemini-pro"
TEMPERATURE = 0.3
VECTOR_STORE_PATH = "faiss_index"

# Load environment variables and configure Google API
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

def extract_text_from_pdfs(pdf_files):
    """Extract text from a list of PDF files."""
    combined_text = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            combined_text += page.extract_text()
    return combined_text

def split_text_into_chunks(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """Split text into chunks using RecursiveCharacterTextSplitter."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)

def create_vector_store(text_chunks):
    """Create and save a FAISS vector store from text chunks."""
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(VECTOR_STORE_PATH)

def get_qa_chain():
    """Create and return a question-answering chain."""
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, say "The answer is not available in the context." Do not provide incorrect information.

    Context: {context}

    Question: {question}

    Answer:
    """
    
    model = ChatGoogleGenerativeAI(model=CHAT_MODEL, temperature=TEMPERATURE)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)

def process_user_question(question):
    """Process user question and generate a response."""
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    vector_store = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    relevant_docs = vector_store.similarity_search(question)
    
    qa_chain = get_qa_chain()
    response = qa_chain({"input_documents": relevant_docs, "question": question}, return_only_outputs=True)
    
    st.write("Reply:", response["output_text"])

def main():
    st.set_page_config("Chat PDF")
    st.header("PDF Summarizing")

    user_question = st.text_input("Ask a Question")
    if user_question:
        process_user_question(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_files = st.file_uploader("Upload your PDF Files and Click on Submit", accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner("Processing PDFs..."):
                raw_text = extract_text_from_pdfs(pdf_files)
                text_chunks = split_text_into_chunks(raw_text)
                create_vector_store(text_chunks)
                st.success("PDFs processed. You can now ask questions.")

if __name__ == "__main__":
    main()
