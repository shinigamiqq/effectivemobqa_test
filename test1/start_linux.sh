#!/bin/bash

echo "Установка зависимостей из requirements.txt..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Ошибка при установке зависимостей."
    exit 1
fi

echo "Запуск тестов с pytest..."
pytest main.py -v

if [ $? -ne 0 ]; then
    echo "Тесты завершились с ошибками."
    exit 1
else
    echo "Тесты успешно пройдены."
fi

