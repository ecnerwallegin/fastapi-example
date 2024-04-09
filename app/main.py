from fastapi import APIRouter, FastAPI
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from app import api
from app.core.logger import logger

router = APIRouter()
app = FastAPI()

@app.get("/docs", include_in_schema=False)
def overridden_swagger():
	return get_swagger_ui_html(openapi_url="/openapi.json", title="Example FastApi Service", swagger_favicon_url="https://www.favicon.cc/?action=icon&file_id=627562#")

@app.get("/redoc", include_in_schema=False)
def overridden_redoc():
	return get_redoc_html(openapi_url="/openapi.json", title="Example FastApi Service", redoc_favicon_url="https://www.favicon.cc/?action=icon&file_id=627562#")

app.include_router(api.router, prefix='/api')

