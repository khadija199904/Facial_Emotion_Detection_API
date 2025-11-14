from pydantic import BaseModel
from datetime import datetime
from typing import List

#  Schema pour résultat de prédiction
class PredictionResult(BaseModel):
    emotion: str
    confidence: float

# Schema pour une prédiction stockée dans database 
class Prediction(PredictionResult):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

 # Schema affichage historique des prédictions  
class HistoryPrediction(BaseModel):
    id: int
    emotion: str
    confidence: float
    created_at: datetime

    class Config:
        orm_mode = True

# Schema pour renvoyer plusieurs prédictions dans une réponse
class PredictionResponse(BaseModel):
    predictions_img: List[PredictionResult]
    message: str

