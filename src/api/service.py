from db.queries import search_cards_query, get_card_by_id_query, predict_card_query

def search_paged_cards(search_params):
    """Service function to search for paged cards."""
    return search_cards_query(search_params)

def predict_card_by_name(card_name):
    """Service function to predict card details based on a name."""
    return predict_card_query(card_name)

def get_card_by_id(card_id):
    """Service function to retrieve a card by its ID."""
    return get_card_by_id_query(card_id)