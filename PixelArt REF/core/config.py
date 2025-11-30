# ========================================
# core/config.py
# ========================================
"""Конфигурация приложения"""

from typing import Tuple


class Config:
    """
    Конфигурация приложения - все константы в одном месте
    """
    
    # Размеры окна
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 850
    
    # Параметры сетки
    GRID_WIDTH = 64
    GRID_HEIGHT = 64
    CELL_SIZE = 12
    
    # Цвета интерфейса
    BG_COLOR = (255, 255, 255)
    WALL_COLOR = (50, 50, 50)
    SIDEBAR_COLOR = (150, 150, 150)
    BOTTOM_BAR_COLOR = (80, 80, 80)
    
    # FPS
    FPS = 60
    
    # Заголовок окна
    WINDOW_TITLE = "Pixelart Editor - ООП Рефакторинг"
    
    # Пути к ресурсам
    ICON_PATH = "assets/icon.png"
    
    @classmethod
    def get_grid_pixel_size(cls) -> Tuple[int, int]:
        """Получить размер сетки в пикселях"""
        return (cls.GRID_WIDTH * cls.CELL_SIZE, cls.GRID_HEIGHT * cls.CELL_SIZE)