from fastapi import APIRouter

from .schema import Data
from database.database import coin_mapping, get_session


router = APIRouter()


@router.post("/coin")
async def coin(parameters: Data):
    table = coin_mapping[parameters.coin]

    # Connect to database
    with get_session() as session:
        # Type the query in sqlalchemy
        data = (
            session
            .query(table)
            .filter(table.date >= parameters.from_date)
            .filter(table.date <= parameters.to_date)
            .limit(parameters.limit)
        )

        lists = data.all()

        for item in lists:
            print(item.to_dict())
        return lists
