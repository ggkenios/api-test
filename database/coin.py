from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CoinMixin:
    __table_args__ = {"schema": "coin"}

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    marketcap = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "high": self.high,
            "low": self.low,
            "open": self.open,
            "close": self.close,
            "volume": self.volume,
            "marketcap": self.marketcap,
        }
