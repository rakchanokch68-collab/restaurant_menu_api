"""
Restaurant Menu API - Main Application
OOP Final Project: การประยุกต์ใช้ OOP, SOLID, Design Patterns
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routers import menu, orders

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="Restaurant Menu API",
    description="API สำหรับจัดการรายการเมนูและคำสั่งซื้อร้านอาหาร",
    version="1.0.0",
)

# CORS - ให้ frontend เรียกใช้ได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# รวม Routers
app.include_router(menu.router)
app.include_router(orders.router)

# Static files - รูปภาพ
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/")
def root():
    """แสดง UI หลัก"""
    return FileResponse(BASE_DIR / "static" / "index.html")
