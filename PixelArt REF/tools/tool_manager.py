# ========================================
# tools/tool_manager.py
# ========================================
"""Менеджер инструментов"""

from typing import List, Optional
from .base_tool import Tool
from .brush_tool import BrushTool
from .eraser_tool import EraserTool
from .fill_tool import FillTool
from .eyedropper_tool import EyeDropperTool


class ToolManager:
    """
    Менеджер инструментов - управляет коллекцией инструментов
    Реализует паттерн Strategy для переключения между инструментами
    """
    
    # Константы для индексов инструментов
    BRUSH = 0
    ERASER = 1
    FILL = 2
    EYEDROPPER = 3
    
    def __init__(self):
        """Инициализация менеджера с предустановленными инструментами"""
        self._tools: List[Tool] = [
            BrushTool(),
            EraserTool(),
            FillTool(),
            EyeDropperTool()
        ]
        self._current_tool_index = 0
    
    @property
    def current_tool(self) -> Tool:
        """Получить текущий активный инструмент"""
        return self._tools[self._current_tool_index]
    
    @property
    def current_tool_index(self) -> int:
        """Индекс текущего инструмента"""
        return self._current_tool_index
    
    def get_tool(self, index: int) -> Optional[Tool]:
        """
        Получить инструмент по индексу
        
        Args:
            index: индекс инструмента
        
        Returns:
            Tool или None если индекс невалиден
        """
        if 0 <= index < len(self._tools):
            return self._tools[index]
        return None
    
    def select_tool(self, index: int) -> bool:
        """
        Выбрать инструмент по индексу
        
        Args:
            index: индекс инструмента
        
        Returns:
            True если успешно выбран
        """
        if 0 <= index < len(self._tools):
            self._current_tool_index = index
            return True
        return False
    
    def select_tool_by_name(self, name: str) -> bool:
        """
        Выбрать инструмент по имени
        
        Args:
            name: название инструмента
        
        Returns:
            True если найден и выбран
        """
        for i, tool in enumerate(self._tools):
            if tool.name.lower() == name.lower():
                self._current_tool_index = i
                return True
        return False
    
    def next_tool(self):
        """Переключиться на следующий инструмент (циклически)"""
        self._current_tool_index = (self._current_tool_index + 1) % len(self._tools)
    
    def previous_tool(self):
        """Переключиться на предыдущий инструмент (циклически)"""
        self._current_tool_index = (self._current_tool_index - 1) % len(self._tools)
    
    def get_brush(self) -> BrushTool:
        """Получить инструмент кисть"""
        return self._tools[self.BRUSH]
    
    def get_eraser(self) -> EraserTool:
        """Получить инструмент ластик"""
        return self._tools[self.ERASER]
    
    def get_fill(self) -> FillTool:
        """Получить инструмент заливка"""
        return self._tools[self.FILL]
    
    def get_eyedropper(self) -> EyeDropperTool:
        """Получить инструмент пипетка"""
        return self._tools[self.EYEDROPPER]
    
    def set_tool_size(self, size: int):
        """
        Установить размер текущего инструмента
        
        Args:
            size: размер (1-5)
        """
        self.current_tool.size = size
    
    def get_all_tool_names(self) -> List[str]:
        """Получить список имен всех инструментов"""
        return [tool.name for tool in self._tools]
    
    def __repr__(self) -> str:
        return f"ToolManager(current='{self.current_tool.name}', tools={len(self._tools)})"