"""
Створіть функцію, яка буде підраховувати кількість символів у рядку. Рядок вводить користувач з клавіатури.
"""

text = input("Введіть рядок: ")
def num(text):
    text = list(text)
    n = len(text)
    return n
print(num(text))
