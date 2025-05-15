"""
Створіть функцію, яка приймає масив і елементи пошуку в ньому.
Якщо елемент в масиві присутній, функція на екран виводить True, інакше False.
"""

def comparison(data, data1):
    data = data.split(" ")
    data1 = data1.split(" ")
    for el1 in data1:
        nums = 0
        for el in data:
            if el1 == el:
                nums += 1
        if nums > 0:
            print(f"{el1}:  True")
        else:
            print(f"{el1}:  False")

data = input("Введіть базовий текст: ")
data1 = input("Введіть бажані слова: ")
comparison(data, data1)