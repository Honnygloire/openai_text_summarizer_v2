from pydantic import BaseModel, Field

class SummarizeRequest(BaseModel):
    text: str = Field(..., description="Texte à résumer")

class SummarizeResponse(BaseModel):
    summary: str = Field(..., description="Résumé généré")
