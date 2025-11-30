# ========================================
# models/palette.py (ИСПРАВЛЕНО - добавлен заголовок)
# ========================================
"""
# ========================================
# models/palette.py
# ========================================
Модуль цветовых палитр
"""

from typing import List, Tuple, Optional


class Palette:
    """
    Цветовая палитра - коллекция цветов
    Поддерживает различные схемы и категории
    """
    
    def __init__(self, name: str, colors: List[Tuple[int, int, int]]):
        """
        Инициализация палитры
        
        Args:
            name: название палитры
            colors: список цветов в формате (R, G, B)
        """
        self._name = name
        self._colors = colors.copy()
        self._selected_index = 0
    
    @property
    def name(self) -> str:
        """Название палитры"""
        return self._name
    
    @property
    def colors(self) -> List[Tuple[int, int, int]]:
        """Список всех цветов"""
        return self._colors.copy()
    
    @property
    def count(self) -> int:
        """Количество цветов в палитре"""
        return len(self._colors)
    
    @property
    def selected_color(self) -> Tuple[int, int, int]:
        """Текущий выбранный цвет"""
        return self._colors[self._selected_index]
    
    @property
    def selected_index(self) -> int:
        """Индекс выбранного цвета"""
        return self._selected_index
    
    def get_color(self, index: int) -> Optional[Tuple[int, int, int]]:
        """
        Получить цвет по индексу
        
        Args:
            index: индекс цвета
        
        Returns:
            Цвет или None если индекс невалиден
        """
        if 0 <= index < len(self._colors):
            return self._colors[index]
        return None
    
    def select_color(self, index: int) -> bool:
        """
        Выбрать цвет по индексу
        
        Args:
            index: индекс цвета
        
        Returns:
            True если успешно, False если индекс невалиден
        """
        if 0 <= index < len(self._colors):
            self._selected_index = index
            return True
        return False
    
    def add_color(self, color: Tuple[int, int, int]):
        """Добавить новый цвет в палитру"""
        if color not in self._colors:
            self._colors.append(color)
    
    def remove_color(self, index: int) -> bool:
        """
        Удалить цвет по индексу
        
        Args:
            index: индекс цвета
        
        Returns:
            True если успешно удален
        """
        if 0 <= index < len(self._colors) and len(self._colors) > 1:
            self._colors.pop(index)
            if self._selected_index >= len(self._colors):
                self._selected_index = len(self._colors) - 1
            return True
        return False
    
    def find_color_index(self, color: Tuple[int, int, int]) -> int:
        """
        Найти индекс цвета в палитре
        
        Args:
            color: цвет для поиска
        
        Returns:
            Индекс цвета или -1 если не найден
        """
        try:
            return self._colors.index(color)
        except ValueError:
            return -1
    
    def __repr__(self) -> str:
        return f"Palette('{self._name}', colors={self.count})"


