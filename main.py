import json

from fastapi import FastAPI

from models import StoreItem


app = FastAPI()

filename = "Store Items.json"
with open(filename, 'r') as f:
    data = json.load(f)

items: list[StoreItem] = []

for item in data:
    items.append(StoreItem(**item))


@ app.get("/accessories")
async def list_accessories() -> list[StoreItem]:
    return items


@ app.post("/accessories")
async def add_accessories(item: StoreItem) -> None:
    items.append(item)
    return "Item added successfully"


@ app.put("/accessories/{item_id}")
async def update_accessories(item_id: int, updated_item: StoreItem) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = updated_item
            return "Item updated successfully"


@ app.delete("/accessories/{item_id}")
async def delete_accessories(item_id: int) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return "Item successfully deleted"
