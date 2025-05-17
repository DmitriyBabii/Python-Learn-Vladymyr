"""
Напишіть функцію, яка приймає рядок і число. Ця ж функція знаходить масив, що складається з слів,
довжина яких більша за число, передане в функцію.
"""


def new_mass(text, size):
    mass = []
    words = text.split(" ")
    for el in words:
        if len(el) > size:
            mass.append(el)
    return mass

num = int(input("Введіть бажану довжену слів: "))
text = input("Введіть слова: ")
print(new_mass(text, num))
