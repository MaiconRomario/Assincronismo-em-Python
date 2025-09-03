from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse 

from src.model.settings.db_connection_handler import db_connection_handler
from src.views.pessoa_finder_view import PessoasFinderView

pessoas_routes = APIRouter()

@pessoas_routes.get("/pessoas")
async def get_pessoas(request: Request):
    Pessoas_finder_view = PessoasFinderView()

    await db_connection_handler.connect_to_db()
    http_response = await Pessoas_finder_view.handle_find_people()
    await db_connection_handler.disconnect_to_db()

    return JSONResponse(
        content=http_response['body'],
        status_code=http_response["status_code"]
    )