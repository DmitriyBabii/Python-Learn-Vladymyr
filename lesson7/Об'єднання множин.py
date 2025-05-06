"""
Створіть set та frozenset. Об'єднайте обидва множини в одне ціле.

Виконайте операції:

до об'єднаного множини додайте елементи 2 і 5;
видаліть число 2, а також перший елемент у множині.
"""

data = set("Good boy")
data1 = frozenset([23, 37, 8])
data.update(data1)
data.add(2)
data.add(5)
print(data)
data.remove(2)
data.pop()
print(data)
