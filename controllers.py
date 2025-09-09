from fastapi import APIRouter, UploadFile
from services import healthService, listDocumentsService, queryService, uploadDocumentsService

rag_router = APIRouter()

@rag_router.post("/documents/upload")
async def upload_documents(file: UploadFile):
    result = await uploadDocumentsService(file)
    return result

@rag_router.get("/documents/")
async def list_documents():
    result = await listDocumentsService()
    return result

@rag_router.post("/query")
async def query(query: str):
    result = await queryService(query)
    return result

@rag_router.get("/health")
async def health():
    result = await healthService()
    return result