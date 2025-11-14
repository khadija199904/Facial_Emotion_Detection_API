from fastapi import FastAPI, UploadFile, Depends,File
from database import Base ,engine ,SessionLocal
from sqlalchemy.orm import Session
from schema import PredictionResponse, HistoryPrediction 
from detect_and_predict import detect_and_predict_emotion
from models import Prediction
import numpy as np
from typing import List


app = FastAPI(title="API Reconnaissance Faciale des Émotions",
    description="Bienvenue sur l'API Reconnaissance Faciale des Émotions ! Cette API détecte les visages, prédit les émotions et enregistre les résultats dans une base de données PostgreSQL.")



# Configuration de la base de données 
Base.metadata.create_all(bind=engine)

# Obtenir une session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/predict_emotion",response_model=PredictionResponse)
async def predict_emotion(file: UploadFile = File(...) , db : Session = Depends(get_db)):
   file = await file.read()
   results = detect_and_predict_emotion(file)

   response = []
   for emotion, score in results:  
        # Enregistrer dans DB
        confidence= float(score)
        pred = Prediction(emotion=emotion, confidence=confidence)
        db.add(pred)
        db.commit()
        db.refresh(pred)
        response.append({
            "emotion": emotion,
            "confidence": f"{confidence:.2f}", # affichage en pourcentage
            "id": pred.id
        })
   
   
   return PredictionResponse(predictions_img=response, message="Image traité avec succes!")



@app.get("/history", response_model= List[HistoryPrediction])
def get_history(db: Session = Depends(get_db)):
    """Retourne toutes les prédictions enregistrées"""
    predictions = db.query(Prediction).order_by(Prediction.created_at.desc()).all()
    
    return predictions