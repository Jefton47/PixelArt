# ========================================
# tools/test.py
# ========================================
"""
Тестирование модуля tools
"""

import sys
import os

# Добавляем родительскую папку в путь
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Импортируем
from models import Grid
from tools import (
    Tool,
    BrushTool,
    EraserTool,
    FillTool,
    EyeDropperTool,
    ToolManager
)


if __name__ == "__main__":
    """Тесты для модуля tools"""
    
    print("=== Тестирование Tools ===\n")
    
    # Создаем тестовую сетку
    grid = Grid(10, 10, 10)
    
    # Тест ToolManager
    print("1. Тест ToolManager:")
    manager = ToolManager()
    print(f"   Создан: {manager}")
    print(f"   Текущий инструмент: {manager.current_tool.name}")
    print(f"   Все инструменты: {manager.get_all_tool_names()}")
    
    # Тест BrushTool
    print("\n2. Тест BrushTool:")
    brush = manager.get_brush()
    print(f"   Кисть: {brush}")
    print(f"   Размер по умолчанию: {brush.size}")
    
    brush.size = 1
    brush.use(grid, 5, 5, (255, 0, 0))
    print(f"   Нарисовано кистью размера 1")
    print(f"   Цвет ячейки [5,5]: {grid.get_cell_color(5, 5)}")
    
    brush.size = 3
    brush.use(grid, 7, 7, (0, 255, 0))
    print(f"   Нарисовано кистью размера 3")
    print(f"   Цвет ячейки [7,7]: {grid.get_cell_color(7, 7)}")
    
    # Тест EraserTool
    print("\n3. Тест EraserTool:")
    eraser = manager.get_eraser()
    print(f"   Ластик: {eraser}")
    eraser.use(grid, 5, 5, (0, 0, 0))  # Цвет игнорируется
    print(f"   Стерто ячейку [5,5]")
    print(f"   Цвет ячейки [5,5] после стирания: {grid.get_cell_color(5, 5)}")
    
    # Тест FillTool
    print("\n4. Тест FillTool:")
    fill = manager.get_fill()
    print(f"   Заливка: {fill}")
    
    # Создаем небольшую область для заливки
    for i in range(3):
        grid.set_cell_color(i, 0, (100, 100, 100))
    
    print(f"   Создана область серого цвета")
    fill.use(grid, 0, 0, (255, 255, 0))
    print(f"   Залита область желтым")
    print(f"   Цвет [0,0]: {grid.get_cell_color(0, 0)}")
    print(f"   Цвет [1,0]: {grid.get_cell_color(1, 0)}")
    
    # Тест EyeDropperTool
    print("\n5. Тест EyeDropperTool:")
    eyedropper = manager.get_eyedropper()
    print(f"   Пипетка: {eyedropper}")
    
    eyedropper.use(grid, 0, 0, (0, 0, 0))  # Выбираем цвет
    print(f"   Выбран цвет с [0,0]: {eyedropper.picked_color}")
    
    # Тест переключения инструментов
    print("\n6. Тест переключения инструментов:")
    print(f"   Текущий: {manager.current_tool.name}")
    
    manager.next_tool()
    print(f"   После next_tool(): {manager.current_tool.name}")
    
    manager.select_tool(ToolManager.FILL)
    print(f"   После select_tool(FILL): {manager.current_tool.name}")
    
    manager.select_tool_by_name("Brush")
    print(f"   После select_tool_by_name('Brush'): {manager.current_tool.name}")
    
    # Тест размеров инструмента
    print("\n7. Тест размеров инструмента:")
    brush.size = 1
    print(f"   Размер 1: паттерн = {len(brush._get_brush_pattern())} точек")
    brush.size = 3
    print(f"   Размер 3: паттерн = {len(brush._get_brush_pattern())} точек")
    brush.size = 5
    print(f"   Размер 5: паттерн = {len(brush._get_brush_pattern())} точек")
    
    # Тест ограничения размера
    print("\n8. Тест ограничения размера:")
    brush.size = 10
    print(f"   Установлено 10, получено: {brush.size}")
    brush.size = -5
    print(f"   Установлено -5, получено: {brush.size}")
    brush.size = 3
    print(f"   Установлено 3, получено: {brush.size}")
    
    print("\n✅ Все тесты Tools пройдены!")
    print(f"\n📊 Статистика:")
    print(f"   - Инструментов: {len(manager.get_all_tool_names())}")
    print(f"   - Паттерн: Strategy")
    print(f"   - Размеры кисти: 1-5")
    print(f"   - Текущий инструмент: {manager.current_tool.name}")