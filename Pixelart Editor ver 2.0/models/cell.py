# ========================================
# models/cell.py
# ========================================
"""Модуль ячейки сетки"""

import pygame as pg
from typing import Tuple


class Cell:
    """
    Ячейка сетки - минимальная единица рисования
    Инкапсулирует данные о цвете и размере
    """
    
    def __init__(self, size: int, color: Tuple[int, int, int] = (255, 255, 255)):
        """
        Инициализация ячейки
        
        Args:
            size: размер ячейки в пикселях
            color: цвет ячейки (R, G, B)
        """
        self._size = size
        self._color = color
        self._surface = pg.Surface((size, size))
        self._update_surface()
    
    @property
    def size(self) -> int:
        """Получить размер ячейки"""
        return self._size
    
    @property
    def color(self) -> Tuple[int, int, int]:
        """Получить текущий цвет ячейки"""
        return self._color
    
    @color.setter
    def color(self, value: Tuple[int, int, int]):
        """
        Установить новый цвет ячейки
        Автоматически обновляет surface
        """
        if self._color != value:
            self._color = value
            self._update_surface()
    
    def _update_surface(self):
        """Обновить surface с новым цветом"""
        self._surface.fill(self._color)
    
    def render(self, screen: pg.Surface, x: int, y: int):
        """
        Отрисовать ячейку на экране
        
        Args:
            screen: поверхность для рисования
            x, y: координаты верхнего левого угла
        """
        screen.blit(self._surface, (x, y))
    
    def clone(self) -> 'Cell':
        """Создать копию ячейки"""
        return Cell(self._size, self._color)
    
    def __repr__(self) -> str:
        return f"Cell(size={self._size}, color={self._color})"