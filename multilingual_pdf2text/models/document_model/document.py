from pydantic import BaseModel

class Document(BaseModel):
    document_path: str
    language: str = 'en'
    
