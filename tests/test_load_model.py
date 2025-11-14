import pytest
from tensorflow.keras.models import load_model
import os

model_path = 'Model_CNN_saved/model1.keras'

def test_load():
    

    model = load_model(model_path)
    # Vérifie que l'objet est bien un modèle Keras
    assert model is not None, " Le modèle n'a pas été chargé correctement."
    print(" Modèle chargé avec succès ")

if __name__ == "__main__":
    test_load()
    