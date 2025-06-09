import contextlib
import psycopg2
from api.models import PagedQueryRequest
from db.constants import PREDICT_LIMIT
from db.config import settings
from db.models import CardDict

@contextlib.contextmanager
def get_db_connection():
    conn = psycopg2.connect(settings.db_url)
    try:
        yield conn
    finally:
        conn.close()

def search_cards_query(search_params: PagedQueryRequest) -> list[CardDict]:
    """Query to search for paged cards based on search parameters."""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            # Example query, replace with actual logic
            cursor.execute("SELECT * FROM %s WHERE name ILIKE %s LIMIT %s OFFSET %s", (f"%{search_params['name']}%", search_params['limit'], search_params['offset']))
            return cursor.fetchall()

def get_card_by_id_query(card_id: str) -> CardDict:
    """Query to retrieve a card by its ID."""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {settings.card_table} WHERE id = %s"
            cursor.execute(query, (card_id,))
            return cursor.fetchone()

def predict_card_query(card_name: str) -> list[str]:
    """Query to predict card details based on a name and return an array of strings."""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            query = f"SELECT name FROM {settings.card_table} WHERE name ILIKE %s LIMIT %s"
            cursor.execute(query, (f"{card_name}%", PREDICT_LIMIT))
            results = cursor.fetchall()
            return [row[0] for row in results]
