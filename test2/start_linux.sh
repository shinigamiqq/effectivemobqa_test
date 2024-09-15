#!/bin/bash

echo "Установка зависимостей из requirements.txt..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Ошибка при установке зависимостей."
    exit 1
fi

# 2. Запуск тестов с помощью pytest
echo "Запуск тестов..."
python test_api.py

# Проверяем успешность выполнения тестов
if [ $? -ne 0 ]; then
    echo "Тесты завершились с ошибками."
    exit 1
else
    echo "Тесты успешно пройдены."
fi

