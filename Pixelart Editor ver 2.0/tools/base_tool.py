# ========================================
# tools/base_tool.py
# ========================================
"""Базовый класс для всех инструментов"""

from abc import ABC, abstractmethod
from typing import Tuple, TYPE_CHECKING
import pygame as pg

if TYPE_CHECKING:
    from models import Grid


class Tool(ABC):
    """
    Абстрактный базовый класс для всех инструментов рисования
    Реализует паттерн Strategy
    """
    
    def __init__(self, name: str):
        """
        Инициализация инструмента
        
        Args:
            name: название инструмента
        """
        self._name = name
        self._size = 3  # Размер инструмента (1-5)
    
    @property
    def name(self) -> str:
        """Название инструмента"""
        return self._name
    
    @property
    def size(self) -> int:
        """Размер инструмента"""
        return self._size
    
    @size.setter
    def size(self, value: int):
        """Установить размер (1-5)"""
        self._size = max(1, min(5, value))
    
    @abstractmethod
    def use(self, grid: 'Grid', x: int, y: int, color: Tuple[int, int, int]):
        """
        Использовать инструмент на сетке
        
        Args:
            grid: сетка для рисования
            x: координата X (в ячейках)
            y: координата Y (в ячейках)
            color: цвет для применения
        """
        pass
    
    @abstractmethod
    def draw_cursor(self, screen: pg.Surface, pos: Tuple[int, int], color: Tuple[int, int, int]):
        """
        Отрисовать курсор инструмента
        
        Args:
            screen: поверхность для рисования
            pos: позиция курсора (в пикселях)
            color: цвет курсора
        """
        pass
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}', size={self._size})"