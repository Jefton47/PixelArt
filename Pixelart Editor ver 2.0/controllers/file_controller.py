# ========================================
# controllers/input_controller.py
# ========================================
"""Контроллер обработки пользовательского ввода"""

import pygame as pg
from typing import Tuple, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models import Grid
    from utils import Vector2D


class InputController:
    """
    Контроллер для обработки ввода (мышь, клавиатура)
    Преобразует события pygame в игровые действия
    """
    
    def __init__(self):
        """Инициализация контроллера"""
        self._mouse_pos = (0, 0)
        self._mouse_pressed = [False, False, False]  # Left, Middle, Right
        self._mouse_clicked = [False, False, False]
        self._keys_pressed = {}
        self._keys_down = {}
        self._keys_up = {}
    
    @property
    def mouse_pos(self) -> Tuple[int, int]:
        """Текущая позиция мыши"""
        return self._mouse_pos
    
    @property
    def left_mouse_pressed(self) -> bool:
        """Левая кнопка мыши нажата"""
        return self._mouse_pressed[0]
    
    @property
    def right_mouse_pressed(self) -> bool:
        """Правая кнопка мыши нажата"""
        return self._mouse_pressed[2]
    
    @property
    def left_mouse_clicked(self) -> bool:
        """Левая кнопка мыши кликнута (одиночный клик)"""
        return self._mouse_clicked[0]
    
    def update(self, events: list):
        """
        Обновить состояние ввода на основе событий
        
        Args:
            events: список pygame событий
        """
        # Сбрасываем одиночные события
        self._mouse_clicked = [False, False, False]
        self._keys_down = {}
        self._keys_up = {}
        
        # Обновляем позицию мыши
        self._mouse_pos = pg.mouse.get_pos()
        
        # Обрабатываем события
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button <= 3:
                    self._mouse_pressed[event.button - 1] = True
                    self._mouse_clicked[event.button - 1] = True
            
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button <= 3:
                    self._mouse_pressed[event.button - 1] = False
            
            elif event.type == pg.KEYDOWN:
                self._keys_pressed[event.key] = True
                self._keys_down[event.key] = True
            
            elif event.type == pg.KEYUP:
                self._keys_pressed[event.key] = False
                self._keys_up[event.key] = True
    
    def is_key_pressed(self, key: int) -> bool:
        """Проверить нажата ли клавиша (удерживается)"""
        return self._keys_pressed.get(key, False)
    
    def is_key_down(self, key: int) -> bool:
        """Проверить была ли клавиша нажата (одиночное нажатие)"""
        return self._keys_down.get(key, False)
    
    def is_key_up(self, key: int) -> bool:
        """Проверить была ли клавиша отпущена"""
        return self._keys_up.get(key, False)
    
    def pixel_to_grid(self, pixel_x: int, pixel_y: int, cell_size: int) -> Tuple[int, int]:
        """
        Преобразовать пиксельные координаты в координаты сетки
        
        Args:
            pixel_x, pixel_y: координаты в пикселях
            cell_size: размер ячейки
        
        Returns:
            Координаты в сетке (grid_x, grid_y)
        """
        grid_x = pixel_x // cell_size
        grid_y = pixel_y // cell_size
        return (grid_x, grid_y)
    
    def __repr__(self) -> str:
        return f"InputController(mouse={self._mouse_pos}, left={self.left_mouse_pressed})"


# ========================================
# controllers/file_controller.py
# ========================================
"""Контроллер работы с файлами"""

from typing import Optional, TYPE_CHECKING
from utils import (
    save_grid_to_file,
    load_grid_from_file,
    export_to_png,
    open_file_dialog,
    save_file_dialog,
    get_filename_from_path
)

if TYPE_CHECKING:
    from models import Grid
    import pygame as pg


class FileController:
    """
    Контроллер для работы с файлами
    Управляет сохранением, загрузкой и экспортом
    """
    
    def __init__(self):
        """Инициализация контроллера"""
        self._current_filename: Optional[str] = None
        self._last_save_path: Optional[str] = None
    
    @property
    def current_filename(self) -> Optional[str]:
        """Имя текущего открытого файла"""
        return self._current_filename
    
    @property
    def has_file(self) -> bool:
        """Открыт ли файл"""
        return self._current_filename is not None
    
    def save_project(self, grid: 'Grid', filepath: Optional[str] = None) -> bool:
        """
        Сохранить проект
        
        Args:
            grid: сетка для сохранения
            filepath: путь для сохранения (None = показать диалог)
        
        Returns:
            True если успешно сохранено
        """
        # Если путь не указан - открываем диалог
        if filepath is None:
            filepath = save_file_dialog([("Text files", "*.txt")])
            if not filepath:
                return False
        
        # Сохраняем
        state = grid.save_state()
        success = save_grid_to_file(state, filepath)
        
        if success:
            self._current_filename = get_filename_from_path(filepath)
            self._last_save_path = filepath
        
        return success
    
    def load_project(self, grid: 'Grid', filepath: Optional[str] = None) -> bool:
        """
        Загрузить проект
        
        Args:
            grid: сетка для загрузки
            filepath: путь к файлу (None = показать диалог)
        
        Returns:
            True если успешно загружено
        """
        # Если путь не указан - открываем диалог
        if filepath is None:
            filepath = open_file_dialog([("Text files", "*.txt")])
            if not filepath:
                return False
        
        # Загружаем
        state = load_grid_from_file(filepath, grid.width, grid.height)
        
        if state:
            grid.restore_state(state)
            self._current_filename = get_filename_from_path(filepath)
            self._last_save_path = filepath
            return True
        
        return False
    
    def export_image(self, screen: 'pg.Surface', region: tuple, filepath: Optional[str] = None) -> bool:
        """
        Экспортировать область экрана в PNG
        
        Args:
            screen: поверхность pygame
            region: область для экспорта (x, y, width, height)
            filepath: путь для сохранения (None = показать диалог)
        
        Returns:
            True если успешно экспортировано
        """
        # Если путь не указан - открываем диалог
        if filepath is None:
            filepath = save_file_dialog([("PNG Image", "*.png")])
            if not filepath:
                return False
        
        # Экспортируем
        success = export_to_png(screen, region, filepath)
        
        return success
    
    def quick_save(self, grid: 'Grid') -> bool:
        """
        Быстрое сохранение (в последний использованный файл)
        
        Args:
            grid: сетка для сохранения
        
        Returns:
            True если успешно сохранено
        """
        if self._last_save_path:
            return self.save_project(grid, self._last_save_path)
        else:
            return self.save_project(grid, None)
    
    def new_project(self):
        """Создать новый проект (сбросить имя файла)"""
        self._current_filename = "unnamed"
        self._last_save_path = None
    
    def __repr__(self) -> str:
        return f"FileController(file='{self._current_filename}')"

