from fastapi import FastAPI

from app import router


app = FastAPI(
    title="API Part2",
    description="Just a simple API"
)

app.include_router(router.router, tags=["v1"])
