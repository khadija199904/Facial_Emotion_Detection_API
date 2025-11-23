from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List

#  Schema pour résultat de prédiction
class PredictionResult(BaseModel):
    emotion: str
    confidence: float



 # Schema affichage historique des prédictions  
class HistoryPrediction(BaseModel):
    id: int
    emotion: str
    confidence: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
    
# Schema pour renvoyer plusieurs prédictions dans une réponse
class PredictionResponse(BaseModel):
    predictions_img: List[PredictionResult]
    message: str

