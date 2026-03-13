"""
OrderItem Model - Composition (OrderItem ประกอบด้วย MenuItem + quantity)
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .menu_item import MenuItem


@dataclass
class OrderItem:
    """
    แทนที่รายการสั่งใน Order
    Composition: OrderItem ประกอบด้วย menu_item_id และ quantity
    """
    menu_item_id: int
    quantity: int
    unit_price: float  # เก็บราคาตอนสั่ง (กรณีราคาเปลี่ยนในอนาคต)

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("จำนวนต้องมากกว่า 0")
        if self.unit_price < 0:
            raise ValueError("ราคาต้องไม่เป็นค่าติดลบ")

    @property
    def subtotal(self) -> float:
        """คำนวณยอดรวมของรายการนี้"""
        return self.unit_price * self.quantity

    def to_dict(self) -> dict:
        return {
            "menu_item_id": self.menu_item_id,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "subtotal": self.subtotal,
        }
