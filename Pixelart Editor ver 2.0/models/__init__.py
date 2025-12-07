"""
Модуль моделей данных для Pixelart Editor

Содержит базовые структуры данных:
- Color: работа с цветами
- Cell: ячейка сетки
- Grid: сетка для рисования
- Palette: цветовые палитры
- UndoRedoManager: история изменений
"""

from .color import Color
from .cell import Cell
from .grid import Grid
from .palette import Palette, PaletteManager
from .history import UndoRedoManager

__all__ = [
    'Color',
    'Cell',
    'Grid',
    'Palette',
    'PaletteManager',
    'UndoRedoManager',
]

__version__ = '1.0.0'
__author__ = 'Pixelart Editor Team'
__description__ = 'Data models for pixel art editor'
