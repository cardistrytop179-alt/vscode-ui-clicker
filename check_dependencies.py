# -*- coding: utf-8 -*-
"""
Скрипт для проверки и установки необходимых зависимостей
"""

import subprocess
import sys
import importlib

def check_and_install_package(package_name):
    """Проверка и установка пакета"""
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} уже установлен")
        return True
    except ImportError:
        print(f"📦 {package_name} не найден, начинаем установку...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"✅ {package_name} успешно установлен")
            return True
        except subprocess.CalledProcessError:
            print(f"❌ Ошибка при установке {package_name}")
            return False

def main():
    print("🔍 Проверка необходимых зависимостей...")
    
    packages = ["pyautogui", "cv2", "numpy"]
    installed_count = 0
    
    for package in packages:
        if check_and_install_package(package):
            installed_count += 1
    
    print(f"\n📊 Результат: {installed_count}/{len(packages)} пакетов установлено")
    
    if installed_count == len(packages):
        print("🎉 Все зависимости установлены успешно!")
        print("\nТеперь вы можете запустить скрипт клика:")
        print("python simple_clicker.py")
    else:
        print("⚠️  Не все зависимости удалось установить")
        print("Попробуйте установить вручную командой:")
        print("pip install pyautogui opencv-python pillow")

if __name__ == "__main__":
    main()