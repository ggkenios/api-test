from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.bitcoin import Bitcoin
from database.ethereum import Ethereum

DB_USER = "postgres"
DB_PASSWORD = "OWu7oR2v%el&%ieOjkeF7il&"
DB_URL = "34.141.175.127"
DB_PORT = "5432"

db = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_URL}:{DB_PORT}/crypto")

coin_mapping = {
    "bitcoin": Bitcoin,
    "ethereum": Ethereum,
}

def get_session():
    return Session(db)
