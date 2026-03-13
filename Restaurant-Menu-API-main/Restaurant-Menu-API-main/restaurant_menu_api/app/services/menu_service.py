"""
MenuService - Business Logic สำหรับเมนู
Single Responsibility: จัดการ logic ที่เกี่ยวข้องกับเมนูเท่านั้น
"""

from typing import List, Optional

from app.models.menu_item import MenuItem, ItemType
from app.repositories.menu_repository import MenuRepository


class MenuService:
    """Service สำหรับจัดการเมนู - Dependency Injection ของ Repository"""

    def __init__(self, repository: MenuRepository):
        self._repository = repository

    def get_all_menu_items(self) -> List[MenuItem]:
        """ดึงรายการเมนูทั้งหมด"""
        return self._repository.get_all()

    def get_menu_item_by_id(self, item_id: int) -> Optional[MenuItem]:
        """ดึงเมนูตาม id"""
        return self._repository.get_by_id(item_id)

    def create_menu_item(
        self,
        name: str,
        price: float,
        item_type: ItemType,
        description: Optional[str] = None,
    ) -> MenuItem:
        """สร้างเมนูใหม่"""
        return self._repository.add(
            name=name,
            price=price,
            item_type=item_type,
            description=description,
        )
