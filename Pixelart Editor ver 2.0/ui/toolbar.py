# ========================================
# ui/toolbar.py
# ========================================
"""Панель инструментов"""

import pygame as pg
from typing import List, Optional, Callable, Tuple  # ← ДОБАВЛЕНО Tuple
from .button import Button


class Toolbar:
    """
    Панель инструментов с кнопками
    """
    
    def __init__(self, x: int, y: int, title: str = ""):
        """
        Инициализация панели
        
        Args:
            x, y: позиция панели
            title: заголовок панели
        """
        self._x = x
        self._y = y
        self._title = title
        self._buttons: List[Button] = []
        self._font = pg.font.SysFont(None, 25)
        self._title_surface = self._font.render(title, True, (50, 50, 50))
    
    def add_button(self, button: Button):
        """Добавить кнопку на панель"""
        self._buttons.append(button)
    
    def update(self, mouse_pos: Tuple[int, int], mouse_pressed: bool):
        """Обновить все кнопки"""
        for button in self._buttons:
            button.update(mouse_pos, mouse_pressed)
    
    def render(self, screen: pg.Surface):
        """Отрисовать панель"""
        # Заголовок
        if self._title:
            screen.blit(self._title_surface, (self._x, self._y))
        
        # Кнопки
        for button in self._buttons:
            button.render(screen)
    
    def get_button(self, index: int) -> Optional[Button]:
        """Получить кнопку по индексу"""
        if 0 <= index < len(self._buttons):
            return self._buttons[index]
        return None
    
    def __repr__(self) -> str:
        return f"Toolbar('{self._title}', buttons={len(self._buttons)})"