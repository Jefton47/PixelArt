# ========================================
# utils/vector2d.py
# ========================================
"""Модуль для работы с 2D координатами"""

from typing import Tuple
import math


class Vector2D:
    """
    Класс для работы с 2D координатами
    Упрощает работу с позициями, расстояниями и векторными операциями
    """
    
    def __init__(self, x: float = 0, y: float = 0):
        """
        Инициализация вектора
        
        Args:
            x: координата X
            y: координата Y
        """
        self._x = float(x)
        self._y = float(y)
    
    @property
    def x(self) -> float:
        """Получить X координату"""
        return self._x
    
    @x.setter
    def x(self, value: float):
        """Установить X координату"""
        self._x = float(value)
    
    @property
    def y(self) -> float:
        """Получить Y координату"""
        return self._y
    
    @y.setter
    def y(self, value: float):
        """Установить Y координату"""
        self._y = float(value)
    
    def to_tuple(self) -> Tuple[float, float]:
        """Преобразовать в кортеж (x, y)"""
        return (self._x, self._y)
    
    def to_int_tuple(self) -> Tuple[int, int]:
        """Преобразовать в кортеж целых чисел (int, int)"""
        return (int(self._x), int(self._y))
    
    @classmethod
    def from_tuple(cls, coords: Tuple[float, float]) -> 'Vector2D':
        """Создать вектор из кортежа"""
        return cls(coords[0], coords[1])
    
    def distance_to(self, other: 'Vector2D') -> float:
        """
        Вычислить расстояние до другого вектора
        
        Args:
            other: другой вектор
        
        Returns:
            Расстояние между векторами
        """
        dx = self._x - other._x
        dy = self._y - other._y
        return math.sqrt(dx * dx + dy * dy)
    
    def length(self) -> float:
        """Длина вектора (расстояние от начала координат)"""
        return math.sqrt(self._x * self._x + self._y * self._y)
    
    def normalize(self) -> 'Vector2D':
        """
        Нормализовать вектор (привести к длине 1)
        
        Returns:
            Новый нормализованный вектор
        """
        length = self.length()
        if length > 0:
            return Vector2D(self._x / length, self._y / length)
        return Vector2D(0, 0)
    
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        """Сложение векторов: v1 + v2"""
        return Vector2D(self._x + other._x, self._y + other._y)
    
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        """Вычитание векторов: v1 - v2"""
        return Vector2D(self._x - other._x, self._y - other._y)
    
    def __mul__(self, scalar: float) -> 'Vector2D':
        """Умножение на скаляр: v * 2"""
        return Vector2D(self._x * scalar, self._y * scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector2D':
        """Деление на скаляр: v / 2"""
        if scalar != 0:
            return Vector2D(self._x / scalar, self._y / scalar)
        return Vector2D(0, 0)
    
    def __eq__(self, other) -> bool:
        """Сравнение векторов: v1 == v2"""
        if isinstance(other, Vector2D):
            return self._x == other._x and self._y == other._y
        return False
    
    def __repr__(self) -> str:
        return f"Vector2D({self._x}, {self._y})"
    
    def __str__(self) -> str:
        return f"({self._x}, {self._y})"
