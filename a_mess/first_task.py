"""Посмотрите видео по работе с файлами https://www.youtube.com/watch?v=oRr_bEXJbV0"""
import inline
import matplotlib

# Посмотрел - все понял

"""Откройте и прочитайте данные с файла lorum.txt, способом, который рассматривается в видео из пункта 1."""

# file = open('PY-241/lorum.txt', encoding="utf-8")
# print(file.read())
# file.close()

"""Прочитать про разницу между модами, при открытии файла
https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function"""
# Прочел - все понял

"""Попробуйте открыть файлы с разными значениями mode для чтения."""
#
with open('PY-241/lorum.txt', 'a+', encoding='utf-8') as fl:
    # fl.write('Скажи мне , и я скажу тебе. Чем проще, тем проще. Если надо объяснять, то не надо объяснять\n')
    fl.seek(0)
    print(fl.read())

with open('PY-241/lorum.txt', 'w+', encoding='utf-8') as fl:
    fl.write('Скажи мне , и я скажу тебе. Чем проще, тем проще. Если надо объяснять, то не надо объяснять\n')
    fl.seek(0)
    print(fl.read())

with open('PY-241/lorum.txt', 'r+', encoding='utf-8') as fl:
    print(fl.read())
    fl.write('Скажи мне , и я скажу тебе. Чем проще, тем проще. Если надо объяснять, то не надо объяснять\n')
    fl.seek(0)
    print(fl.read())

with open('PY-241/lorum.txt', 'r', encoding='utf-8') as fl:
    print(fl.read())


"""Запишите любую информацию в файл с разными значениями mode для записи. 
Какую разницу при записи файла вы заметили?"""

with open('PY-241/lorum.txt', 'a+', encoding='utf-8') as fl:
    # fl.write('Скажи мне , и я скажу тебе. Чем проще, тем проще. Если надо объяснять, то не надо объяснять\n')
    fl.seek(0)
    print(fl.read())

with open('PY-241/lorum.txt', 'w+', encoding='utf-8') as fl:
    fl.write('Скажи мне , и я скажу тебе. Чем проще, тем проще. Если надо объяснять, то не надо объяснять\n')
    fl.seek(0)
    print(fl.read())

with open('PY-241/lorum.txt', 'r+', encoding='utf-8') as fl:
    print(fl.read())
    fl.write('Скажи мне , и я скажу тебе. Чем проще, тем проще. Если надо объяснять, то не надо объяснять\n')
    fl.seek(0)
    print(fl.read())




"""Посмотрите видео про контекстный менеджер и повторите все действия из видео с файлом из пункта 2 
https://www.youtube.com/watch?v=ycVlsU_c4Mg"""

import os

with os.scandir(".") as os_fl:
    for i in os_fl:
        print(i.name, ':', i.stat().st_size, 'bytes')

print()
with os.scandir("./PY-241") as os_fl:
    for i in os_fl:
        print(i.name, ':', i.stat().st_size, 'bytes')



"""Прочитайте статью и выполните действия, которые там указаны с файлом bikes.csv
https://webtort.ru/чтение-csv-файла-в-python-при-помощи-pandas/"""

import pandas as pd
import pathlib
from pathlib import Path

# путь в рабочую дерикторию
worki_path = pathlib.Path.cwd()
# путь к файлу
data_path = Path(worki_path, 'PY-241', 'bikes.csv')

# # header - название столбцов (по умолчанию на 0 строкке)
# data = pd.read_csv(data_path, header=0)

# nrow выводит определенное количество строк
data = pd.read_csv(data_path, nrows=5)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

print(data)


"""Посчитайте сумму столбца Rachel1 из файла bikes.csv"""

import pandas as pd
import pathlib
from pathlib import Path

worki_path = pathlib.Path.cwd()
data_path = Path(worki_path, 'PY-241', 'bikes.csv')
data = pd.read_csv(data_path)

summ_df = data['Rachel1'].sum() # +в том что NaN обходит стороной


print(summ_df)
print(data)


import csv

with open('PY-241/bikes.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

header = rows[0]
index_of_Rachel1 = header.index('Rachel1')

sum_of_Rachel1 = 0
for row in rows[1:]:
    sum_of_Rachel1 += float(row[index_of_Rachel1])

print(sum_of_Rachel1)



"""Прочитайте семь первых статей по работе с pandas и выполните из них все действия
https://pythonworld.ru/obrabotka-dannyx/pandas-cookbook-1-csv-reading.html
Это ссылка на первую статью, перейти на последующие можно с помощью кнопки Следующая часть в конце страницы."""

