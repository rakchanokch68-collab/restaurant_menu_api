"""
OrderRepository - จัดการข้อมูล Order
Single Responsibility: เฉพาะการเข้าถึงข้อมูลคำสั่งซื้อ
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from app.models.order import Order
from app.models.order_item import OrderItem


class OrderRepository:
    """Repository สำหรับ Order - ใช้ JSON file เป็น storage"""

    def __init__(self, storage_path: str = "data/orders.json"):
        self._storage_path = Path(storage_path)
        self._storage_path.parent.mkdir(parents=True, exist_ok=True)
        self._orders: dict[int, Order] = {}
        self._next_id = 1
        self._load()

    def _load(self) -> None:
        """โหลดข้อมูลจากไฟล์"""
        if self._storage_path.exists():
            with open(self._storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for order_data in data.get("orders", []):
                    items = [
                        OrderItem(
                            menu_item_id=i["menu_item_id"],
                            quantity=i["quantity"],
                            unit_price=i["unit_price"],
                        )
                        for i in order_data["items"]
                    ]
                    order = Order(
                        id=order_data["id"],
                        table_number=order_data["table_number"],
                        items=items,
                        status=order_data.get("status", "pending"),
                        created_at=datetime.fromisoformat(order_data["created_at"]),
                    )
                    self._orders[order.id] = order
                    self._next_id = max(self._next_id, order.id + 1)
        self._save()

    def _save(self) -> None:
        """บันทึกข้อมูลลงไฟล์"""
        data = {
            "orders": [o.to_dict() for o in self._orders.values()],
            "next_id": self._next_id,
        }
        with open(self._storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_all(self) -> List[Order]:
        return list(self._orders.values())

    def get_by_id(self, id: int) -> Optional[Order]:
        return self._orders.get(id)

    def add(self, table_number: int, items: List[OrderItem]) -> Order:
        """เพิ่ม Order ใหม่"""
        order = Order(
            id=self._next_id,
            table_number=table_number,
            items=items,
            created_at=datetime.now(),
        )
        self._next_id += 1
        self._orders[order.id] = order
        self._save()
        return order
