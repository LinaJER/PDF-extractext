from sqlalchemy.orm import Session
from src.repositories import DocumentRepository
from src.schemas import DocumentCreate, DocumentResponse
from src.core import NotFoundException


class DocumentService:
    def __init__(self, db: Session):
        self.repository = DocumentRepository(db)

    def create(self, data: DocumentCreate, file_path: str) -> DocumentResponse:
        document = self.repository.create(name=data.name, file_path=file_path)
        return DocumentResponse.model_validate(document)

    def get_by_id(self, document_id: int) -> DocumentResponse:
        document = self.repository.get_by_id(document_id)
        if not document:
            raise NotFoundException("Document")
        return DocumentResponse.model_validate(document)

    def get_all(self) -> list[DocumentResponse]:
        documents = self.repository.get_all()
        return [DocumentResponse.model_validate(d) for d in documents]

    def update_extracted_text(self, document_id: int, text: str) -> DocumentResponse:
        document = self.repository.get_by_id(document_id)
        if not document:
            raise NotFoundException("Document")
        document.extracted_text = text
        document = self.repository.update(document)
        return DocumentResponse.model_validate(document)

    def delete(self, document_id: int) -> None:
        document = self.repository.get_by_id(document_id)
        if not document:
            raise NotFoundException("Document")
        self.repository.delete(document)
