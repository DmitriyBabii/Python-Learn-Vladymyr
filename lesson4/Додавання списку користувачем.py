"""
Попросіть користувача ввести число в змінну N.



Додайте до списку some N кількість нових елементів. Кожен елемент також має вводити користувач з клавіатури.



Список:

some = [9, "Hi", 23.5, "A"]
"""

n = int(input("Введіть змінну N:  "))
some = [9, "Hi", 23.5, "A"]
for i in range(n):
    user_input = input("Введіть в список новий елемент:  ")
    some.append(user_input)
    print(some)