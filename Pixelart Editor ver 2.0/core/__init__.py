# ========================================
# core/__init__.py
# ========================================
"""
Ядро приложения для Pixelart Editor

Содержит:
- Config: конфигурация приложения
- Application: главный класс приложения (Singleton)
"""

from .config import Config
from .application import Application

__all__ = [
    'Config',
    'Application',
]

__version__ = '1.0.0'
__author__ = 'Pixelart Editor Team'
__description__ = 'Core application module'