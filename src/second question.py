import json

def open_json():
    with open('products.json', encoding='utf-8') as data_file:
        data = json.load(data_file)
        return data

"""Не открывает фаил из папки как только не пытался его открыть
Error running 'second question' 
Cannot run program "Z:\projects\new\pytest_proj\.venv\Scripts\python.exe" (in directory "Z:\projects\new\13.1\src"): CreateProcess error=2, Не удается найти указанный файл"""

