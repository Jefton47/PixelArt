# ========================================
# ui/button.py
# ========================================
"""Компонент кнопки"""

import pygame as pg
from typing import Tuple, Optional, Callable


class Button:
    """
    Кнопка пользовательского интерфейса
    Поддерживает различные состояния и события
    """
    
    def __init__(self, x: int, y: int, width: int, height: int,
                 color: Tuple[int, int, int] = (100, 100, 100),
                 text: str = "",
                 font_size: int = 24,
                 text_color: Tuple[int, int, int] = (255, 255, 255)):
        """
        Инициализация кнопки
        
        Args:
            x, y: позиция кнопки
            width, height: размеры
            color: цвет кнопки
            text: текст на кнопке
            font_size: размер шрифта
            text_color: цвет текста
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._text = text
        self._font_size = font_size
        self._text_color = text_color
        
        # Состояния
        self._hovered = False
        self._clicked = False
        self._enabled = True
        
        # Surface и шрифт
        self._surface = pg.Surface((width, height))
        self._font = pg.font.SysFont(None, font_size)
        self._text_surface = self._font.render(text, True, text_color)
        
        # Callback функция при клике
        self._on_click: Optional[Callable] = None
    
    @property
    def rect(self) -> pg.Rect:
        """Получить прямоугольник кнопки"""
        return pg.Rect(self._x, self._y, self._width, self._height)
    
    @property
    def clicked(self) -> bool:
        """Кнопка в нажатом состоянии"""
        return self._clicked
    
    @clicked.setter
    def clicked(self, value: bool):
        """Установить состояние нажатия"""
        self._clicked = value
    
    @property
    def enabled(self) -> bool:
        """Кнопка активна"""
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool):
        """Включить/выключить кнопку"""
        self._enabled = value
    
    def set_on_click(self, callback: Callable):
        """Установить callback при клике"""
        self._on_click = callback
    
    def update(self, mouse_pos: Tuple[int, int], mouse_pressed: bool):
        """
        Обновить состояние кнопки
        
        Args:
            mouse_pos: позиция мыши
            mouse_pressed: нажата ли кнопка мыши
        """
        if not self._enabled:
            self._hovered = False
            return
        
        # Проверяем наведение
        self._hovered = self.rect.collidepoint(mouse_pos)
        
        # Обрабатываем клик
        if self._hovered and mouse_pressed:
            if self._on_click:
                self._on_click()
    
    def render(self, screen: pg.Surface):
        """
        Отрисовать кнопку
        
        Args:
            screen: поверхность для рисования
        """
        # Определяем прозрачность в зависимости от состояния
        if not self._enabled:
            alpha = 50
        elif self._clicked:
            alpha = 255
        elif self._hovered:
            alpha = 150
        else:
            alpha = 100
        
        # Рисуем фон кнопки
        self._surface.fill(self._color)
        self._surface.set_alpha(alpha)
        screen.blit(self._surface, (self._x, self._y))
        
        # Рисуем текст
        if self._text:
            text_x = self._x + 15
            text_y = self._y + (self._height - self._text_surface.get_height()) // 2
            screen.blit(self._text_surface, (text_x, text_y))
    
    def __repr__(self) -> str:
        return f"Button('{self._text}', pos=({self._x},{self._y}), size=({self._width}x{self._height}))"