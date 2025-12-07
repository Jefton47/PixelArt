# ========================================
# ui/slider.py
# ========================================
"""Слайдер для регулировки значений"""

import pygame as pg
from typing import Tuple


class Slider:
    """
    Слайдер - элемент UI для выбора числового значения
    В стиле оригинального приложения
    """
    
    def __init__(self, x: int, y: int, width: int, height: int,
                 min_value: int, max_value: int, initial_value: int,
                 label: str = ""):
        """
        Инициализация слайдера
        
        Args:
            x, y: позиция ЦЕНТРА трека слайдера
            width: ширина ползунка
            height: высота ползунка
            min_value: минимальное значение
            max_value: максимальное значение
            initial_value: начальное значение
            label: подпись слайдера
        """
        self._x = x  # Центр трека
        self._y = y
        self._width = width
        self._height = height
        self._min_value = min_value
        self._max_value = max_value
        self._value = initial_value
        self._label = label
        
        # Размеры трека (УВЕЛИЧЕН)
        self._track_width = 120  # Было 100
        self._track_height = height // 2
        
        # Позиции для отрисовки (фиксированные относительно x)
        self._draw_x = x  # x - это уже позиция отрисовки
        
        self._dragging = False
        
        # Шрифт (УВЕЛИЧЕН как в оригинале)
        self._font = pg.font.SysFont(None, 25)  # Было 20
    
    @property
    def value(self) -> int:
        """Текущее значение слайдера"""
        return self._value
    
    @value.setter
    def value(self, val: int):
        """Установить значение (с ограничением)"""
        self._value = max(self._min_value, min(self._max_value, val))
    
    def _calculate_slider_position(self) -> int:
        """Вычислить позицию ползунка на основе значения"""
        range_size = self._max_value - self._min_value
        if range_size == 0:
            return self._draw_x
        
        # Позиция относительно начала трека
        track_start = self._draw_x - 60  # Трек начинается на 60px левее центра (120/2)
        normalized = (self._value - self._min_value) / range_size
        return int(track_start + normalized * self._track_width)
    
    def _calculate_value_from_position(self, mouse_x: int) -> int:
        """Вычислить значение на основе позиции мыши"""
        track_start = self._draw_x - 60
        relative_x = max(0, min(mouse_x - track_start, self._track_width))
        
        normalized = relative_x / self._track_width
        value_range = self._max_value - self._min_value
        value = self._min_value + (normalized * value_range)
        
        return int(round(value))
    
    def update(self, mouse_pos: Tuple[int, int], mouse_pressed: bool):
        """Обновить состояние слайдера"""
        slider_x = self._calculate_slider_position()
        slider_rect = pg.Rect(slider_x - self._width // 2, self._y, self._width, self._height)
        
        if mouse_pressed and slider_rect.collidepoint(mouse_pos):
            self._dragging = True
        
        if self._dragging and mouse_pressed:
            self._value = self._calculate_value_from_position(mouse_pos[0])
        
        if not mouse_pressed:
            self._dragging = False
    
    def render(self, screen: pg.Surface):
        """Отрисовать слайдер (в стиле оригинала)"""
        # Фон - серый прямоугольник (УВЕЛИЧЕН)
        bg_rect = pg.Rect(self._draw_x - 95, self._y - 30, 168, 60)  # Было 148
        pg.draw.rect(screen, (190, 190, 190), bg_rect)
        
        # Трек слайдера
        track_y = self._y + self._height // 3
        track_rect = pg.Rect(self._draw_x - 60, track_y, self._track_width, self._track_height)
        pg.draw.rect(screen, (140, 140, 140), track_rect)
        
        # Квадратик для значения (слева)
        value_box = pg.Rect(self._draw_x - 90, self._y + 1, 24, 24)
        pg.draw.rect(screen, (220, 220, 220), value_box)
        
        # Значение - текст крупнее
        value_surface = self._font.render(str(self._value), True, (30, 30, 30))
        screen.blit(value_surface, (self._draw_x - 83, self._y + 5))
        
        # Ползунок
        slider_x = self._calculate_slider_position()
        slider_rect = pg.Rect(slider_x - self._width // 2, self._y, self._width, self._height)
        pg.draw.rect(screen, (240, 240, 240), slider_rect)
        
        # Подпись
        if self._label:
            label_surface = self._font.render(self._label, True, (30, 30, 30))
            screen.blit(label_surface, (self._draw_x - 90, self._y - 25))
    
    def __repr__(self) -> str:
        return f"Slider('{self._label}', value={self._value}, range=[{self._min_value}, {self._max_value}])"