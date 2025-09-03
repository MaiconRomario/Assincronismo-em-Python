from fastapi import FastAPI
from src.main.routes.pessoas_route import pessoas_routes

app = FastAPI()
app.include_router(pessoas_routes)