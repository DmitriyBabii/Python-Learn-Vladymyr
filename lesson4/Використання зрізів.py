"""
Виведіть кожен 3 елемент списку, починаючи з першого і закінчуючи передостаннім.

Список:
list = [3.4, 56, "Some", "Hi", 7, 3.8, 44]
"""

#  1 й варіант
print("1 й варіант:")
mass = [3.4, 56, "Some", "Hi", 7, 3.8, 44]

now_mass = [mass[0]]
now_mass.extend(mass[2:len(mass):3])
print(now_mass)