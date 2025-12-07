"""
Модуль инструментов рисования для Pixelart Editor

Реализует паттерн Strategy для различных инструментов:
- Tool: базовый абстрактный класс
- BrushTool: кисть для рисования
- EraserTool: ластик для стирания
- FillTool: заливка области
- EyeDropperTool: пипетка для выбора цвета
- ToolManager: управление инструментами
"""

from .base_tool import Tool
from .brush_tool import BrushTool
from .eraser_tool import EraserTool
from .fill_tool import FillTool
from .eyedropper_tool import EyeDropperTool
from .tool_manager import ToolManager

__all__ = [
    'Tool',
    'BrushTool',
    'EraserTool',
    'FillTool',
    'EyeDropperTool',
    'ToolManager',
]

__version__ = '1.0.0'
__author__ = 'Pixelart Editor Team'
__description__ = 'Drawing tools using Strategy pattern'