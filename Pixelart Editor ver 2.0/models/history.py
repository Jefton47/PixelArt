# ========================================
# models/history.py
# ========================================
"""Модуль управления историей изменений (Undo/Redo)"""

from typing import List, Tuple, TYPE_CHECKING
from collections import deque

# Используем TYPE_CHECKING для избежания циклических импортов
if TYPE_CHECKING:
    from .grid import Grid


class UndoRedoManager:
    """
    Менеджер истории изменений
    Реализует паттерн Command для Undo/Redo
    """
    
    def __init__(self, grid: 'Grid', max_history: int = 50):
        """
        Инициализация менеджера
        
        Args:
            grid: сетка для управления
            max_history: максимальное количество сохраненных состояний
        """
        self._grid = grid
        self._max_history = max_history
        
        # Используем deque для эффективного управления историей
        self._undo_stack: deque = deque(maxlen=max_history)
        self._redo_stack: deque = deque(maxlen=max_history)
        
        # Сохраняем начальное состояние
        self._save_initial_state()
    
    def _save_initial_state(self):
        """Сохранить начальное состояние"""
        initial_state = self._grid.save_state()
        self._undo_stack.append(initial_state)
    
    def save_state(self):
        """
        Сохранить текущее состояние для Undo
        Очищает Redo стек
        """
        current_state = self._grid.save_state()
        self._undo_stack.append(current_state)
        
        # При новом действии очищаем redo
        self._redo_stack.clear()
    
    def can_undo(self) -> bool:
        """Можно ли выполнить Undo"""
        return len(self._undo_stack) > 1  # Оставляем хотя бы начальное состояние
    
    def can_redo(self) -> bool:
        """Можно ли выполнить Redo"""
        return len(self._redo_stack) > 0
    
    def undo(self) -> bool:
        """
        Отменить последнее действие
        
        Returns:
            True если отмена выполнена, False если нечего отменять
        """
        if not self.can_undo():
            return False
        
        # Сохраняем текущее состояние в redo
        current_state = self._undo_stack.pop()
        self._redo_stack.append(current_state)
        
        # Восстанавливаем предыдущее состояние
        previous_state = self._undo_stack[-1]
        self._grid.restore_state(previous_state)
        
        return True
    
    def redo(self) -> bool:
        """
        Повторить отмененное действие
        
        Returns:
            True если повтор выполнен, False если нечего повторять
        """
        if not self.can_redo():
            return False
        
        # Восстанавливаем состояние из redo
        next_state = self._redo_stack.pop()
        self._undo_stack.append(next_state)
        self._grid.restore_state(next_state)
        
        return True
    
    def clear_history(self):
        """Очистить всю историю"""
        self._undo_stack.clear()
        self._redo_stack.clear()
        self._save_initial_state()
    
    def get_undo_count(self) -> int:
        """Количество доступных отмен"""
        return max(0, len(self._undo_stack) - 1)
    
    def get_redo_count(self) -> int:
        """Количество доступных повторов"""
        return len(self._redo_stack)
    
    def __repr__(self) -> str:
        return f"UndoRedoManager(undo={self.get_undo_count()}, redo={self.get_redo_count()})"
