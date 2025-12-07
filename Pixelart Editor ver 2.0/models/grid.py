# ========================================
# models/grid.py (ПОЛНОСТЬЮ ИСПРАВЛЕНО)
# ========================================
"""Модуль сетки для рисования"""

from typing import List, Tuple, Optional
import pygame as pg
from .cell import Cell


class Grid:
    """
    Сетка для рисования - основная модель данных
    Хранит двумерный массив ячеек
    """
    
    def __init__(self, width: int, height: int, cell_size: int, 
                 background_color: Tuple[int, int, int] = (255, 255, 255)):
        """
        Инициализация сетки
        
        Args:
            width: количество ячеек по горизонтали
            height: количество ячеек по вертикали
            cell_size: размер одной ячейки в пикселях
            background_color: цвет фона (по умолчанию белый)
        """
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._background_color = background_color
        
        # Создаем двумерный массив ячеек
        self._cells: List[List[Cell]] = []
        for i in range(width):
            column = []
            for j in range(height):
                column.append(Cell(cell_size, background_color))
            self._cells.append(column)
        
        # ДОБАВЛЕНО: Создаем менеджер истории
        from .history import UndoRedoManager
        self._history = UndoRedoManager(self)
    
    @property
    def width(self) -> int:
        """Ширина сетки (количество ячеек)"""
        return self._width
    
    @property
    def height(self) -> int:
        """Высота сетки (количество ячеек)"""
        return self._height
    
    @property
    def cell_size(self) -> int:
        """Размер одной ячейки"""
        return self._cell_size
    
    @property
    def background_color(self) -> Tuple[int, int, int]:
        """Цвет фона"""
        return self._background_color
    
    @property
    def pixel_width(self) -> int:
        """Ширина в пикселях"""
        return self._width * self._cell_size
    
    @property
    def pixel_height(self) -> int:
        """Высота в пикселях"""
        return self._height * self._cell_size
    
    # ДОБАВЛЕНО: Свойство для доступа к истории
    @property
    def history(self):
        """Менеджер истории изменений"""
        return self._history
    
    def get_cell(self, x: int, y: int) -> Optional[Cell]:
        """
        Получить ячейку по координатам
        
        Args:
            x: координата по X
            y: координата по Y
        
        Returns:
            Cell или None если координаты вне границ
        """
        if self.is_valid_position(x, y):
            return self._cells[x][y]
        return None
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """Проверить валидность координат"""
        return 0 <= x < self._width and 0 <= y < self._height
    
    def set_cell_color(self, x: int, y: int, color: Tuple[int, int, int]) -> bool:
        """
        Установить цвет ячейки
        
        Args:
            x: координата по X
            y: координата по Y
            color: новый цвет
        
        Returns:
            True если успешно, False если координаты невалидны
        """
        cell = self.get_cell(x, y)
        if cell:
            cell.color = color
            return True
        return False
    
    def get_cell_color(self, x: int, y: int) -> Optional[Tuple[int, int, int]]:
        """Получить цвет ячейки"""
        cell = self.get_cell(x, y)
        return cell.color if cell else None
    
    def clear(self):
        """Очистить всю сетку (залить фоновым цветом)"""
        for column in self._cells:
            for cell in column:
                cell.color = self._background_color
    
    def render(self, screen: pg.Surface, offset_x: int = 0, offset_y: int = 0):
        """
        Отрисовать всю сетку
        
        Args:
            screen: поверхность для рисования
            offset_x: смещение по X
            offset_y: смещение по Y
        """
        for x in range(self._width):
            for y in range(self._height):
                pixel_x = offset_x + (x * self._cell_size)
                pixel_y = offset_y + (y * self._cell_size)
                self._cells[x][y].render(screen, pixel_x, pixel_y)
    
    def save_state(self) -> List[List[Tuple[int, int, int]]]:
        """
        Сохранить текущее состояние сетки
        
        Returns:
            Двумерный массив цветов
        """
        state = []
        for column in self._cells:
            column_colors = [cell.color for cell in column]
            state.append(column_colors)
        return state
    
    def restore_state(self, state: List[List[Tuple[int, int, int]]]):
        """
        Восстановить состояние сетки
        
        Args:
            state: двумерный массив цветов
        """
        for x in range(min(len(state), self._width)):
            for y in range(min(len(state[x]), self._height)):
                self._cells[x][y].color = state[x][y]
    
    def __repr__(self) -> str:
        return f"Grid({self._width}x{self._height}, cell_size={self._cell_size})"