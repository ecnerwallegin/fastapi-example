from app.api import v1
from fastapi import APIRouter

router = APIRouter()
router.include_router(v1.wikipedia.router, prefix='/v1/wikipedia', tags=['Wikipedia'])
