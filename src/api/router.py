from fastapi import APIRouter
from api.models import PagedRequest
from api.service import predict_card_by_name, get_card_by_id

router = APIRouter()

@router.post("/cards/search", response_model=PagedRequest)
async def get_paged_cards():
    return {"message": "This is a placeholder for paged cards."}

@router.get("/cards/predict")
async def predict_card(card_name: str):
    return predict_card_by_name(card_name)

@router.get("/cards/{card_id}")
async def get_card(card_id: str):
    return get_card_by_id(card_id)
