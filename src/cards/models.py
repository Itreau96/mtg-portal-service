from pydantic import BaseModel
from cards.constants import DEFAULT_PAGE_SIZE

class PagedRequest(BaseModel):
    page: int = 1
    page_size: int = DEFAULT_PAGE_SIZE
    sort_by: str = "id"
    sort_order: str = "asc"

class PagedQueryRequest(PagedRequest):
    