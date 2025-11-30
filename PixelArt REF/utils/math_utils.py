# ========================================
# utils/math_utils.py
# ========================================
"""Математические утилиты"""

from typing import Union


def remap(value: float, 
          old_min: float, old_max: float,
          new_min: float, new_max: float) -> float:
    """
    Переотобразить значение из одного диапазона в другой
    
    Args:
        value: значение для переотображения
        old_min: минимум старого диапазона
        old_max: максимум старого диапазона
        new_min: минимум нового диапазона
        new_max: максимум нового диапазона
    
    Returns:
        Переотображенное значение
    
    Example:
        >>> remap(5, 0, 10, 0, 100)
        50.0
        >>> remap(750, 0, 1000, 0, 100)
        75.0
    """
    old_range = old_max - old_min
    new_range = new_max - new_min
    
    if old_range == 0:
        return new_min
    
    return (((value - old_min) * new_range) / old_range) + new_min


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Ограничить значение в пределах диапазона
    
    Args:
        value: значение для ограничения
        min_value: минимальное значение
        max_value: максимальное значение
    
    Returns:
        Значение в пределах [min_value, max_value]
    
    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(5, 0, 10)
        5
    """
    return max(min_value, min(value, max_value))


def lerp(start: float, end: float, t: float) -> float:
    """
    Линейная интерполяция между двумя значениями
    
    Args:
        start: начальное значение
        end: конечное значение
        t: параметр интерполяции (0.0 - 1.0)
    
    Returns:
        Интерполированное значение
    
    Example:
        >>> lerp(0, 100, 0.5)
        50.0
        >>> lerp(10, 20, 0.25)
        12.5
    """
    return start + (end - start) * t


def normalize(value: float, min_value: float, max_value: float) -> float:
    """
    Нормализовать значение в диапазон [0, 1]
    
    Args:
        value: значение для нормализации
        min_value: минимум диапазона
        max_value: максимум диапазона
    
    Returns:
        Нормализованное значение [0, 1]
    
    Example:
        >>> normalize(50, 0, 100)
        0.5
        >>> normalize(25, 0, 100)
        0.25
    """
    range_size = max_value - min_value
    if range_size == 0:
        return 0.0
    return (value - min_value) / range_size


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Вычислить расстояние между двумя точками
    
    Args:
        x1, y1: координаты первой точки
        x2, y2: координаты второй точки
    
    Returns:
        Расстояние между точками
    
    Example:
        >>> distance(0, 0, 3, 4)
        5.0
    """
    import math
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)


def sign(value: float) -> int:
    """
    Получить знак числа
    
    Args:
        value: число
    
    Returns:
        1 если положительное, -1 если отрицательное, 0 если ноль
    
    Example:
        >>> sign(10)
        1
        >>> sign(-5)
        -1
        >>> sign(0)
        0
    """
    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0