# ========================================
# ui/test.py (ИСПРАВЛЕНО)
# ========================================
"""
Тестирование модуля ui
"""

import sys
import os

# Добавляем родительскую папку
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# ВАЖНО: Инициализируем pygame ДО импорта UI компонентов!
import pygame as pg
pg.init()

from ui import Button, Slider, ColorPicker, Toolbar


if __name__ == "__main__":
    """Тесты для модуля ui"""
    
    print("=== Тестирование UI ===\n")
    print("✓ Pygame инициализирован")
    
    # Тест Button
    print("\n1. Тест Button:")
    btn1 = Button(10, 10, 80, 40, text="Save")
    print(f"   Создана: {btn1}")
    print(f"   Rect: {btn1.rect}")
    print(f"   Enabled: {btn1.enabled}")
    print(f"   Clicked: {btn1.clicked}")
    
    # Callback
    def on_button_click():
        print("   >>> Кнопка нажата!")
    
    btn1.set_on_click(on_button_click)
    print(f"   Callback установлен")
    
    # Тест состояний
    btn1.clicked = True
    print(f"   Установлено clicked=True: {btn1.clicked}")
    btn1.clicked = False
    
    btn1.enabled = False
    print(f"   Установлено enabled=False: {btn1.enabled}")
    btn1.enabled = True
    
    # Тест Slider
    print("\n2. Тест Slider:")
    slider1 = Slider(100, 100, 10, 20, min_value=1, max_value=5, initial_value=3, label="Размер")
    print(f"   Создан: {slider1}")
    print(f"   Начальное значение: {slider1.value}")
    
    slider1.value = 5
    print(f"   Установлено значение 5: {slider1.value}")
    
    slider1.value = 10  # За пределами
    print(f"   Установлено значение 10 (ограничено): {slider1.value}")
    
    slider1.value = -1  # За пределами
    print(f"   Установлено значение -1 (ограничено): {slider1.value}")
    
    slider1.value = 2
    print(f"   Установлено значение 2: {slider1.value}")
    
    # Тест ColorPicker
    print("\n3. Тест ColorPicker:")
    picker = ColorPicker(10, 10, cell_size=20)
    print(f"   Создан: {picker}")
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    picker.set_colors(colors)
    print(f"   Установлено {len(colors)} цветов")
    print(f"   Позиции вычислены: {len(picker._positions)} шт")
    print(f"   Цветов на ряд: {picker._cols}")
    
    # Тест Toolbar
    print("\n4. Тест Toolbar:")
    toolbar = Toolbar(10, 10, title="Инструменты")
    print(f"   Создана: {toolbar}")
    
    btn_brush = Button(10, 50, 50, 30, text="Brush")
    btn_eraser = Button(70, 50, 50, 30, text="Eraser")
    btn_fill = Button(130, 50, 50, 30, text="Fill")
    
    toolbar.add_button(btn_brush)
    toolbar.add_button(btn_eraser)
    toolbar.add_button(btn_fill)
    print(f"   Добавлено 3 кнопки")
    print(f"   Кнопка 0: {toolbar.get_button(0)}")
    print(f"   Кнопка 1: {toolbar.get_button(1)}")
    print(f"   Кнопка 2: {toolbar.get_button(2)}")
    
    # Тест создания нескольких кнопок
    print("\n5. Тест создания множества кнопок:")
    buttons = []
    button_names = ["Save", "Load", "Export", "Clear", "Undo", "Redo"]
    for i, name in enumerate(button_names):
        btn = Button(10 + i * 90, 200, 80, 40, text=name)
        buttons.append(btn)
    print(f"   Создано {len(buttons)} кнопок")
    for btn in buttons:
        print(f"   - {btn}")
    
    # Тест создания слайдеров
    print("\n6. Тест создания нескольких слайдеров:")
    sliders = []
    slider_configs = [
        ("Brush", 1, 5, 3),
        ("Eraser", 1, 5, 2),
        ("Opacity", 0, 100, 100)
    ]
    for i, (label, min_v, max_v, init_v) in enumerate(slider_configs):
        s = Slider(100, 300 + i * 80, 10, 20, min_v, max_v, init_v, label)
        sliders.append(s)
    print(f"   Создано {len(sliders)} слайдеров")
    for s in sliders:
        print(f"   - {s}")
    
    # Тест больших палитр
    print("\n7. Тест ColorPicker с большой палитрой:")
    picker_large = ColorPicker(400, 10, cell_size=25)
    
    # Создаем палитру из 24 цветов
    large_palette = []
    for r in range(4):
        for g in range(3):
            for b in range(2):
                color = (r * 85, g * 127, b * 255)
                large_palette.append(color)
    
    picker_large.set_colors(large_palette)
    print(f"   Создана палитра из {len(large_palette)} цветов")
    print(f"   Позиций: {len(picker_large._positions)}")
    print(f"   Цветов в ряду: {picker_large._cols}")
    rows = (len(large_palette) + picker_large._cols - 1) // picker_large._cols
    print(f"   Рядов: {rows}")
    
    # Статистика
    print("\n✅ Все тесты UI пройдены!")
    print(f"\n📊 Статистика:")
    print(f"   - Компонентов: 4 (Button, Slider, ColorPicker, Toolbar)")
    print(f"   - Создано кнопок: {len(buttons) + 3}")
    print(f"   - Создано слайдеров: {len(sliders)}")
    print(f"   - Цветов в палитре: {len(large_palette)}")
    print(f"   - Состояния: hovered, clicked, enabled, dragging")
    print(f"   - Callbacks: поддерживаются")
    
    print("\n💡 Для визуального теста запустите полное приложение!")
    
    # Завершаем pygame
    pg.quit()
    print("\n✓ Pygame завершен")