from sqlalchemy import create_engine,  text
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Charge variables de mon env
load_dotenv()

# Lire les variables du .env
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DB_NAME  = os.getenv("POSTGRES_DB")


DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"


# Creation du moteur de la base de données
engine = create_engine(DATABASE_URL)

# Creation d'une session de base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définit la base pour les modèles ORM
Base = declarative_base()






# Test connection 
if __name__ == "__main__":
     
     # obtenir la session
     def get_db():
        db = SessionLocal()
        try:
             yield db
        finally:
          db.close()

     print(" Test de connexion à la base de données...")
     print(f"DB: {DB_NAME} | User: {USER} | Host: {HOST}:{PORT}")
     try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print(" Connexion réussie à la base de données !")
     except Exception as e:
        print(" Échec de la connexion :", e)
    