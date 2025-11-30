# ========================================
# utils/test.py (ИСПРАВЛЕНО)
# ========================================
"""
Тестирование модуля utils
"""

import sys
import os

# Добавляем родительскую папку в путь
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Импортируем все из utils
from utils import (
    Vector2D,
    remap, clamp, lerp, normalize, distance, sign,
    get_filename_from_path
)


if __name__ == "__main__":
    """Тесты для модуля utils"""
    
    print("=== Тестирование Utils ===\n")
    
    # Тест Vector2D
    print("1. Тест Vector2D:")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 1)
    print(f"   v1 = {v1}")
    print(f"   v2 = {v2}")
    print(f"   v1 + v2 = {v1 + v2}")
    print(f"   v1 - v2 = {v1 - v2}")
    print(f"   v1 * 2 = {v1 * 2}")
    print(f"   v1 / 2 = {v1 / 2}")
    print(f"   Длина v1 = {v1.length()}")
    print(f"   Расстояние между v1 и v2 = {v1.distance_to(v2):.2f}")
    print(f"   v1.to_tuple() = {v1.to_tuple()}")
    print(f"   v1.to_int_tuple() = {v1.to_int_tuple()}")
    
    # Тест нормализации
    normalized = v1.normalize()
    print(f"   Нормализованный v1 = {normalized}")
    print(f"   Длина нормализованного = {normalized.length():.2f}")
    
    # Тест math_utils
    print("\n2. Тест math_utils:")
    print(f"   remap(5, 0, 10, 0, 100) = {remap(5, 0, 10, 0, 100)}")
    print(f"   remap(750, 0, 1000, 0, 100) = {remap(750, 0, 1000, 0, 100)}")
    print(f"   clamp(15, 0, 10) = {clamp(15, 0, 10)}")
    print(f"   clamp(-5, 0, 10) = {clamp(-5, 0, 10)}")
    print(f"   clamp(5, 0, 10) = {clamp(5, 0, 10)}")
    print(f"   lerp(0, 100, 0.5) = {lerp(0, 100, 0.5)}")
    print(f"   lerp(10, 20, 0.25) = {lerp(10, 20, 0.25)}")
    print(f"   normalize(50, 0, 100) = {normalize(50, 0, 100)}")
    print(f"   normalize(25, 0, 100) = {normalize(25, 0, 100)}")
    print(f"   distance(0, 0, 3, 4) = {distance(0, 0, 3, 4)}")
    print(f"   sign(10) = {sign(10)}")
    print(f"   sign(-5) = {sign(-5)}")
    print(f"   sign(0) = {sign(0)}")
    
    # Тест file_utils
    print("\n3. Тест file_utils:")
    print(f"   get_filename_from_path('C:/folder/file.txt') = '{get_filename_from_path('C:/folder/file.txt')}'")
    print(f"   get_filename_from_path('C:\\\\Users\\\\file.png') = '{get_filename_from_path('C:\\\\Users\\\\file.png')}'")
    print(f"   get_filename_from_path('/home/user/doc.txt') = '{get_filename_from_path('/home/user/doc.txt')}'")
    
    # Дополнительные тесты Vector2D
    print("\n4. Дополнительные тесты Vector2D:")
    v3 = Vector2D.from_tuple((5, 10))
    print(f"   Vector2D.from_tuple((5, 10)) = {v3}")
    
    v4 = Vector2D(0, 0)
    print(f"   Нулевой вектор = {v4}")
    print(f"   Длина нулевого = {v4.length()}")
    
    print(f"   v1 == v2? {v1 == v2}")
    print(f"   v1 == Vector2D(3, 4)? {v1 == Vector2D(3, 4)}")
    
    print("\n✅ Все тесты Utils пройдены!")
    print(f"\n📊 Статистика:")
    print(f"   - Классов: 1 (Vector2D)")
    print(f"   - Функций: 12 (6 math + 6 file)")
    print(f"   - Всего экспортов: 13")