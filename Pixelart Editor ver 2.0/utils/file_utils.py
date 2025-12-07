# ========================================
# utils/file_utils.py
# ========================================
"""Утилиты для работы с файлами"""

from typing import List, Tuple, Optional
import pygame as pg
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def save_grid_to_file(grid_state: List[List[Tuple[int, int, int]]], 
                      filepath: str) -> bool:
    """
    Сохранить состояние сетки в текстовый файл
    
    Args:
        grid_state: двумерный массив цветов
        filepath: путь к файлу для сохранения
    
    Returns:
        True если успешно сохранено
    
    Format файла:
        R,G,B
        R,G,B
        ...
    """
    try:
        # Добавляем расширение если его нет
        if not filepath.endswith('.txt'):
            filepath = filepath + '.txt'
        
        with open(filepath, 'w') as file:
            for column in grid_state:
                for color in column:
                    color_str = f"{color[0]},{color[1]},{color[2]}\n"
                    file.write(color_str)
        
        return True
    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")
        return False


def load_grid_from_file(filepath: str, 
                        width: int, 
                        height: int) -> Optional[List[List[Tuple[int, int, int]]]]:
    """
    Загрузить состояние сетки из текстового файла
    
    Args:
        filepath: путь к файлу
        width: ширина сетки
        height: высота сетки
    
    Returns:
        Двумерный массив цветов или None при ошибке
    """
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        # Создаем пустую сетку
        state: List[List[Tuple[int, int, int]]] = []
        
        line_index = 0
        for x in range(width):
            column: List[Tuple[int, int, int]] = []
            for y in range(height):
                if line_index < len(lines):
                    # Парсим цвет из строки "R,G,B"
                    color_parts = lines[line_index].strip().split(',')
                    color = (
                        int(color_parts[0]),
                        int(color_parts[1]),
                        int(color_parts[2])
                    )
                    column.append(color)
                    line_index += 1
                else:
                    # Если не хватает данных - белый цвет
                    column.append((255, 255, 255))
            state.append(column)
        
        return state
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return None


def export_to_png(screen: pg.Surface, 
                  region: Tuple[int, int, int, int],
                  filepath: str) -> bool:
    """
    Экспортировать область экрана в PNG файл
    
    Args:
        screen: поверхность Pygame
        region: (x, y, width, height) область для экспорта
        filepath: путь для сохранения
    
    Returns:
        True если успешно экспортировано
    """
    try:
        # Добавляем расширение если его нет
        if not filepath.endswith('.png'):
            filepath = filepath + '.png'
        
        x, y, width, height = region
        
        # Создаем surface для экспорта
        export_surface = pg.Surface((width, height))
        export_surface.blit(screen, (0, 0), region)
        
        # Сохраняем
        pg.image.save(export_surface, filepath)
        
        return True
    except Exception as e:
        print(f"Ошибка экспорта PNG: {e}")
        return False


def open_file_dialog(file_types: List[Tuple[str, str]] = None) -> Optional[str]:
    """
    Открыть диалог выбора файла
    
    Args:
        file_types: список типов файлов [("Описание", "*.ext")]
    
    Returns:
        Путь к выбранному файлу или None
    
    Example:
        >>> path = open_file_dialog([("Text files", "*.txt")])
    """
    if file_types is None:
        file_types = [("Text files", "*.txt")]
    
    window = Tk()
    window.withdraw()  # Скрываем основное окно
    
    filepath = askopenfilename(
        title="Открыть файл",
        filetypes=file_types
    )
    
    window.destroy()
    
    return filepath if filepath else None


def save_file_dialog(file_types: List[Tuple[str, str]] = None) -> Optional[str]:
    """
    Открыть диалог сохранения файла
    
    Args:
        file_types: список типов файлов [("Описание", "*.ext")]
    
    Returns:
        Путь для сохранения или None
    
    Example:
        >>> path = save_file_dialog([("PNG Image", "*.png")])
    """
    if file_types is None:
        file_types = [("Text files", "*.txt")]
    
    window = Tk()
    window.withdraw()
    
    filepath = asksaveasfilename(
        title="Сохранить файл",
        filetypes=file_types
    )
    
    window.destroy()
    
    return filepath if filepath else None


def get_filename_from_path(filepath: str) -> str:
    """
    Извлечь имя файла из полного пути
    
    Args:
        filepath: полный путь к файлу
    
    Returns:
        Имя файла
    
    Example:
        >>> get_filename_from_path("C:/Users/file.txt")
        'file.txt'
    """
    # Поддержка как Windows (\) так и Unix (/)
    return filepath.replace('\\', '/').split('/')[-1]
