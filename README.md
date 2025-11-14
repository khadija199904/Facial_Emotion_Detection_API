#  Facial-Emotion-Detection-API
<p align="center">
  <img src="https://img.shields.io/badge/Python+-blue?logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi" alt="FastAPI Badge"/>
  <img src="https://img.shields.io/badge/OpenCV-HaarCascade-red?logo=opencv" alt="OpenCV Badge"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql" alt="PostgreSQL Badge"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter" alt="Jupyter Badge"/>
  <img src="https://img.shields.io/badge/TensorFlow-orange?logo=tensorflow" alt="TensorFlow Badge"/>
</p>


---


##  Description du projet

Ce projet consiste à développer une **API d’intelligence artificielle** capable de :

- **Détecter automatiquement le visage** sur une image.  
- **Prédire l’émotion** .  
- **Enregistrer la prédiction** et les métadonnées associées dans une base de données.  

```bash
Facial_Emotion_Detection_API/
├─ api_app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schema.py
│  └─ detect_and_predict.py.py # script Python pour détecter les visages et prédire les émotions
├─ tests/
│  ├─ __init__.py
│  ├─ test_api.py
│  └─ test_load_model.py 
├─ Model_CNN_saved/
│   └─ model1.keras    
├─ Preprocessing_and_Entrainement.ipynb
│  
├─ requirements.txt
└─ README.md
  ```

## Partie Deep Learning

### Visualisation du dataset.

### Entraînement d’un modèle CNN simple
- Observation d’un surapprentissage (overfitting) initial.

### Optimisation du modèle
- Rescaling des images .  
- Data augmentation (rotation, zoom, flip, shift).

### Sauvegarde du modèle
- Modèle entraîné : `model1.keras`  
- Utilisé dans la partie backend pour les prédictions.

## Partie Backend (API)

- **Technologie :** FastAPI  
- **Interface :** Accessible via Swagger UI 

![alt text](Interface.png)

- **Endpoints :**

### POST `/predict_emotion`  

- **Description :** Prédit l’émotion à partir d’une image chargée.  
- **Paramètres :**  
  - `file` : Image (.jpg, .png, ...) à uploader.  

![alt text](Post.png)


- **Réponse :**  
```json
{
      "emotion": "Sad",
      "confidence": 0.35901835560798645
}
```

### GET `/history` 
- **Description :** Retourne l’historique des prédictions effectuées.  

![alt text](Get.png)

- **Réponse :**  

```json
{ 
 {
    "id": 85,
    "emotion": "Sad",
    "confidence": 0.35901835560798645,
    "created_at": "2025-11-14T16:12:10.458848"
  },
  {
    "id": 84,
    "emotion": "Surprise",
    "confidence": 0.28211894631385803,
    "created_at": "2025-11-14T16:11:55.683715"
  },
  {
    "id": 83,
    "emotion": "Happy",
    "confidence": 0.6230819821357727,
    "created_at": "2025-11-14T16:11:55.636840"
  },
  {
    "id": 82,
    "emotion": "Happy",
    "confidence": 0.8596352338790894,
    "created_at": "2025-11-14T14:02:44.887818"
  }
}
```
### Installation et exécution
 1. clone repo 
 ``` bash
 git clone https://github.com/khadija199904/Facial_Emotion_Detection_API.git
  cd Facial_Emotion_Detection_API
```
 2. Créer un environnement virtuel et installer les dépendances :
``` bash
 python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
```
3. Lancer l’API :
``` bash
 cd api_app
 uvicorn api_app.main:app --reload

```
4. Tester l’API
- Accéder à Swagger UI : http://127.0.0.1:8000/docs




