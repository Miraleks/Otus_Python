from fastapi import APIRouter

router = APIRouter(
    prefix='/items',
    tags=['items'],
)

@router.get("")
def get_items():
    return {
        "data": [
            {
                "id": 1,
                "value": "qwerty",
            },
            {
                "id": 2,
                "value": "asdfgh",
            },
        ]
    }


@router.get("/{item_id}")
def get_item(item_id: int):  # FastAPI производит приведение типов
    return {
        'item': {'id': item_id}
    }


@router.post('')
def create_item(data: dict):
    return {
        'item': '...',
    }

# @app.get("{url_path:path}")
# def all_others(
#         url_path: str,
# ):
#     return {"request to": url_path}
