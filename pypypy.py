import requests
import random
from pathlib import Path
import pytest
import os

def getCat() -> (requests.models.Request, str):
    folder_path = Path(__file__).resolve().parent

    URL = "https://cataas.com/cat/gif"

    r = requests.get(URL)


    file_name = folder_path / f"catS_{random.randint(0, 10**6)}.gif"

    with open(file_name, "wb") as f:
        f.write(r.content)


    return r, file_name

def test_getCat_request():
    r, file_name = getCat()
    assert r.status_code == 200,"Помилка завантаження"
    assert len(r.content) > 0, "Пустий файл"
    os.remove(file_name)

def test_getCat_file():
    r, file_name = getCat()
    assert os.path.exists(file_name), 'Не зберигся файл'
    os.remove(file_name)