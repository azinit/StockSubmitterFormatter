# StockSubmitterFormatter
Работа для взаимодействия и доп. функционала к программе Stock Submitter

# Алгоритм
## 1. Читаем с файла запросы (построчно)
/.../data.csv

'''
file_1.eps,term_1
or
term_1
'''

## 2. В ключевалку
- вводим
- получаем информацию


* [(file,)term]+= ,
* только запросы иногда файлы
* Сохраняется каждый раз после каждой строки
* Ключевалка -> .exe

""" 
TERM => 
TERM,"kw_1;kw_2;kw_3;...",
или
FILE, TERM =>
FILE.eps,TERM,"kw_1;kw_2;kw_3;...",
"""
