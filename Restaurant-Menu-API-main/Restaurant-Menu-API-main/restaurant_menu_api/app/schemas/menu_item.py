"""
Pydantic Schemas สำหรับ MenuItem
"""

from typing import Optional
from pydantic import BaseModel, Field

from app.models.menu_item import ItemType


class MenuItemCreate(BaseModel):
    """Schema สำหรับสร้าง MenuItem ใหม่"""
    name: str = Field(..., min_length=1, description="ชื่อเมนู")
    price: float = Field(..., gt=0, description="ราคา")
    item_type: ItemType = Field(..., description="ประเภท: food หรือ drink")
    description: Optional[str] = None


class MenuItemResponse(BaseModel):
    """Schema สำหรับ Response MenuItem"""
    id: int
    name: str
    price: float
    item_type: str
    description: Optional[str] = None
    image: Optional[str] = None

    class Config:
        from_attributes = True
