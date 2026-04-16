from .base import BaseSchema, TimestampSchema


class DocumentBase(BaseSchema):
    name: str
    file_path: str


class DocumentCreate(BaseSchema):
    name: str


class DocumentResponse(TimestampSchema):
    id: int
    name: str
    file_path: str
    extracted_text: str | None = None


__all__ = [
    "BaseSchema",
    "TimestampSchema",
    "DocumentBase",
    "DocumentCreate",
    "DocumentResponse",
]
