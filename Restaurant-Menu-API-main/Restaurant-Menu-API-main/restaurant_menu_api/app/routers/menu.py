"""
Menu API Router - GET/POST /menu
"""

from fastapi import APIRouter, HTTPException, Depends

from app.schemas.menu_item import MenuItemCreate, MenuItemResponse
from app.services.menu_service import MenuService
from app.repositories.menu_repository import MenuRepository

router = APIRouter(prefix="/menu", tags=["Menu"])

# Dependency Injection - FastAPI Depends
def get_menu_service() -> MenuService:
    repo = MenuRepository()
    return MenuService(repository=repo)


@router.get("", response_model=list[MenuItemResponse])
def get_menu(service: MenuService = Depends(get_menu_service)):
    """GET /menu - ดึงรายการเมนูทั้งหมด"""
    items = service.get_all_menu_items()
    return [
        MenuItemResponse(
            id=item.id,
            name=item.name,
            price=item.price,
            item_type=item.item_type.value,
            description=item.description,
            image=item.image,
        )
        for item in items
    ]


@router.post("", response_model=MenuItemResponse, status_code=201)
def create_menu_item(
    data: MenuItemCreate,
    service: MenuService = Depends(get_menu_service),
):
    """POST /menu - เพิ่มเมนูใหม่"""
    try:
        item = service.create_menu_item(
            name=data.name,
            price=data.price,
            item_type=data.item_type,
            description=data.description,
        )
        return MenuItemResponse(
            id=item.id,
            name=item.name,
            price=item.price,
            item_type=item.item_type.value,
            description=item.description,
            image=item.image,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
