# GitHub API Test


## Требования


1. Python >=3.7
2. Установленные библиотеки из файла requirements.txt
3. Токен GitHub с правами repo


## Установка


1. pip install -r requirements.txt
2. Создайте или отредактируйте файл .env, и заполните следующие переменные:
    ```bash
    GITHUB_TOKEN=your_github_token
    GITHUB_USERNAME=your_github_username
    REPO_NAME=test_repo
    ```


## Использование


```bash
python test_api.py
```

## Установка библиотек и запуск с помощью bash/bat скрипта
1. Для Windows запустите run_tests_windows.bat
2. Для Linux запустите start_linux.sh (предварительно установите права доступа +x для этого файла)
