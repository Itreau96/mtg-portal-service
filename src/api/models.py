from pydantic import BaseModel
from typing import List, Optional
from fastapi import Query
from api.constants import DEFAULT_PAGE_SIZE

class PagedRequest(BaseModel):
    page: int = 1
    page_size: int = DEFAULT_PAGE_SIZE
    sort_by: str = "id"
    sort_order: str = "asc"

class PagedQueryRequest(PagedRequest):
    name: Optional[str] = Query(None)                           # Card name (or part of it)
    type: Optional[str] = Query(None)                           # Card type (e.g., creature, sorcery)
    color_identity: Optional[List[str]] = Query(None)           # Comma-separated list of colors
    mana_cost: Optional[str] = Query(None)                      # Comma-separated list of mana costs (corresponds to colors)
    set_code: Optional[str] = Query(None)                       # Innistrad
    keywords: Optional[List[str]] = Query(None)                 # Comma-separated list of keywords (e.g., flying, trample)
    rarity: Optional[str] = Query(None)                         # Card rarity (e.g., common, rare)
    cost: Optional[str] = Query(None)                           # Ex: >1.0, <2.0, =3.0
    power: Optional[str] = Query(None)                          # 1, 5, x, etc.
    toughness: Optional[str] = Query(None)                      # 1, 5, x, etc.
