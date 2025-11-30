# ========================================
# tools/eyedropper_tool.py
# ========================================
"""Инструмент пипетка (выбор цвета)"""

from typing import Tuple, Optional
import pygame as pg
from .base_tool import Tool


class EyeDropperTool(Tool):
    """
    Инструмент пипетка - выбирает цвет из сетки
    """
    
    def __init__(self):
        super().__init__("EyeDropper")
        self._picked_color: Optional[Tuple[int, int, int]] = None
    
    @property
    def picked_color(self) -> Optional[Tuple[int, int, int]]:
        """Последний выбранный цвет"""
        return self._picked_color
    
    def use(self, grid, x: int, y: int, color: Tuple[int, int, int]):
        """Выбор цвета из ячейки (цвет параметр игнорируется)"""
        picked = grid.get_cell_color(x, y)
        if picked:
            self._picked_color = picked
    
    def draw_cursor(self, screen: pg.Surface, pos: Tuple[int, int], color: Tuple[int, int, int]):
        """Отрисовка курсора пипетки"""
        # Круг с крестиком внутри
        pg.draw.circle(screen, color, pos, 8, 1)
        pg.draw.line(screen, color, (pos[0] - 4, pos[1]), (pos[0] + 4, pos[1]), 1)
        pg.draw.line(screen, color, (pos[0], pos[1] - 4), (pos[0], pos[1] + 4), 1)
