"""
Створіть анонімну функцію з невстановленою кількістю параметрів.

Функція повинна виводити всі параметри на екран.
"""

# 1 variant
# def anonim(*args):
#     print(args)
#
# anonim(2, 3, 4 ,5, "G G G")

# 2 variant
anonim = lambda *args: print(args)

anonim(23, 56, "Yes")
