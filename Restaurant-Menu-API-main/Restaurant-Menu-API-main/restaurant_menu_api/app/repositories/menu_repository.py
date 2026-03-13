"""
MenuRepository - จัดการข้อมูล MenuItem
Single Responsibility: เฉพาะการเข้าถึงข้อมูลเมนู
"""

import json
from pathlib import Path
from typing import List, Optional

from app.models.menu_item import MenuItem, ItemType


class MenuRepository:
    """Repository สำหรับ MenuItem - ใช้ JSON file เป็น storage"""

    def __init__(self, storage_path: str = "data/menu.json"):
        self._storage_path = Path(storage_path)
        self._storage_path.parent.mkdir(parents=True, exist_ok=True)
        self._items: dict[int, MenuItem] = {}
        self._next_id = 1
        self._load()

    def _load(self) -> None:
        """โหลดข้อมูลจากไฟล์"""
        IMAGE_MAP = {
            "ข้าวผัด": "fried-rice.png", "ผัดไทย": "pad-thai.png", "ส้มตำ": "som-tam.png",
            "น้ำอัดลม": "cola.png", "น้ำเปล่า": "water.png", "ชาเย็น": "thai-tea.png",
        }
        if self._storage_path.exists():
            with open(self._storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item_data in data.get("items", []):
                    img = item_data.get("image") or IMAGE_MAP.get(item_data["name"])
                    item = MenuItem(
                        id=item_data["id"],
                        name=item_data["name"],
                        price=item_data["price"],
                        item_type=ItemType(item_data["item_type"]),
                        description=item_data.get("description"),
                        image=img,
                    )
                    self._items[item.id] = item
                    self._next_id = max(self._next_id, item.id + 1)
        else:
            self._seed_default_menu()

    def _save(self) -> None:
        """บันทึกข้อมูลลงไฟล์"""
        data = {
            "items": [item.to_dict() for item in self._items.values()],
            "next_id": self._next_id,
        }
        with open(self._storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _seed_default_menu(self) -> None:
        """ข้อมูลเมนูเริ่มต้น"""
        default_items = [
            {"name": "ข้าวผัด", "price": 45.0, "item_type": "food", "image": "fried-rice.png"},
            {"name": "ผัดไทย", "price": 50.0, "item_type": "food", "image": "pad-thai.png"},
            {"name": "ส้มตำ", "price": 55.0, "item_type": "food", "image": "som-tam.png"},
            {"name": "น้ำอัดลม", "price": 15.0, "item_type": "drink", "image": "cola.png"},
            {"name": "น้ำเปล่า", "price": 10.0, "item_type": "drink", "image": "water.png"},
            {"name": "ชาเย็น", "price": 25.0, "item_type": "drink", "image": "thai-tea.png"},
        ]
        for i, d in enumerate(default_items, 1):
            item = MenuItem(
                id=i,
                name=d["name"],
                price=d["price"],
                item_type=ItemType(d["item_type"]),
                image=d.get("image"),
            )
            self._items[item.id] = item
            self._next_id = i + 1
        self._save()

    def get_all(self) -> List[MenuItem]:
        return list(self._items.values())

    def get_by_id(self, id: int) -> Optional[MenuItem]:
        return self._items.get(id)

    def add(self, name: str, price: float, item_type: ItemType, description: Optional[str] = None, image: Optional[str] = None) -> MenuItem:
        """เพิ่มเมนูใหม่"""
        item = MenuItem(
            id=self._next_id,
            name=name,
            price=price,
            item_type=item_type,
            description=description,
            image=image,
        )
        self._items[item.id] = item
        self._next_id += 1
        self._save()
        return item
