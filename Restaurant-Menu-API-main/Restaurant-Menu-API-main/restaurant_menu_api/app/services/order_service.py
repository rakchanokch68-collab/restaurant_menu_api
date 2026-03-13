"""
OrderService - Business Logic สำหรับคำสั่งซื้อ
Single Responsibility: จัดการ logic ที่เกี่ยวข้องกับ Order เท่านั้น
"""

from typing import List, Optional

from app.models.menu_item import MenuItem
from app.models.order import Order
from app.models.order_item import OrderItem
from app.repositories.menu_repository import MenuRepository
from app.repositories.order_repository import OrderRepository


class OrderService:
    """
    Service สำหรับจัดการ Order
    Composition: ใช้ทั้ง MenuRepository และ OrderRepository
    """

    def __init__(self, order_repo: OrderRepository, menu_repo: MenuRepository):
        self._order_repo = order_repo
        self._menu_repo = menu_repo

    def get_all_orders(self) -> List[Order]:
        """ดึงคำสั่งทั้งหมด"""
        return self._order_repo.get_all()

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        """ดึงคำสั่งตาม id"""
        return self._order_repo.get_by_id(order_id)

    def create_order(self, table_number: int, items_data: List[dict]) -> Order:
        """
        สร้าง Order ใหม่
        items_data: [{"menu_item_id": 1, "quantity": 2}, ...]
        """
        order_items: List[OrderItem] = []

        for item_data in items_data:
            menu_item: Optional[MenuItem] = self._menu_repo.get_by_id(item_data["menu_item_id"])
            if not menu_item:
                raise ValueError(f"ไม่พบเมนูรหัส {item_data['menu_item_id']}")

            order_items.append(
                OrderItem(
                    menu_item_id=menu_item.id,
                    quantity=item_data["quantity"],
                    unit_price=menu_item.price,
                )
            )

        return self._order_repo.add(table_number=table_number, items=order_items)
