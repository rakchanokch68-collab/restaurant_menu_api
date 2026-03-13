"""
Pydantic Schemas สำหรับ Order
"""

from typing import List
from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    """Schema สำหรับรายการใน Order"""
    menu_item_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)


class OrderItemResponse(BaseModel):
    """Schema สำหรับ Response OrderItem"""
    menu_item_id: int
    quantity: int
    unit_price: float
    subtotal: float


class OrderCreate(BaseModel):
    """Schema สำหรับสร้าง Order ใหม่"""
    table_number: int = Field(..., gt=0)
    items: List[OrderItemCreate] = Field(..., min_length=1)


class OrderResponse(BaseModel):
    """Schema สำหรับ Response Order"""
    id: int
    table_number: int
    items: List[OrderItemResponse]
    total_amount: float
    status: str
    created_at: str

    class Config:
        from_attributes = True
