#функция для чтения файлов с данными и проверки наличия файлов

import pandas as pd

def read_file(filename):
    try:
        df = pd.read_excel(filename)
    except FileNotFoundError:
        print('Файл не найден')
    else:
        return df