"""
Створіть функцію, яка приймає масив і елементи пошуку в ньому.
Якщо елемент в масиві присутній, функція на екран виводить True, інакше False.
"""
import re

def comparison(text, elements):
    for el in elements:
        pattern = r'\b' + re.escape(el) + r'\b'
        match = re.search(pattern, text)
        print(f"{el}: {bool(match)}")
    # for el1 in elements:
    #     nums = 0
    #     for el in text:
    #         if el1 == el:
    #             nums += 1
    #     if nums > 0:
    #         print(f"{el1}:  True")
    #     else:
    #         print(f"{el1}:  False")


text = input("Введіть базовий текст: ")
elements = input("Введіть бажані слова: ")
comparison(text, elements.split(" "))
