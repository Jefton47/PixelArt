# ========================================
# controllers/canvas_controller.py
# ========================================
"""Контроллер управления холстом"""

from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from models import Grid
    from tools import ToolManager


class CanvasController:
    """
    Контроллер холста - управляет рисованием и взаимодействием
    """
    
    def __init__(self, grid: 'Grid', tool_manager: 'ToolManager'):
        """
        Инициализация контроллера
        
        Args:
            grid: сетка для рисования
            tool_manager: менеджер инструментов
        """
        self._grid = grid
        self._tool_manager = tool_manager
        self._is_drawing = False
        self._current_color = (0, 0, 0)
    
    @property
    def grid(self) -> 'Grid':
        """Получить сетку"""
        return self._grid
    
    @property
    def current_color(self) -> Tuple[int, int, int]:
        """Текущий цвет рисования"""
        return self._current_color
    
    @current_color.setter
    def current_color(self, color: Tuple[int, int, int]):
        """Установить цвет рисования"""
        self._current_color = color
    
    def start_drawing(self):
        """Начать рисование"""
        self._is_drawing = True
        # Сохраняем состояние для Undo
        self._grid.history.save_state()
    
    def stop_drawing(self):
        """Закончить рисование"""
        self._is_drawing = False
    
    def draw_at(self, grid_x: int, grid_y: int):
        """
        Рисовать в указанной позиции текущим инструментом
        
        Args:
            grid_x, grid_y: координаты в сетке
        """
        current_tool = self._tool_manager.current_tool
        
        # Если пипетка - берем цвет с холста
        if current_tool.name == "EyeDropper":
            current_tool.use(self._grid, grid_x, grid_y, self._current_color)
            if current_tool.picked_color:
                self._current_color = current_tool.picked_color
            return
        
        # Остальные инструменты
        current_tool.use(self._grid, grid_x, grid_y, self._current_color)
    
    def clear_canvas(self):
        """Очистить холст"""
        self._grid.history.save_state()
        self._grid.clear()
    
    def undo(self) -> bool:
        """
        Отменить последнее действие
        
        Returns:
            True если отмена выполнена
        """
        return self._grid.history.undo()
    
    def redo(self) -> bool:
        """
        Повторить отмененное действие
        
        Returns:
            True если повтор выполнен
        """
        return self._grid.history.redo()
    
    def can_undo(self) -> bool:
        """Можно ли отменить"""
        return self._grid.history.can_undo()
    
    def can_redo(self) -> bool:
        """Можно ли повторить"""
        return self._grid.history.can_redo()
    
    
    
    def pick_color_at(self, grid_x: int, grid_y: int) -> Tuple[int, int, int]:
        """
        Выбрать цвет из ячейки
        
        Args:
            grid_x, grid_y: координаты в сетке
        
        Returns:
            Цвет ячейки
        """
        color = self._grid.get_cell_color(grid_x, grid_y)
        if color:
            self._current_color = color
            return color
        return self._current_color
    
    def __repr__(self) -> str:
        return f"CanvasController(grid={self._grid}, color={self._current_color})"