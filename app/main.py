import datetime
from typing import Optional

from fastapi import FastAPI
from database.database import coin_mapping, get_session


app = FastAPI()


@app.get("/coin")
async def coin(
    coin: str,
    limit: Optional[int] = 10,
    from_date: Optional[datetime.date] = None,
    to_date: Optional[datetime.date] = None
):
    # Check if coin is valid
    if coin not in ["bitcoin", "ethereum"]:
        return
    table = coin_mapping[coin]

    # Connect to database
    with get_session() as session:
        data = session.query(table)

        # If starting date is not given, set it to 1800 (Actual one is 2013-04-29)
        if not from_date:
            from_date = "1800-01-01"
        data = data.filter(table.date >= from_date)

        # If end date is not given, set it to today's date
        if not to_date:
            to_date = str(datetime.date.today())
        data = data.filter(table.date <= to_date)

        # If limit is given, apply it
        if limit:
            data = data.limit(limit)

        lists = data.all()

        for item in lists:
            print(item.to_dict())
        return lists
