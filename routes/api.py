from fastapi import APIRouter
from src import views

router = APIRouter()
router.include_router(views.router)