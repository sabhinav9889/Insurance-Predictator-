from pydantic import BaseModel, Field
from typing import Dict

class OutputRes(BaseModel):
    predicited_category: str = Field(..., description="Predicted category", example="High")
    confidence: float = Field(..., description="Confidence of the Model", example=0.39)
    class_probablities: Dict[str, float] = Field(..., description="All the class of category", example={
    "High": 0.32,
    "Low": 0.14,
    "Medium": 0.54
  })