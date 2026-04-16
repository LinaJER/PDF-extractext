from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core import get_db
from src.schemas import DocumentCreate, DocumentResponse
from src.services import DocumentService


router = APIRouter(prefix="/documents", tags=["documents"])


def get_service(db: Session = Depends(get_db)) -> DocumentService:
    return DocumentService(db)


@router.post("/", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
def create_document(
    data: DocumentCreate,
    service: DocumentService = Depends(get_service),
):
    return service.create(data, file_path=f"/uploads/{data.name}")


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(
    document_id: int,
    service: DocumentService = Depends(get_service),
):
    return service.get_by_id(document_id)


@router.get("/", response_model=list[DocumentResponse])
def list_documents(service: DocumentService = Depends(get_service)):
    return service.get_all()


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(
    document_id: int,
    service: DocumentService = Depends(get_service),
):
    service.delete(document_id)
