"""
Order Model - Composition (Order ประกอบด้วย OrderItems)
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from .order_item import OrderItem


@dataclass
class Order:
    """
    แทนที่คำสั่งซื้อของลูกค้า
    Composition: Order ประกอบด้วย OrderItems หลายรายการ
    """
    id: int
    table_number: int
    items: List[OrderItem]
    created_at: datetime = field(default_factory=datetime.now)
    status: str = "pending"  # pending, preparing, completed, cancelled

    def __post_init__(self) -> None:
        if self.table_number <= 0:
            raise ValueError("หมายเลขโต๊ะต้องมากกว่า 0")
        if not self.items:
            raise ValueError("คำสั่งต้องมีอย่างน้อย 1 รายการ")

    @property
    def total_amount(self) -> float:
        """คำนวณยอดรวมทั้งคำสั่ง"""
        return sum(item.subtotal for item in self.items)

    @property
    def item_count(self) -> int:
        """จำนวนรายการในคำสั่ง"""
        return sum(item.quantity for item in self.items)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "table_number": self.table_number,
            "items": [i.to_dict() for i in self.items],
            "total_amount": self.total_amount,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }
