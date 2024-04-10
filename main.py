from fastapi import FastAPI
import json
import uuid
import requests

from models import Accessory


app = FastAPI()

filename = "Store Items.json"
with open(filename, 'r') as f:
    data = json.load(f)

accessories: dict[uuid.UUID, Accessory] = {}


@app.get("/accessories")
async def list_accessories() -> list[Accessory]:
    return data


@app.post("/accessories")
async def add_accessories(acc_detail: Accessory) -> uuid.UUID:
    acc_id = uuid.uuid4()
    acc = Accessory(
        id=acc_id,
        name=acc_detail.name,
        description=acc_detail.description,
        price=acc_detail.price
    )
    data[str(acc_id)] = acc.model_dump()

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    return acc_id


@app.put("/accessories")
async def update_accessories():
    pass


@app.delete("/accessories")
async def delete_accessories():
    pass
