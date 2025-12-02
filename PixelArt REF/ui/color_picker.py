# ========================================
# ui/color_picker.py
# ========================================
"""Палитра цветов с отступами"""

import pygame as pg
from typing import List, Tuple, Optional


class ColorPicker:
    """
    Выбор цвета из палитры
    С отступами между цветами и индикатором выбранного цвета
    """
    
    def __init__(self, x: int, y: int, cell_size: int = 20):
        """
        Инициализация палитры
        
        Args:
            x, y: позиция палитры
            cell_size: размер одной ячейки цвета
        """
        self._x = x
        self._y = y
        self._cell_size = cell_size
        self._gap = 5  # Отступ между рядами (как в оригинале)
        self._colors: List[Tuple[int, int, int]] = []
        self._positions: List[Tuple[int, int]] = []
        self._selected_index = 0
        self._cols = 8  # Цветов в ряду
    
    def set_colors(self, colors: List[Tuple[int, int, int]]):
        """Установить список цветов"""
        self._colors = colors
        self._calculate_positions()
    
    def set_selected_color(self, color: Tuple[int, int, int]):
        """Установить выбранный цвет (для пипетки)"""
        try:
            self._selected_index = self._colors.index(color)
        except ValueError:
            # Цвет не в палитре - ничего не делаем
            pass
    
    def _calculate_positions(self):
        """Вычислить позиции всех цветов в сетке"""
        self._positions = []
        
        for i, color in enumerate(self._colors):
            col = i % self._cols
            row = i // self._cols
            
            # Отступ только по вертикали (между рядами)
            x = self._x + col * self._cell_size  # БЕЗ отступа по горизонтали
            y = self._y + row * (self._cell_size + self._gap)  # С отступом по вертикали
            
            self._positions.append((x, y))
    
    def update(self, mouse_pos: Tuple[int, int], mouse_clicked: bool) -> Optional[Tuple[int, int, int]]:
        """
        Обновить палитру
        
        Args:
            mouse_pos: позиция мыши
            mouse_clicked: была ли нажата мышь
        
        Returns:
            Выбранный цвет или None
        """
        if not mouse_clicked:
            return None
        
        for i, (x, y) in enumerate(self._positions):
            rect = pg.Rect(x, y, self._cell_size, self._cell_size)
            if rect.collidepoint(mouse_pos):
                self._selected_index = i
                return self._colors[i]
        
        return None
    
    def render(self, screen: pg.Surface, current_color: Optional[Tuple[int, int, int]] = None):
        """
        Отрисовать палитру
        
        Args:
            screen: поверхность для рисования
            current_color: текущий выбранный цвет (для индикатора)
        """
        # Рисуем все цвета
        for i, (color, (x, y)) in enumerate(zip(self._colors, self._positions)):
            # Ячейка цвета
            rect = pg.Rect(x, y, self._cell_size, self._cell_size)
            pg.draw.rect(screen, color, rect)
            
            # Обводка для выбранного цвета (белая)
            if i == self._selected_index:
                pg.draw.rect(screen, (255, 255, 255), rect, 2)
        
        # Индикатор выбранного цвета ПОД палитрой по центру
        if current_color is None:
            current_color = self._colors[self._selected_index] if self._colors else (0, 0, 0)
        
        # Вычисляем позицию под палитрой
        rows = (len(self._colors) + self._cols - 1) // self._cols
        palette_height = rows * (self._cell_size + self._gap)
        
        # Центр палитры по X
        palette_width = self._cols * self._cell_size
        center_x = self._x + palette_width // 2
        
        # Позиция индикатора
        indicator_y = self._y + palette_height + 15
        indicator_size = 23
        
        # Серый фон
        bg_rect = pg.Rect(
            center_x - indicator_size // 2 - 5,
            indicator_y - 5,
            indicator_size + 10,
            indicator_size + 10
        )
        pg.draw.rect(screen, (235, 235, 235), bg_rect)
        
        # Цвет
        color_rect = pg.Rect(
            center_x - indicator_size // 2,
            indicator_y,
            indicator_size,
            indicator_size
        )
        pg.draw.rect(screen, current_color, color_rect)
    
    def __repr__(self) -> str:
        return f"ColorPicker(colors={len(self._colors)}, selected={self._selected_index})"