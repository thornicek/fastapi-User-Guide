from typing import Annotated, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Annotated[
            Item,
            Body(
                examples=[
                    {
                        "name": "Boo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                    {
                        "name": "Bar",
                        "price": "35.4",
                    },
                    {
                        "name": "Foo",
                        "price": "hundred and fifty czech crowns"
                    }
                ],
            ),
        ],
):
    results = {"item_id": item_id, "item": item}
    return results
