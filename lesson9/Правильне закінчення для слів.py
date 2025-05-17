"""
Створіть функцію, яка буде повертати правильне закінчення кількості років.

Наприклад: при введенні числа 1 функція буде додавати слово «рік» (щоб отримати 1 рік),
при введенні 2 – 2 роки, при введенні 5 – 5 років і т. д.
"""


def ender(age_text):
    age_num = int(age_text)

    if 11 <= age_num <= 19:
        print(age_text + " років")
        return

    age_last_num = age_num % 10
    if 2 <= age_last_num <= 4:
        print(age_text + " роки")
    elif age_last_num == 1:
        print(age_text + " рік")
    else:
        print(age_text + " років")


age = input("Введіть ваш вік: ")
ender(age)
