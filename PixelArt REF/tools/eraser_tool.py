# ========================================
# tools/eraser_tool.py
# ========================================
"""Инструмент ластик"""

from typing import Tuple
import pygame as pg
from .brush_tool import BrushTool


class EraserTool(BrushTool):
    """
    Инструмент ластик - наследует от кисти, но рисует белым цветом
    """
    
    def __init__(self):
        super().__init__()
        self._name = "Eraser"
        self._background_color = (255, 255, 255)
    
    def set_background_color(self, color: Tuple[int, int, int]):
        """Установить цвет фона (для стирания)"""
        self._background_color = color
    
    def use(self, grid, x: int, y: int, color: Tuple[int, int, int]):
        """Стирание (рисование цветом фона)"""
        # Игнорируем переданный цвет и используем цвет фона
        super().use(grid, x, y, self._background_color)
    
    def draw_cursor(self, screen: pg.Surface, pos: Tuple[int, int], color: Tuple[int, int, int]):
        """Отрисовка курсора ластика (серый круг)"""
        radius = self._size * 8
        pg.draw.circle(screen, (50, 50, 50), pos, radius, 1)