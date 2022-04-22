from database.coin import Base, CoinMixin


class Ethereum(Base, CoinMixin):
    __tablename__ = "ethereum"
