"""
Створіть словник, що описує учнів у класі. Словник повинен містити такі ключі:

ім'я
вік
середня оцінка.

Виведіть дані на екран через цикл for. У циклі окрім значень також виведіть ключі.
"""

data = {"ім'я" :['Данило', 'Дмитро', 'Радія', 'Володимир'], 'вік' : [12, 22, 46, 49], 'середня оцінка': [4, 3, 2, 1]}

for key, value in data.items():
	print (key, data[key])