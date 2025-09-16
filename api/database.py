""" Datasbase configuration"""
# sqlalchemy imports create_engine, declarative_base, sessionmaker
from sqlalchemy import create_engine
#pour la creation de la machine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

#declaration du chemin de la base de donnee
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#creration du moteur (engine ) de la base de donnee qui etablit la connection avec notre base SQL (movies.db)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Déffinition de la session, qui permet de creer des sesions pour interagir avec la base de donnee
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Definition de la Base , qui servira de classe de base pour nos modele SQLAlchemy
Base = declarative_base()

# tester la connection a la base de donnee
def test_db_connection():
    try:
        #essayer de se connecter a la base de donnee
        with engine.connect() as connection:
            print("Connection to the database was successful.")
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
#appeler la fonction pour tester la connection
test_db_connection()


