from typing import List
from pydantic import BaseModel, UUID4


class Item(BaseModel):
    category_uuids: List[UUID4]
    price: int
    title: str
    uuid: UUID4


class ItemsResponse(BaseModel):
    items: List[Item]
    user_uuid: UUID4