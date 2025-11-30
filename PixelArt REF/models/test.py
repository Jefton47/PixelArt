# ========================================
# models/test.py (ИСПРАВЛЕНО ДЛЯ РАБОТЫ ИЗ ЛЮБОЙ ПАПКИ)
# ========================================
"""
Тестирование модуля models
"""

import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Теперь можем импортировать models
from models import Color, Cell, Grid, Palette, PaletteManager, UndoRedoManager


if __name__ == "__main__":
    """Простые тесты для проверки работы моделей"""
    
    print("=== Тестирование Models ===\n")
    
    # Тест Color
    print("1. Тест Color:")
    color1 = Color(255, 128, 0)
    print(f"   Создан: {color1}")
    print(f"   RGB: {color1.rgb}")
    print(f"   String: {color1.to_string()}")
    
    color2 = Color.from_string("255,128,0")
    print(f"   Из строки: {color2}")
    print(f"   Равны: {color1 == color2}")
    
    # Тест Cell
    print("\n2. Тест Cell:")
    cell = Cell(10, (255, 0, 0))
    print(f"   Создана: {cell}")
    print(f"   Цвет: {cell.color}")
    cell.color = (0, 255, 0)
    print(f"   Новый цвет: {cell.color}")
    
    # Тест Grid
    print("\n3. Тест Grid:")
    grid = Grid(5, 5, 10, (255, 255, 255))
    print(f"   Создана: {grid}")
    print(f"   Размеры: {grid.width}x{grid.height}")
    print(f"   В пикселях: {grid.pixel_width}x{grid.pixel_height}")
    
    # Устанавливаем цвета
    grid.set_cell_color(2, 2, (255, 0, 0))
    print(f"   Цвет [2,2]: {grid.get_cell_color(2, 2)}")
    
    # Тест UndoRedoManager
    print("\n4. Тест UndoRedoManager:")
    history = UndoRedoManager(grid, max_history=10)
    print(f"   Создан: {history}")
    
    # Делаем изменение
    grid.set_cell_color(1, 1, (0, 255, 0))
    history.save_state()
    print(f"   После изменения: {history}")
    print(f"   Цвет [1,1]: {grid.get_cell_color(1, 1)}")
    
    # Отменяем
    history.undo()
    print(f"   После undo: {history}")
    print(f"   Цвет [1,1]: {grid.get_cell_color(1, 1)}")
    
    # Повторяем
    history.redo()
    print(f"   После redo: {history}")
    print(f"   Цвет [1,1]: {grid.get_cell_color(1, 1)}")
    
    print("\n=== Все тесты пройдены! ===")
    
    # Тест Palette
    print("\n5. Тест Palette:")
    palette = Palette("Тестовая", [(255, 0, 0), (0, 255, 0), (0, 0, 255)])
    print(f"   Создана: {palette}")
    print(f"   Количество цветов: {palette.count}")
    print(f"   Выбранный цвет: {palette.selected_color}")
    
    palette.select_color(1)
    print(f"   Новый выбранный цвет: {palette.selected_color}")
    
    palette.add_color((255, 255, 0))
    print(f"   После добавления: {palette.count} цветов")
    
    # Тест PaletteManager
    print("\n6. Тест PaletteManager:")
    manager = PaletteManager()
    print(f"   Создан: {manager}")
    print(f"   Текущая палитра: {manager.current_palette.name}")
    print(f"   Цветов в палитре: {manager.current_palette.count}")
    
    manager.next_palette()
    print(f"   После переключения: {manager.current_palette.name}")
    
    # Добавляем кастомную палитру
    custom = Palette("Моя палитра", [(100, 100, 100), (200, 200, 200)])
    manager.add_palette(custom)
    print(f"   Всего палитр: {manager.palette_count}")
    print(f"   Названия: {manager.get_all_palette_names()}")
    
    print("\n=== Все тесты пройдены! ===")


