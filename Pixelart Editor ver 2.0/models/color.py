# ========================================
# models/color.py
# ========================================
"""Модуль для работы с цветами"""

from typing import Tuple, List


class Color:
    """Класс для работы с цветами RGB"""
    
    # Предопределенные цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (200, 200, 200)
    DARK_GRAY = (50, 50, 50)
    RED = (128, 30, 30)
    
    def __init__(self, r: int, g: int, b: int):
        """
        Инициализация цвета
        
        Args:
            r: красный компонент (0-255)
            g: зеленый компонент (0-255)
            b: синий компонент (0-255)
        """
        self._r = max(0, min(255, r))
        self._g = max(0, min(255, g))
        self._b = max(0, min(255, b))
    
    @property
    def rgb(self) -> Tuple[int, int, int]:
        """Получить цвет как кортеж (R, G, B)"""
        return (self._r, self._g, self._b)
    
    @property
    def r(self) -> int:
        return self._r
    
    @property
    def g(self) -> int:
        return self._g
    
    @property
    def b(self) -> int:
        return self._b
    
    @classmethod
    def from_tuple(cls, color_tuple: Tuple[int, int, int]) -> 'Color':
        """Создать цвет из кортежа"""
        return cls(color_tuple[0], color_tuple[1], color_tuple[2])
    
    @classmethod
    def from_string(cls, color_string: str) -> 'Color':
        """
        Создать цвет из строки формата 'R,G,B'
        
        Args:
            color_string: строка вида "255,128,0"
        """
        r, g, b = map(int, color_string.strip().split(','))
        return cls(r, g, b)
    
    def to_string(self) -> str:
        """Преобразовать цвет в строку 'R,G,B'"""
        return f"{self._r},{self._g},{self._b}"
    
    def __eq__(self, other) -> bool:
        """Сравнение цветов"""
        if isinstance(other, Color):
            return self.rgb == other.rgb
        elif isinstance(other, tuple):
            return self.rgb == other
        return False
    
    def __repr__(self) -> str:
        return f"Color({self._r}, {self._g}, {self._b})"
