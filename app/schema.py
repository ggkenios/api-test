import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, root_validator


class Coin(str, Enum):
    """Restrict the possible values the 'coin' parameter can take"""
    bitcoin = 'bitcoin'
    ethereum = 'ethereum'


class Data(BaseModel):
    coin: Coin
    limit: Optional[int] = 10,
    from_date: Optional[datetime.date] = "1945-04-30",
    to_date: Optional[datetime.date] = datetime.date.today()

    class Config:
        use_enum_values = True

    @root_validator()
    def validity_of_dates(cls, fields):
        """Validate that the 'from_date' is not after the 'to_date'."""
        if fields.get("from_date") and fields.get("to_date"):
            if fields["from_date"] > fields["to_date"]:
                raise ValueError("The 'from_date' parameter cannot be after the 'to_date' parameter")
        if fields.get("to_date"):
            if fields["to_date"] > datetime.date.today():
                raise ValueError("The 'to_date' parameter cannot be a date from the future")
        return fields
