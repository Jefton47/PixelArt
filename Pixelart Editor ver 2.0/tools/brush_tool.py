# ========================================
# tools/brush_tool.py
# ========================================
"""Инструмент кисть"""

from typing import List, Tuple
import pygame as pg
from .base_tool import Tool


class BrushTool(Tool):
    """
    Инструмент кисть - рисование с различными размерами
    """
    
    def __init__(self):
        super().__init__("Brush")
    
    def _get_brush_pattern(self) -> List[Tuple[int, int]]:
        """
        Получить паттерн кисти в зависимости от размера
        
        Returns:
            Список смещений (dx, dy) относительно центра
        """
        if self._size == 1:
            return [(0, 0)]
        
        elif self._size == 2:
            return [
                (0, 0),
                (-1, 0), (1, 0),
                (0, -1), (0, 1)
            ]
        
        elif self._size == 3:
            return [
                (0, 0),
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]
        
        elif self._size == 4:
            return [
                (0, 0),
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1),
                (-2, 0), (2, 0), (0, -2), (0, 2)
            ]
        
        else:  # size == 5
            return [
                (0, 0),
                # Крест
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                # Диагонали
                (-1, -1), (-1, 1), (1, -1), (1, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                # Дополнительные точки
                (-1, -2), (0, -2), (1, -2),
                (-1, 2), (0, 2), (1, 2),
                (-2, -1), (-2, 0), (-2, 1),
                (2, -1), (2, 0), (2, 1)
            ]
    
    def use(self, grid, x: int, y: int, color: Tuple[int, int, int]):
        """Рисование кистью"""
        pattern = self._get_brush_pattern()
        
        for dx, dy in pattern:
            grid.set_cell_color(x + dx, y + dy, color)
    
    def draw_cursor(self, screen: pg.Surface, pos: Tuple[int, int], color: Tuple[int, int, int]):
        """Отрисовка курсора кисти (круг)"""
        radius = self._size * 8
        pg.draw.circle(screen, color, pos, radius, 1)
