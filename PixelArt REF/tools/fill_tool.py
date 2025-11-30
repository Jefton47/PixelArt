# ========================================
# tools/fill_tool.py
# ========================================
"""Инструмент заливка (flood fill)"""

from typing import Tuple, Set
import pygame as pg
from .base_tool import Tool


class FillTool(Tool):
    """
    Инструмент заливка - заполняет связную область одним цветом
    Использует рекурсивный алгоритм flood fill
    """
    
    def __init__(self):
        super().__init__("Fill")
    
    def use(self, grid, x: int, y: int, color: Tuple[int, int, int]):
        """Заливка области"""
        target_color = grid.get_cell_color(x, y)
        
        # Если цвет уже совпадает - ничего не делаем
        if not target_color or target_color == color:
            return
        
        # Используем итеративный подход вместо рекурсии (избегаем stack overflow)
        self._flood_fill_iterative(grid, x, y, target_color, color)
    
    def _flood_fill_iterative(self, grid, start_x: int, start_y: int,
                              target_color: Tuple[int, int, int],
                              fill_color: Tuple[int, int, int]):
        """
        Итеративная заливка (избегает переполнения стека)
        
        Args:
            grid: сетка
            start_x, start_y: начальная позиция
            target_color: цвет который заменяем
            fill_color: новый цвет
        """
        # Стек для обработки
        stack = [(start_x, start_y)]
        visited: Set[Tuple[int, int]] = set()
        
        while stack:
            x, y = stack.pop()
            
            # Проверки
            if (x, y) in visited:
                continue
            if not grid.is_valid_position(x, y):
                continue
            if grid.get_cell_color(x, y) != target_color:
                continue
            
            # Заливаем текущую ячейку
            grid.set_cell_color(x, y, fill_color)
            visited.add((x, y))
            
            # Добавляем соседей
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))
    
    def draw_cursor(self, screen: pg.Surface, pos: Tuple[int, int], color: Tuple[int, int, int]):
        """Отрисовка курсора заливки (можно показать иконку ведра)"""
        # Простой крестик как индикатор
        size = 10
        pg.draw.line(screen, color, (pos[0] - size, pos[1]), (pos[0] + size, pos[1]), 2)
        pg.draw.line(screen, color, (pos[0], pos[1] - size), (pos[0], pos[1] + size), 2)