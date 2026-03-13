"""
Base Repository - Interface/Abstraction
SOLID: Interface Segregation, Dependency Inversion
"""

from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar

T = TypeVar("T")


class BaseRepository(ABC):
    """Abstract base class สำหรับ Repository - Dependency Inversion Principle"""

    @abstractmethod
    def get_all(self) -> List[T]:
        """ดึงข้อมูลทั้งหมด"""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        """ดึงข้อมูลตาม id"""
        pass