class PaletteManager:
    """
    Менеджер палитр - управляет несколькими палитрами
    Реализует паттерн Strategy для переключения между палитрами
    """
    
    BASIC_PALETTE = [
        [0, 0, 0], [24, 24, 24], [48, 48, 48], [64, 64, 64],
        [128, 128, 128], [155, 155, 155], [200, 200, 200], [255, 255, 255],
        [27, 38, 49], [40, 55, 71], [46, 64, 83], [52, 73, 94],
        [93, 109, 126], [133, 146, 158], [174, 182, 191], [214, 219, 223],
        [77, 86, 86], [95, 106, 106], [113, 125, 126], [149, 165, 166],
        [170, 183, 184], [191, 201, 202], [213, 219, 219], [229, 232, 232],
        [98, 101, 103], [121, 125, 127], [144, 148, 151], [189, 195, 199],
        [202, 207, 210], [229, 231, 233], [248, 249, 249], [255, 255, 255],
        [100, 30, 22], [123, 36, 28], [146, 43, 33], [192, 57, 43],
        [205, 97, 85], [217, 136, 128], [230, 176, 170], [242, 215, 213],
        [120, 40, 31], [148, 49, 38], [176, 58, 46], [220, 76, 60],
        [236, 112, 99], [241, 148, 138], [245, 183, 177], [250, 219, 216],
        [74, 35, 90], [91, 44, 111], [108, 52, 131], [142, 68, 173],
        [165, 105, 189], [187, 143, 206], [210, 180, 222], [232, 218, 239],
        [21, 67, 96], [26, 82, 118], [31, 97, 141], [41, 128, 185],
        [84, 153, 199], [127, 179, 213], [169, 204, 227], [212, 230, 241],
        [20, 90, 50], [25, 111, 61], [34, 141, 84], [34, 174, 96],
        [82, 190, 128], [125, 206, 160], [169, 223, 191], [212, 239, 223],
        [125, 102, 8], [154, 125, 10], [183, 149, 11], [230, 196, 15],
        [244, 208, 63], [247, 220, 111], [249, 231, 159], [252, 243, 207],
        [126, 81, 9], [156, 100, 12], [185, 119, 14], [242, 156, 18],
        [245, 176, 65], [248, 196, 113], [250, 215, 160], [253, 235, 208],
        [110, 44, 0], [135, 54, 0], [160, 64, 0], [211, 84, 0],
        [220, 118, 51], [229, 152, 102], [237, 187, 153], [246, 221, 204]
    ]
    
    THEMED_PALETTE = [
        [241, 157, 154], [241, 179, 164], [246, 209, 190],
        [252, 225, 213], [242, 193, 173], [241, 175, 153],
        [128, 232, 221], [124, 194, 246], [175, 129, 228],
        [231, 132, 186], [249, 193, 160], [183, 246, 175],
        [100, 93, 62], [130, 123, 92], [156, 151, 115],
        [86, 113, 80], [46, 71, 43], [16, 42, 10],
        [252, 120, 150], [193, 107, 188], [152, 89, 197],
        [108, 66, 196], [85, 56, 193], [30, 171, 215],
        [92, 58, 42], [121, 84, 63], [172, 138, 104],
        [200, 173, 139], [223, 213, 191], [206, 159, 85]
    ]
    
    def __init__(self):
        """Инициализация менеджера палитр"""
        self._palettes: List[Palette] = []
        self._current_palette_index = 0
        self._initialize_default_palettes()
    
    def _initialize_default_palettes(self):
        """Инициализация стандартных палитр"""
        basic_colors = [tuple(c) for c in self.BASIC_PALETTE]
        themed_colors = [tuple(c) for c in self.THEMED_PALETTE]
        
        self._palettes.append(Palette("Облик", basic_colors))
        self._palettes.append(Palette("Мягкие оттенки", themed_colors))
    
    @property
    def current_palette(self) -> Palette:
        """Текущая активная палитра"""
        return self._palettes[self._current_palette_index]
    
    @property
    def palette_count(self) -> int:
        """Количество доступных палитр"""
        return len(self._palettes)
    
    def get_palette(self, index: int) -> Optional[Palette]:
        """Получить палитру по индексу"""
        if 0 <= index < len(self._palettes):
            return self._palettes[index]
        return None
    
    def get_palette_by_name(self, name: str) -> Optional[Palette]:
        """Получить палитру по имени"""
        for palette in self._palettes:
            if palette.name == name:
                return palette
        return None
    
    def switch_palette(self, index: int) -> bool:
        """Переключить текущую палитру"""
        if 0 <= index < len(self._palettes):
            self._current_palette_index = index
            return True
        return False
    
    def next_palette(self):
        """Переключить на следующую палитру"""
        self._current_palette_index = (self._current_palette_index + 1) % len(self._palettes)
    
    def previous_palette(self):
        """Переключить на предыдущую палитру"""
        self._current_palette_index = (self._current_palette_index - 1) % len(self._palettes)
    
    def add_palette(self, palette: Palette):
        """Добавить новую палитру"""
        self._palettes.append(palette)
    
    def remove_palette(self, index: int) -> bool:
        """Удалить палитру"""
        if 0 <= index < len(self._palettes) and len(self._palettes) > 1:
            self._palettes.pop(index)
            if self._current_palette_index >= len(self._palettes):
                self._current_palette_index = len(self._palettes) - 1
            return True
        return False
    
    def get_all_palette_names(self) -> List[str]:
        """Получить список имен всех палитр"""
        return [p.name for p in self._palettes]
    
    def __repr__(self) -> str:
        return f"PaletteManager(palettes={self.palette_count}, current='{self.current_palette.name}')"
