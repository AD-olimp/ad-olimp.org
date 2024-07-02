from fastapi import FastAPI
from src.routes.route import router

app = FastAPI(title="AD Olimp")

app.include_router(router)

