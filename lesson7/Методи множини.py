"""
Створіть множину зі слів "Hello World". Виконайте дії:

виведіть множину в консоль;
видаліть випадковий елемент (два рази);
очистіть множину від усіх елементів;
створіть frozenset зі слів "Hello World".
"""
word = set("Hello World")
print(word)
word.pop()
word.pop()
print(word)
word.clear()
print(word)
word = frozenset("Hello World")
print(word)
