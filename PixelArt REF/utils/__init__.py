# ========================================
# utils/__init__.py
# ========================================
"""
Модуль утилит для Pixelart Editor

Содержит вспомогательные функции и классы:
- Vector2D: работа с 2D координатами
- math_utils: математические функции (remap, clamp, lerp и др.)
- file_utils: работа с файлами (save, load, export)
"""

from .vector2d import Vector2D
from .math_utils import (
    remap,
    clamp,
    lerp,
    normalize,
    distance,
    sign
)
from .file_utils import (
    save_grid_to_file,
    load_grid_from_file,
    export_to_png,
    open_file_dialog,
    save_file_dialog,
    get_filename_from_path
)

__all__ = [
    # Vector2D
    'Vector2D',
    
    # Math utilities
    'remap',
    'clamp',
    'lerp',
    'normalize',
    'distance',
    'sign',
    
    # File utilities
    'save_grid_to_file',
    'load_grid_from_file',
    'export_to_png',
    'open_file_dialog',
    'save_file_dialog',
    'get_filename_from_path',
]

__version__ = '1.0.0'
__author__ = 'Pixelart Editor Team'
__description__ = 'Utility functions and classes'
