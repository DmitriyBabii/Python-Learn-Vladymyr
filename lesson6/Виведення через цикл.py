"""
Створіть словник зі значеннями:

1: 1, 3: 9, 5: 25, 7: 49, 9: 81
Створіть два цикли:

У першому циклі for виведіть тільки всі значення цього словника;
У другому циклі виведіть значення та ключі словника.
"""

data = {a: a**2 for a in range(1, 10, 2)}
print(data)
print()
for el in data:
    print(data[el])
print()
for key, values in data.items():
    print(key, values, sep="-")