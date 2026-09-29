@echo off
echo.
echo ##############################
echo # Автоматизация кликов в VS Code #
echo ##############################
echo.
echo 1. Установка зависимостей...
python -c "import pyautogui" >nul 2>&1
if errorlevel 1 (
    echo Устанавливаю pyautogui...
    pip install pyautogui
) else (
    echo pyautogui уже установлен
)

echo.
echo 2. Запуск скрипта клика...
echo Убедитесь, что VS Code с кнопкой Run видно на экране
echo.
echo Нажмите любую клавишу для запуска через 5 секунд...
timeout /t 5 >nul

python main_clicker.py

echo.
echo #########################
echo # Завершено #
echo #########################
pause