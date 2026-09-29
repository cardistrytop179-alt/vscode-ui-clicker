# -*- coding: utf-8 -*-
"""
Упрощенный скрипт для клика по кнопке Run в VS Code
"""

try:
    import pyautogui
    import time
    import os
    
    def simple_click_run():
        print("🔍 Проверка наличия pyautogui...")
        print("✅ pyautogui успешно импортирован")
        
        # Проверяем наличие файла run.png
        if not os.path.exists('run.png'):
            print("❌ Файл 'run.png' не найден в текущей директории")
            print("📁 Текущая директория:", os.getcwd())
            print("⚠️  Пожалуйста, убедитесь, что файл 'run.png' находится в этой папке")
            return False
        
        print("🎯 Файл 'run.png' найден")
        print("🖱️  Текущая позиция мыши:", pyautogui.position())
        print("🖥️  Размер экрана:", pyautogui.size())
        
        print("\n⏳ Через 3 секунды начнется поиск кнопки Run...")
        print("⚠️  Переместите мышь в верхний левый угол экрана для отмены")
        
        time.sleep(3)
        
        # Устанавливаем безопасный режим PyAutoGUI
        pyautogui.FAILSAFE = True
        
        try:
            print("🔍 Ищем кнопку Run на экране...")
            
            # Ищем изображение на экране
            button_location = pyautogui.locateOnScreen('run.png', confidence=0.7)
            
            if button_location:
                # Получаем центральную точку кнопки
                center_x = button_location.left + button_location.width // 2
                center_y = button_location.top + button_location.height // 2
                
                print(f"🎯 Найдена кнопка Run! Координаты: ({center_x}, {center_y})")
                
                # Клик по центру кнопки
                pyautogui.click(center_x, center_y)
                print("✅ Клик по кнопке Run выполнен успешно!")
                
                return True
            else:
                print("❌ Кнопка Run не найдена на экране")
                print("💡 Возможно, кнопка не видна на текущем экране или изображение не совпадает")
                return False
        
        except Exception as e:
            print(f"❌ Произошла ошибка при поиске кнопки: {e}")
            print("💡 Это может быть связано с тем, что pyautogui не может найти кнопку")
            return False
        
    def main():
        print("🤖 Простой скрипт клика по кнопке Run")
        print("=" * 40)
        
        success = simple_click_run()

        if success:
            print("\n🎉 Задача выполнена успешно!")
        else:
            print("\n⚠️  Задача не выполнена.")
            print("Проверьте наличие файла 'run.png' и видимость кнопки Run на экране.")

except ImportError:
    print("❌ Библиотека pyautogui не установлена")
    print("💡 Установите pyautogui командой: pip install pyautogui")
    print("💡 Или попробуйте установить через: pip install --upgrade pyautogui")
    
    def main():
        pass