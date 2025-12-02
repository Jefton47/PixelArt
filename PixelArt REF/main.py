#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pixelart Editor - ООП Рефакторинг
Курсовая работа: Рефакторинг процедурного подхода к ООП
Автор: Чернов Евгений
Версия: 1.0.0
"""

import sys
import os

# Добавляем текущую директорию в путь (на всякий случай)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import Application, Config


def print_banner():
    """Вывести баннер приложения"""
    print("=" * 60)
    print("         PIXELART EDITOR - ООП РЕФАКТОРИНГ")
    print("=" * 60)
    print(f"Размер сетки: {Config.GRID_WIDTH}x{Config.GRID_HEIGHT}")
    print(f"Размер окна: {Config.SCREEN_WIDTH}x{Config.SCREEN_HEIGHT}")
    print(f"FPS: {Config.FPS}")
    print("=" * 60)
    print()

def check_dependencies():
    """Проверить наличие необходимых зависимостей"""
    print("Проверка зависимостей...")
    
    try:
        import pygame
        print(f"✓ Pygame {pygame.version.ver} установлен")
    except ImportError:
        print("✗ Pygame не установлен!")
        print("  Установите: pip install pygame")
        return False
    
    # Проверка модулей проекта
    modules = ['models', 'utils', 'tools', 'ui', 'controllers', 'core']
    for module in modules:
        try:
            __import__(module)
            print(f"✓ Модуль {module} найден")
        except ImportError as e:
            print(f"✗ Модуль {module} не найден!")
            print(f"  Ошибка: {e}")
            return False
    
    print("✓ Все зависимости на месте!\n")
    return True


def main():
    """Главная функция запуска приложения"""
    
    # Баннер
    print_banner()
    
    # Проверка зависимостей
    if not check_dependencies():
        print("\n❌ Невозможно запустить приложение - отсутствуют зависимости")
        sys.exit(1)
    
    # Запуск приложения
    try:
        print("🚀 Запуск приложения...")
        print("   Нажмите Ctrl+C для выхода\n")
        
        app = Application()
        app.run()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем (Ctrl+C)")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

    