# ========================================
# core/application.py
# ========================================
"""Главный класс приложения"""

import pygame as pg
import sys
from typing import Optional

from models import Grid, PaletteManager
from tools import ToolManager
from controllers import InputController, FileController, CanvasController
from ui import Button, Slider, ColorPicker, Toolbar
from .config import Config


class Application:
    """
    Главный класс приложения - Singleton
    Координирует все компоненты системы
    """
    
    _instance: Optional['Application'] = None
    
    def __new__(cls):
        """Реализация паттерна Singleton"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Инициализация приложения"""
        if hasattr(self, '_initialized'):
            return
        
        self._initialized = True
        
        # Инициализация Pygame
        pg.init()
        
        # Создание окна
        self._screen = pg.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pg.display.set_caption(Config.WINDOW_TITLE)
        
        # Загрузка иконок
        self._load_icons()
        
        # Часы для FPS
        self._clock = pg.time.Clock()
        self._running = False
        
        # Инициализация компонентов
        self._init_components()
    
    def _load_icons(self):
        """Загрузка иконок для инструментов"""
        try:
            # Иконка окна
            icon = pg.image.load("assets/icon.png")
            pg.display.set_icon(icon)
        except:
            pass
        
        # Иконки инструментов
        try:
            self._icon_brush = pg.transform.scale(pg.image.load("assets/brush.png"), (22, 22))
            self._icon_eraser = pg.transform.scale(pg.image.load("assets/eraser.png"), (22, 22))
            self._icon_fill = pg.transform.scale(pg.image.load("assets/fill.png"), (22, 22))
            self._icon_eyedropper = pg.transform.scale(pg.image.load("assets/eyedropper.png"), (22, 22))
            self._has_icons = True
        except:
            print("⚠️  Иконки не найдены в папке assets/")
            print("   Создайте папку assets/ и поместите туда:")
            print("   - icon.png, brush.png, eraser.png, fill.png, eyedropper.png")
            self._has_icons = False
    
    def _init_components(self):
        """Инициализация всех компонентов"""
        # Models
        self._grid = Grid(Config.GRID_WIDTH, Config.GRID_HEIGHT, Config.CELL_SIZE)
        self._palette_manager = PaletteManager()
        
        # Tools
        self._tool_manager = ToolManager()
        
        # Controllers
        self._input_controller = InputController()
        self._file_controller = FileController()
        self._canvas_controller = CanvasController(self._grid, self._tool_manager)
        
        # UI Components
        self._init_ui()
        
        # Устанавливаем начальный цвет
        self._canvas_controller.current_color = self._palette_manager.current_palette.selected_color
    
    def _init_ui(self):
        """Инициализация UI компонентов"""
        # Кнопки сохранения/загрузки
        self._btn_save = Button(20, 790, 80, 40, text="Save")
        self._btn_load = Button(110, 790, 80, 40, text="Load")
        self._btn_export = Button(200, 790, 80, 40, text="Export")
        
        self._btn_save.set_on_click(self._on_save_click)
        self._btn_load.set_on_click(self._on_load_click)
        self._btn_export.set_on_click(self._on_export_click)
        
        # Кнопки инструментов
        self._btn_brush = Button(825, 60, 30, 30, (80, 80, 80))
        self._btn_eraser = Button(875, 60, 30, 30, (80, 80, 80))
        self._btn_fill = Button(825, 110, 30, 30, (80, 80, 80))
        self._btn_eyedropper = Button(875, 110, 30, 30, (80, 80, 80))
        
        self._btn_brush.clicked = True  # Кисть выбрана по умолчанию
        
        self._btn_brush.set_on_click(lambda: self._select_tool(0))
        self._btn_eraser.set_on_click(lambda: self._select_tool(1))
        self._btn_fill.set_on_click(lambda: self._select_tool(2))
        self._btn_eyedropper.set_on_click(lambda: self._select_tool(3))
        
        self._tool_buttons = [self._btn_brush, self._btn_eraser, self._btn_fill, self._btn_eyedropper]
        
        # Слайдеры размера (сдвинуты правее)
        # Боковая панель: 768-960 (ширина 192px)
        # Центр слайдера: 875, трек 120px → начало 815, конец 935
        self._slider_brush = Slider(875, 305, 10, 20, 1, 5, 3, "Размер кисти")
        self._slider_eraser = Slider(875, 225, 10, 20, 1, 5, 3, "Размер ластика")
        
        # Палитра цветов
        self._color_picker = ColorPicker(784, 405, cell_size=20)
        self._color_picker.set_colors(self._palette_manager.current_palette.colors)
        
        # Шрифты
        self._font = pg.font.SysFont(None, 30)
        self._small_font = pg.font.SysFont(None, 25)
    
    def _select_tool(self, tool_index: int):
        """Выбрать инструмент"""
        self._tool_manager.select_tool(tool_index)
        
        # Обновляем состояние кнопок
        for i, btn in enumerate(self._tool_buttons):
            btn.clicked = (i == tool_index)
    
    def _on_save_click(self):
        """Обработка клика по кнопке Save"""
        self._file_controller.save_project(self._grid)
    
    def _on_load_click(self):
        """Обработка клика по кнопке Load"""
        self._file_controller.load_project(self._grid)
    
    def _on_export_click(self):
        """Обработка клика по кнопке Export"""
        region = (4, 4, Config.GRID_WIDTH * Config.CELL_SIZE, Config.GRID_HEIGHT * Config.CELL_SIZE)
        self._file_controller.export_image(self._screen, region)
    
    def _handle_events(self):
        """Обработка событий"""
        events = pg.event.get()
        
        for event in events:
            if event.type == pg.QUIT:
                self._running = False
            
            elif event.type == pg.KEYDOWN:
                self._handle_keydown(event)
        
        # Обновляем контроллер ввода
        self._input_controller.update(events)
    
    def _handle_keydown(self, event):
        """Обработка нажатий клавиш"""
        # Ctrl+S - Сохранить
        if event.key == pg.K_s and pg.key.get_mods() & pg.KMOD_CTRL:
            self._file_controller.quick_save(self._grid)
        
        # Ctrl+Z - Отменить
        elif event.key == pg.K_z and pg.key.get_mods() & pg.KMOD_CTRL:
            self._canvas_controller.undo()
        
        # Ctrl+Y - Повторить
        elif event.key == pg.K_y and pg.key.get_mods() & pg.KMOD_CTRL:
            self._canvas_controller.redo()
        
        # Ctrl+Space - Очистить
        elif event.key == pg.K_SPACE and pg.key.get_mods() & pg.KMOD_CTRL:
            self._canvas_controller.clear_canvas()
        
        # Клавиши быстрого выбора инструментов
        elif event.key == pg.K_b:
            self._select_tool(0)  # Brush
        elif event.key == pg.K_e:
            self._select_tool(1)  # Eraser
        elif event.key == pg.K_g:
            self._select_tool(2)  # Fill
        elif event.key == pg.K_i:
            self._select_tool(3)  # Eyedropper
    
    def _update(self):
        """Обновление логики"""
        mouse_pos = self._input_controller.mouse_pos
        mouse_pressed = self._input_controller.left_mouse_pressed
        mouse_clicked = self._input_controller.left_mouse_clicked
        
        # Обновляем UI компоненты
        self._btn_save.update(mouse_pos, mouse_clicked)
        self._btn_load.update(mouse_pos, mouse_clicked)
        self._btn_export.update(mouse_pos, mouse_clicked)
        
        for btn in self._tool_buttons:
            btn.update(mouse_pos, mouse_clicked)
        
        self._slider_brush.update(mouse_pos, mouse_pressed)
        self._slider_eraser.update(mouse_pos, mouse_pressed)
        
        # Обновляем размеры инструментов
        self._tool_manager.get_brush().size = self._slider_brush.value
        self._tool_manager.get_eraser().size = self._slider_eraser.value
        
        # Выбор цвета из палитры
        selected_color = self._color_picker.update(mouse_pos, mouse_clicked)
        if selected_color:
            self._canvas_controller.current_color = selected_color
        
        # Рисование на холсте
        if mouse_pos[0] < Config.GRID_WIDTH * Config.CELL_SIZE and \
           mouse_pos[1] < Config.GRID_HEIGHT * Config.CELL_SIZE:
            
            grid_x, grid_y = self._input_controller.pixel_to_grid(
                mouse_pos[0], mouse_pos[1], Config.CELL_SIZE
            )
            
            if mouse_pressed:
                if not self._canvas_controller._is_drawing:
                    self._canvas_controller.start_drawing()
                
                # Сохраняем старый цвет
                old_color = self._canvas_controller.current_color
                
                # Рисуем
                self._canvas_controller.draw_at(grid_x, grid_y)
                
                # Если цвет изменился (пипетка) - обновляем индикатор
                if self._canvas_controller.current_color != old_color:
                    self._color_picker.set_selected_color(self._canvas_controller.current_color)
                    
            else:
                if self._canvas_controller._is_drawing:
                    self._canvas_controller.stop_drawing()
    
    def _render(self):
        """Отрисовка"""
        # Очищаем экран
        self._screen.fill(Config.BG_COLOR)
        
        # Отрисовка сетки
        self._grid.render(self._screen)
        
        # Отрисовка стен/границ
        self._draw_walls()
        
        # Отрисовка UI
        self._render_ui()
        
        # Обновляем дисплей
        pg.display.flip()
    
    def _draw_walls(self):
        """Отрисовка границ областей"""
        grid_pixel_width = Config.GRID_WIDTH * Config.CELL_SIZE
        grid_pixel_height = Config.GRID_HEIGHT * Config.CELL_SIZE
        
        # Боковая панель
        pg.draw.rect(self._screen, Config.SIDEBAR_COLOR, 
                    (grid_pixel_width, 0, Config.SCREEN_WIDTH - grid_pixel_width, grid_pixel_height))
        
        # Нижняя панель
        pg.draw.rect(self._screen, Config.BOTTOM_BAR_COLOR,
                    (0, grid_pixel_height, Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT - grid_pixel_height))
        
        # Границы
        wall_thickness = 4
        pg.draw.rect(self._screen, Config.WALL_COLOR,
                    (grid_pixel_width, 0, wall_thickness, grid_pixel_height))
        pg.draw.rect(self._screen, Config.WALL_COLOR,
                    (0, grid_pixel_height - wall_thickness, Config.SCREEN_WIDTH, wall_thickness))
    
    def _render_ui(self):
        """Отрисовка UI элементов"""
        # Кнопки файлов
        self._btn_save.render(self._screen)
        self._btn_load.render(self._screen)
        self._btn_export.render(self._screen)
        
        # Заголовок инструментов
        tools_title = self._small_font.render("Инструменты", True, (50, 50, 50))
        self._screen.blit(tools_title, (779, 30))
        
        # Фон панели инструментов
        pg.draw.rect(self._screen, (180, 180, 180), (779, 50, 170, 100))
        
        # Кнопки инструментов
        for btn in self._tool_buttons:
            btn.render(self._screen)
        
        # ИКОНКИ на кнопках инструментов
        if self._has_icons:
            self._screen.blit(self._icon_brush, (self._btn_brush._x + 4, self._btn_brush._y + 4))
            self._screen.blit(self._icon_eraser, (self._btn_eraser._x + 4, self._btn_eraser._y + 4))
            self._screen.blit(self._icon_fill, (self._btn_fill._x + 4, self._btn_fill._y + 4))
            self._screen.blit(self._icon_eyedropper, (self._btn_eyedropper._x + 4, self._btn_eyedropper._y + 4))
        
        # Заголовок настроек размера
        size_title = self._small_font.render("Настройки размера", True, (50, 50, 50))
        self._screen.blit(size_title, (779, 170))
        
        # Слайдеры
        self._slider_brush.render(self._screen)
        self._slider_eraser.render(self._screen)
        
        # Заголовок палитры
        palette_title = self._small_font.render("Палитра", True, (50, 50, 50))
        self._screen.blit(palette_title, (779, 380))
        
        # Фон палитры
        pg.draw.rect(self._screen, (200, 200, 200), (779, 400, 170, 350))
        
        # Палитра (передаем текущий цвет для индикатора)
        self._color_picker.render(self._screen, self._canvas_controller.current_color)
        
        # Фон для имени файла (БЕЛЫЙ)
        pg.draw.rect(self._screen, (255, 255, 255), (310, 790, 370, 40))
        
        # Имя файла
        filename = self._file_controller.current_filename or "unnamed"
        filename_surface = self._font.render(filename, True, (0, 0, 0))
        self._screen.blit(filename_surface, (320, Config.SCREEN_HEIGHT - 50))
    
    def run(self):
        """Главный цикл приложения"""
        self._running = True
        
        print("=== Pixelart Editor запущен ===")
        print(f"Размер сетки: {Config.GRID_WIDTH}x{Config.GRID_HEIGHT}")
        print(f"Размер ячейки: {Config.CELL_SIZE}px")
        print("\nГорячие клавиши:")
        print("  B - Кисть, E - Ластик, G - Заливка, I - Пипетка")
        print("  Ctrl+S - Сохранить, Ctrl+Z - Отменить")
        print("="*35)
        
        while self._running:
            self._handle_events()
            self._update()
            self._render()
            self._clock.tick(Config.FPS)
        
        self._quit()
    
    def _quit(self):
        """Завершение работы"""
        print("\n=== Завершение работы ===")
        pg.quit()
        sys.exit()