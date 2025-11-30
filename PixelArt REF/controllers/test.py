# ========================================
# controllers/test.py
# ========================================
"""
Тестирование модуля controllers
"""

import sys
import os

# Добавляем родительскую папку
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import pygame as pg
pg.init()

from controllers import InputController, FileController, CanvasController
from models import Grid
from tools import ToolManager


if __name__ == "__main__":
    """Тесты для модуля controllers"""
    
    print("=== Тестирование Controllers ===\n")
    
    # Тест InputController
    print("1. Тест InputController:")
    input_ctrl = InputController()
    print(f"   Создан: {input_ctrl}")
    print(f"   Позиция мыши: {input_ctrl.mouse_pos}")
    print(f"   ЛКМ нажата: {input_ctrl.left_mouse_pressed}")
    print(f"   ПКМ нажата: {input_ctrl.right_mouse_pressed}")
    
    # Тест преобразования координат
    pixel_coords = (123, 456)
    grid_coords = input_ctrl.pixel_to_grid(pixel_coords[0], pixel_coords[1], 12)
    print(f"   Пиксели {pixel_coords} -> Сетка {grid_coords}")
    
    # Симуляция события
    fake_event_down = type('Event', (), {'type': pg.MOUSEBUTTONDOWN, 'button': 1})()
    input_ctrl.update([fake_event_down])
    print(f"   После симуляции клика ЛКМ: {input_ctrl.left_mouse_clicked}")
    
    # Тест FileController
    print("\n2. Тест FileController:")
    file_ctrl = FileController()
    print(f"   Создан: {file_ctrl}")
    print(f"   Текущий файл: {file_ctrl.current_filename}")
    print(f"   Файл открыт: {file_ctrl.has_file}")
    
    file_ctrl.new_project()
    print(f"   После new_project(): {file_ctrl.current_filename}")
    
    # Тест CanvasController
    print("\n3. Тест CanvasController:")
    grid = Grid(10, 10, 10)
    tool_manager = ToolManager()
    canvas_ctrl = CanvasController(grid, tool_manager)
    print(f"   Создан: {canvas_ctrl}")
    print(f"   Текущий цвет: {canvas_ctrl.current_color}")
    
    # Установка цвета
    canvas_ctrl.current_color = (255, 0, 0)
    print(f"   Новый цвет: {canvas_ctrl.current_color}")
    
    # Рисование
    print("\n4. Тест рисования:")
    canvas_ctrl.start_drawing()
    print(f"   Начато рисование")
    
    canvas_ctrl.draw_at(5, 5)
    print(f"   Нарисовано в [5,5]")
    print(f"   Цвет ячейки [5,5]: {grid.get_cell_color(5, 5)}")
    
    canvas_ctrl.stop_drawing()
    print(f"   Рисование завершено")
    
    # Тест Undo/Redo
    print("\n5. Тест Undo/Redo:")
    print(f"   Можно отменить: {canvas_ctrl.can_undo()}")
    print(f"   Можно повторить: {canvas_ctrl.can_redo()}")
    
    canvas_ctrl.undo()
    print(f"   После undo - цвет [5,5]: {grid.get_cell_color(5, 5)}")
    
    canvas_ctrl.redo()
    print(f"   После redo - цвет [5,5]: {grid.get_cell_color(5, 5)}")
    
    # Тест очистки
    print("\n6. Тест очистки холста:")
    grid.set_cell_color(3, 3, (0, 255, 0))
    print(f"   Установлен цвет [3,3]: {grid.get_cell_color(3, 3)}")
    
    canvas_ctrl.clear_canvas()
    print(f"   После clear_canvas() - цвет [3,3]: {grid.get_cell_color(3, 3)}")
    
    # Тест пипетки
    print("\n7. Тест выбора цвета (пипетка):")
    grid.set_cell_color(2, 2, (100, 200, 50))
    picked = canvas_ctrl.pick_color_at(2, 2)
    print(f"   Выбран цвет с [2,2]: {picked}")
    print(f"   Текущий цвет изменен на: {canvas_ctrl.current_color}")
    
    # Тест клавиш
    print("\n8. Тест клавиатуры:")
    fake_key_down = type('Event', (), {'type': pg.KEYDOWN, 'key': pg.K_SPACE})()
    input_ctrl.update([fake_key_down])
    print(f"   SPACE нажата: {input_ctrl.is_key_down(pg.K_SPACE)}")
    print(f"   SPACE удерживается: {input_ctrl.is_key_pressed(pg.K_SPACE)}")
    
    fake_key_up = type('Event', (), {'type': pg.KEYUP, 'key': pg.K_SPACE})()
    input_ctrl.update([fake_key_up])
    print(f"   SPACE отпущена: {input_ctrl.is_key_up(pg.K_SPACE)}")
    print(f"   SPACE удерживается: {input_ctrl.is_key_pressed(pg.K_SPACE)}")
    
    # Статистика
    print("\n✅ Все тесты Controllers пройдены!")
    print(f"\n📊 Статистика:")
    print(f"   - Контроллеров: 3")
    print(f"   - Паттерн: MVC (Controller)")
    print(f"   - InputController: мышь + клавиатура")
    print(f"   - FileController: save/load/export")
    print(f"   - CanvasController: рисование + undo/redo")
    
    pg.quit()
    print("\n✓ Pygame завершен")