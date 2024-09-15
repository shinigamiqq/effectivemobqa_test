@echo off
REM Установка зависимостей из requirements.txt
echo Установка зависимостей из requirements.txt...
pip install -r requirements.txt

REM Проверяем успешность установки зависимостей
IF %ERRORLEVEL% NEQ 0 (
    echo Ошибка при установке зависимостей.
    exit /b 1
)

REM Запуск тестов с помощью pytest
echo Запуск тестов с pytest...
pytest main.py -v

REM Проверяем успешность выполнения тестов
IF %ERRORLEVEL% NEQ 0 (
    echo Тесты завершились с ошибками.
    exit /b 1
) ELSE (
    echo Тесты успешно пройдены.
)

