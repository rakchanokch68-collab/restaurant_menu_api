"""
Orders API Router - GET/POST /orders, GET /orders/{id}
"""

from fastapi import APIRouter, HTTPException, Depends

from app.schemas.order import OrderCreate, OrderResponse, OrderItemResponse
from app.services.order_service import OrderService
from app.repositories.order_repository import OrderRepository
from app.repositories.menu_repository import MenuRepository

router = APIRouter(prefix="/orders", tags=["Orders"])


# Dependency Injection
def get_order_service() -> OrderService:
    order_repo = OrderRepository()
    menu_repo = MenuRepository()
    return OrderService(order_repo=order_repo, menu_repo=menu_repo)


@router.get("", response_model=list[OrderResponse])
def get_orders(service: OrderService = Depends(get_order_service)):
    """GET /orders - ดึงคำสั่งทั้งหมด"""
    orders = service.get_all_orders()
    return [
        OrderResponse(
            id=o.id,
            table_number=o.table_number,
            items=[OrderItemResponse(**i.to_dict()) for i in o.items],
            total_amount=o.total_amount,
            status=o.status,
            created_at=o.created_at.isoformat(),
        )
        for o in orders
    ]


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    service: OrderService = Depends(get_order_service),
):
    """GET /orders/{id} - ดึงคำสั่งตาม id"""
    order = service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="ไม่พบคำสั่ง")
    return OrderResponse(
        id=order.id,
        table_number=order.table_number,
        items=[OrderItemResponse(**i.to_dict()) for i in order.items],
        total_amount=order.total_amount,
        status=order.status,
        created_at=order.created_at.isoformat(),
    )


@router.post("", response_model=OrderResponse, status_code=201)
def create_order(
    data: OrderCreate,
    service: OrderService = Depends(get_order_service),
):
    """POST /orders - สร้างคำสั่งใหม่"""
    try:
        items_data = [
            {"menu_item_id": item.menu_item_id, "quantity": item.quantity}
            for item in data.items
        ]
        order = service.create_order(
            table_number=data.table_number,
            items_data=items_data,
        )
        return OrderResponse(
            id=order.id,
            table_number=order.table_number,
            items=[OrderItemResponse(**i.to_dict()) for i in order.items],
            total_amount=order.total_amount,
            status=order.status,
            created_at=order.created_at.isoformat(),
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
