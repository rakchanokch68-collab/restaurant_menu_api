"""
MenuItem Model - Encapsulation & Enum for Item Type
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional


class ItemType(str, Enum):
    """ประเภทของเมนู - Polymorphism support"""
    FOOD = "food"
    DRINK = "drink"


@dataclass
class MenuItem:
    """
    แทนที่รายการเมนูในร้านอาหาร
    Encapsulation: ข้อมูลถูกเก็บและเข้าถึงผ่าน properties
    """
    id: int
    name: str
    price: float
    item_type: ItemType
    description: Optional[str] = None
    image: Optional[str] = None  # path เช่น images/fried-rice.png

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("ราคาต้องไม่เป็นค่าติดลบ")
        if not self.name.strip():
            raise ValueError("ชื่อเมนูต้องไม่ว่างเปล่า")

    @property
    def formatted_price(self) -> str:
        """Abstraction: ซ่อนการจัดรูปแบบราคา"""
        return f"฿{self.price:,.2f}"

    def to_dict(self) -> dict:
        """แปลงเป็น dictionary สำหรับ serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "item_type": self.item_type.value,
            "description": self.description,
            "image": self.image,
        }
