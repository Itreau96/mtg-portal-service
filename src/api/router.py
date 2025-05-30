import asyncio
from fastapi import APIRouter
from api.models import PagedRequest

router = APIRouter()

@router.post("/cards", response_model=PagedRequest)
async def get_paged_cards():
    return {"message": "This is a placeholder for paged cards."}

@router.get("/cards/{card_id}")
async def get_card(card_id: int):
    return {"message": f"This is a placeholder for card with ID {card_id}."}

