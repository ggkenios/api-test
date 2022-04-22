from database.coin import Base, CoinMixin

class Bitcoin(Base, CoinMixin):
    __tablename__ = "bitcoin"
