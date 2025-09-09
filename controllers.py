from fastapi import APIRouter, UploadFile, File

rag_router = APIRouter()

@rag_router.post("/documents/upload")
async def upload_documents(file: UploadFile = File(...)):
    return {"message": "Documents uploaded successfully", "file": file.filename}

@rag_router.get("/documents/")
async def list_documents():
    return {"message": "Documents listed successfully"}

@rag_router.post("/query")
async def query(query: str):
    return {"message": "Query processed successfully"}

@rag_router.get("/health")
async def health():
    return {"message": "OK"}