# Restaurant Menu API

API สำหรับจัดการรายการเมนูและคำสั่งซื้อร้านอาหาร - โครงงานรายวิชาการเขียนโปรแกรมเชิงวัตถุ (OOP Final Project)

## สมาชิกทีม

| ชื่อ-นามสกุล | รหัสนักศึกษา | หน้าที่ความรับผิดชอบ |
|-------------|-------------|---------------------|
| รักชนก ไชยรินทร์ | 68114540496 | Backend API - Models, Repositories, Services, Routers (Menu & Order) |
| อัครพนธ์ โอมาโฮนี่ | 68114540719 | Frontend UI, Static Assets (รูปภาพ), Documentation, Project Setup |

## การประยุกต์ใช้ OOP และ SOLID

### 4 เสาหลักของ OOP
- **Encapsulation**: Class `MenuItem`, `Order`, `OrderItem` เก็บข้อมูลและ validation ในตัว
- **Abstraction**: `formatted_price`, `subtotal`, `total_amount` ซ่อนรายละเอียดการคำนวณ
- **Inheritance**: `ItemType` (Enum) รองรับ Polymorphism
- **Polymorphism**: รองรับการขยายประเภทเมนูผ่าน `ItemType`

### Composition
- `Order` ประกอบด้วย `OrderItem` หลายรายการ
- `OrderItem` อ้างอิง `MenuItem` ผ่าน menu_item_id

### SOLID Principles
- **S**ingle Responsibility: Repository (ข้อมูล), Service (business logic), Router (API)
- **O**pen/Closed: ขยายได้โดยเพิ่ม Class ใหม่ ไม่ต้องแก้ของเดิม
- **L**iskov Substitution: BaseRepository เป็น interface สำหรับ Repository
- **I**nterface Segregation: แยก Repository ตาม domain
- **D**ependency Inversion: Service รับ Repository ผ่าน Constructor Injection

### Design Patterns
- **Repository Pattern**: แยกการเข้าถึงข้อมูล (MenuRepository, OrderRepository)
- **Dependency Injection**: FastAPI `Depends()` สำหรับ Service และ Repository

## วิธีการติดตั้ง

### 1. Clone Repository

```bash
git clone <repository-url>
cd restaurant_menu_api
```

### 2. สร้าง Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

หรือใช้ pyproject.toml:

```bash
pip install -e .
```

## วิธีใช้งาน

### รัน Server

```bash
uvicorn app.main:app --reload
```

หรือ:

```bash
python main.py
```

Server จะรันที่ http://127.0.0.1:8000

### API Documentation (Swagger)

เปิดเบราว์เซอร์ไปที่: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | คำอธิบาย |
|--------|----------|----------|
| GET | `/menu` | ดึงรายการเมนูทั้งหมด |
| POST | `/menu` | เพิ่มเมนูใหม่ |
| GET | `/orders` | ดึงคำสั่งทั้งหมด |
| POST | `/orders` | สร้างคำสั่งใหม่ |
| GET | `/orders/{id}` | ดึงคำสั่งตาม id |

### ตัวอย่าง POST /menu

```json
{
  "name": "ข้าวไข่เจียว",
  "price": 40,
  "item_type": "food",
  "description": "ไข่เจียวฟู"
}
```

### ตัวอย่าง POST /orders

```json
{
  "table_number": 5,
  "items": [
    {"menu_item_id": 1, "quantity": 2},
    {"menu_item_id": 4, "quantity": 3}
  ]
}
```

## โครงสร้างโปรเจกต์

```
restaurant_menu_api/
├── app/
│   ├── models/       # Domain models (MenuItem, Order, OrderItem)
│   ├── schemas/      # Pydantic request/response
│   ├── repositories/ # การเข้าถึงข้อมูล
│   ├── services/     # Business logic
│   ├── routers/      # API endpoints
│   └── main.py       # FastAPI app
├── data/             # ข้อมูล JSON (สร้างอัตโนมัติ)
├── main.py           # จุดเข้าใช้งาน
├── requirements.txt
├── pyproject.toml
└── README.md
```
