# ========================================
# ui/__init__.py
# ========================================
"""
Модуль пользовательского интерфейса для Pixelart Editor

Компоненты UI:
- Button: кнопки с состояниями
- Slider: слайдеры для выбора значений
- ColorPicker: выбор цветов из палитры
- Toolbar: панель инструментов
"""

from .button import Button
from .slider import Slider
from .color_picker import ColorPicker
from .toolbar import Toolbar

__all__ = [
    'Button',
    'Slider',
    'ColorPicker',
    'Toolbar',
]

__version__ = '1.0.0'
__author__ = 'Pixelart Editor Team'
__description__ = 'User interface components'
