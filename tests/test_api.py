from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "api_app"))
from main import app



def test_format_prediction():
    client = TestClient(app)
    request = client.get("/HistoryPrediction")
    # Vérifier que le endpoint répond bien
    assert request.status_code == 200  
    
    data = request.json()
    
    # Le résultat doit être une liste
    assert isinstance(data, list)

    # Si on a au moins 1 prédiction, vérifier les champs
    if len(data) > 0:
        dict = data[0]
        for item in ["id", "emotion", "confidence", "created_at"]:
            assert item in dict

if __name__ == "__main__":
    test_format_prediction()