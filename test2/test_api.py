import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = os.getenv("REPO_NAME")

BASE_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_repo():
    """Создание нового репозитория"""
    url = f"{BASE_URL}/user/repos"
    payload = {
        "name": REPO_NAME,
        "description": "test repository",
        "private": False
    }
    response = requests.post(url, json=payload, headers=HEADERS)

    if response.status_code == 201:
        print(f"Repository '{REPO_NAME}' created successfully.")
    else:
        print(f"Failed to create repository: {response.status_code}, {response.json()}")


def check_repo_exists():
    """Проверка, что репозиторий существует"""
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        print(f"Repository '{REPO_NAME}' exists.")
        return True
    else:
        print(f"Repository '{REPO_NAME}' does not exist: {response.status_code}")
        return False


def delete_repo():
    """Удаление репозитория"""
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f"Repository '{REPO_NAME}' deleted successfully.")
    else:
        print(f"Failed to delete repository: {response.status_code}, {response.json()}")


create_repo()
if check_repo_exists():
    delete_repo()


