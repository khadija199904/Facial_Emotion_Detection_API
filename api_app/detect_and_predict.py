import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
from PIL import Image
import io
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../Model_CNN_saved/model1.keras")

# Charger le modèle et le classifieur
model = load_model(MODEL_PATH)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]



def detect_and_predict_emotion(img_path):
    
    # Convertir bytes → image PIL
    image = Image.open(io.BytesIO(img_path)).convert("RGB")

    # Convertir image numpy array 
    img_array = np.array(image)

    #lire l'image avec Opencv
    img_cv = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

    # Convertir en gris pour Haar Cascade
    img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    
    # Détection des visages
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.19, minNeighbors=6, minSize=(30, 30))

    if len(faces) == 0:
        return{"messge":"Aucun visage déteté"}
    
    results = []   # liste de tous les visages

    for (x, y, w, h) in faces:
        face = img_cv[y:y+h, x:x+w]

        # resize
        face_resized = cv2.resize(face, (48, 48))
         # Pour modèle RGB :
        face_reshaped = face_resized.reshape(1, 48, 48, 3)
        # Prediction
        preds = model.predict(face_reshaped)
       # Sélectionne l'émotion correspondant à la probabilité la plus élevée prédite par le modèle
        emotion = emotions[np.argmax(preds)]
       # Calcule probebilité de l'emotion   
        confidence = np.max(preds)
        confidence= float(confidence) * 100.0  
         # Dessiner rectangle vert et texte d’émotion
        cv2.rectangle(img_cv, (x, y), (x+w, y+h), (0, 255, 0), 3)
        text = f"{emotion} {confidence}%"
        cv2.putText(img_cv, text, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        results.append((emotion, confidence))
        
        

    return results





























































































             

# # Charger le modèle et le classifieur Haar Cascade
# model = load_model("Model_CNN_saved/model_CNN_simple.keras")
# print("le model chargé avec sucess")
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# print("le classifieur haar cascade chargé avec sucess")


# emotions  = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']


# # Fonction pour prédire les emotions
# def predict_emotion_from_face(face_img):
#     """
#     Prédit l'émotion à partir d'une région d'intérêt (ROI) du visage déjà extraite.
#     """

#   # Redimensionner à 48x48
#     resized_face = cv2.resize(face_img, (48, 48), interpolation=cv2.INTER_LANCZOS4)

#     # Normaliser
#     resized_face = resized_face.astype("float32") / 255.0
    
    
#     face_input = resized_face.reshape(1, 48, 48, 1)
#     # face_input = face_input.astype('float32')
#     # # Vérifier shape
#     # assert face_input.shape == (1, 48, 48, 3), f"Shape invalide: {face_input.shape}"
#     preds = model.predict(face_input, verbose=0)

#     # gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
#     # face_resized = cv2.resize(gray, img_size)
#     # face_resized = face_resized.astype("float32") / 255.0
#     # face_input = face_resized.reshape(1, 48, 48, 3)
#     # preds = model.predict(gray, verbose=0)
#     # Sélectionne l'émotion correspondant à la probabilité la plus élevée prédite par le modèle
#     emotion_label = emotions[np.max(preds)]
#     # Calcule probebilité de l'emotion 
#     score = np.max(preds)  
#     score_percent = round(float(score) * 100, 1)

#     return emotion_label, score_percent
    

# def detect_and_predict_emotion(img): 
#     """
#     Détecte les visages dans une image et prédit l'émotion de chaque visage.
#     """
#     # img = cv2.imread(img_path) 
#     # # if img is None:
#     # #     return None, None
    
#     # img = np.array(img)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.19, minNeighbors=6, minSize=(30, 30))
   
#     if len(faces) == 0:
#         return []

#     for (x, y, w, h) in faces:

#         face = img[y:y+h, x:x+w]
#         emotion ,score = predict_emotion_from_face(face)

#         # Dessiner rectangle vert et texte d’émotion
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
#         text = f"{emotion} {score}%"
#         cv2.putText(img, text, (x, y-10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        

#     # Afficher l’image originale annotée
#     cv2.imshow("Detected Faces and Emotions", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     return emotion , score
   
     


# if __name__ == "__main__":
#     images_path = r"C:\Users\khadija\Downloads\test_img"
#     output_dir = r"C:\Users\khadija\Downloads\detected_faces"
#     model_path = "Model_CNN_saved/model1.keras"

    
    

#     for filename in os.listdir(images_path):
#         img_path = os.path.join(images_path, filename)
#         img = cv2.imread(img_path)
        
#         A,B= detect_and_predict_emotion(img)
#         print(A,B)
#         cv2.imshow("Detected Faces and Emotions", img)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()





