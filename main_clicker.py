# -*- coding: utf-8 -*-
"""
Основной скрипт для клика по кнопке Run в VS Code
Использует файл run.PNG для поиска кнопки
"""

try:
    import pyautogui
    import time
    import os
    
    def click_run_button():
        print("🤖 Скрипт автоматического клика по кнопке Run запущен")
        print("=" * 50)
        
        # Проверяем наличие файла run.PNG
        if not os.path.exists('run.PNG'):
            print("❌ Файл 'run.PNG' не найден в текущей директории")
            print("📁 Текущая директория:", os.getcwd())
            print("⚠️  Пожалуйста, убедитесь, что файл 'run.PNG' находится в этой папке")
            return False
        
        print("🎯 Файл 'run.PNG' найден")
        print("🖱️  Текущая позиция мыши:", pyautogui.position())
        print("🖥️  Размер экрана:", pyautogui.size())
        
        print("\n⏳ Через 3 секунды начнется поиск кнопки Run...")
        print("⚠️  Переместите мышь в верхний левый угол экрана для отмены")
        
        time.sleep(3)
        
        # Устанавливаем безопасный режим PyAutoGUI
        pyautogui.FAILSAFE = True
        
        try:
            print("🔍 Ищем кнопку Run на экране...")
            
            # Ищем изображение на экране с использованием вашего файла
            button_location = pyautogui.locateOnScreen('run.PNG', confidence=0.7)
            
            if button_location:
                # Получаем центральную точку кнопки
                center_x = button_location.left + button_location.width // 2
                center_y = button_location.top + button_location.height // 2
                
                print(f"🎯 Найдена кнопка Run! Координаты: ({center_x}, {center_y})")
                
                # Плавное перемещение к кнопке
                pyautogui.moveTo(center_x, center_y, duration=0.2)
                time.sleep(0.1)
                
                # Клик по центру кнопки
                pyautogui.click()
                print("✅ Клик по кнопке Run выполнен успешно!")
                
                return True
            else:
                print("❌ Кнопка Run не найдена на экране")
                print("💡 Возможно, кнопка не видна на текущем экране или изображение не совпадает")
                
                # Попробуем найти accept_all.PNG как альтернативу
                if os.path.exists('accept_all.PNG'):
                    print("🔍 Проверяем наличие кнопки Accept All...")
                    try:
                        accept_location = pyautogui.locateOnScreen('accept_all.PNG', confidence=0.7)
                        if accept_location:
                            center_x = accept_location.left + accept_location.width // 2
                            center_y = accept_location.top + accept_location.height // 2
                            
                            print(f"🎯 Найдена кнопка Accept All! Координаты: ({center_x}, {center_y})")
                            
                            # Плавное перемещение к кнопке
                            pyautogui.moveTo(center_x, center_y, duration=0.2)
                            time.sleep(0.1)
                            
                            # Клик по центру кнопки
                            pyautogui.click()
                            print("✅ Клик по кнопке Accept All выполнен успешно!")
                            
                            return True
                    except:
                        pass
                        
                return False
        
        except Exception as e:
            print(f"❌ Произошла ошибка при поиске кнопки: {e}")
            print("💡 Это может быть связано с тем, что pyautogui не может найти кнопку")
            return False
        
    def main():
        success = click_run_button()

        if success:
            print("\n🎉 Задача выполнена успешно!")
        else:
            print("\n⚠️  Задача не выполнена.")
            print("Проверьте:")
            print("1. Наличие файла 'run.PNG' или 'accept_all.PNG' в папке")
            print("2. Видимость соответствующей кнопки на экране")
            print("3. Совпадение изображения кнопки с файлом-шаблоном")

except ImportError:
    print("❌ Библиотека pyautogui не установлена")
    print("💡 Установите pyautogui командой: pip install pyautogui")
    
    def main():
        pass

if __name__ == "__main__":
    main()