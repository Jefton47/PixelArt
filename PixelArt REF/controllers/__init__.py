# ========================================
# controllers/__init__.py
# ========================================
"""
Модуль контроллеров для Pixelart Editor

Реализует Controller часть MVC паттерна:
- InputController: обработка ввода (мышь, клавиатура)
- FileController: работа с файлами (save, load, export)
- CanvasController: управление холстом и рисованием
"""

from .input_controller import InputController
from .file_controller import FileController
from .canvas_controller import CanvasController

__all__ = [
    'InputController',
    'FileController',
    'CanvasController',
]

__version__ = '1.0.0'
__author__ = 'Pixelart Editor Team'
__description__ = 'Controllers for MVC pattern'