from fastapi import APIRouter
from controllers import upload_documents, list_documents, query, health

rag_router = APIRouter()

rag_router.post("/documents/upload")(upload_documents)

rag_router.get("/documents/")(list_documents)

rag_router.post("/query")(query)

rag_router.get("/health")(health)


