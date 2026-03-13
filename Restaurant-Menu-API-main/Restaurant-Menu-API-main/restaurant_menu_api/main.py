"""
จุดเข้าใช้งานแอปพลิเคชัน
รันด้วย: uvicorn app.main:app --reload หรือ python main.py
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
