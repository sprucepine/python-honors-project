from copy import deepcopy

# In-memory demo data for drag-and-drop ordering.
_ITEMS = [
    {"id": 1, "label": "Review source data"},
    {"id": 2, "label": "Clean malformed rows"},
    {"id": 3, "label": "Run transformation"},
    {"id": 4, "label": "Publish report"},
]


def process_data(user_input: str):
    # Example logic: reverse a string and count characters
    result = user_input[::-1].upper()
    return {
        "processed_text": result,
        "length": len(user_input)
    }


def get_items():
    return deepcopy(_ITEMS)


def save_items_order(ordered_items):
    global _ITEMS

    ordered_ids = {item["id"] for item in ordered_items}
    current_ids = {item["id"] for item in _ITEMS}

    if ordered_ids != current_ids:
        raise ValueError("Reordered list must contain exactly the existing items.")

    _ITEMS = deepcopy(ordered_items)
    return deepcopy(_ITEMS)