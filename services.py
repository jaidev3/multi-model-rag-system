import os
from fastapi import UploadFile

from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from python_multipart.multipart import MultipartFile

load_dotenv()

async def uploadDocumentsService(file: UploadFile):
    print(f"Uploading document: {file.filename}")
    contents = MultipartFile(file.file)
    # doc split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(contents)
    print(f"Splitting document into chunks: {len(chunks)}")

    # create a google generative ai embeddings model
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", api_key=os.getenv("GOOGLE_API_KEY"))

    # create a chroma collection
    collection = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="chroma_db")
    collection.persist()
    print(f"Created chroma collection: {collection}")
    return {"message": "Documents uploaded successfully", "file": file.filename, "status": "success", "docs": contents}

async def listDocumentsService():
    print("Listing documents")
    collection = Chroma(persist_directory="chroma_db")
    docs = collection.get()
    print(f"Documents: {docs}")
    return {"message": "Documents listed successfully", "status": "success", "docs": docs}

async def queryService(query: str):
    print(f"Querying: {query}")
    collection = Chroma(persist_directory="chroma_db")
    docs = collection.get()
    print(f"Documents: {docs}")
    # create a google generative ai embeddings model
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", api_key=os.getenv("GOOGLE_API_KEY"))

    # create a chroma collection
    collection = Chroma.from_documents(docs, embedding=embeddings, persist_directory="chroma_db")
    collection.persist()
    query_text = f"Query: {query}"
    docs = collection.similarity_search(query_text)
    print(f"Documents: {docs}")
    return {"message": "Query processed successfully", "status": "success", "docs": docs}

async def healthService():
    print("Health check successful")
    return {"message": "Health check successful", "status": "success"}