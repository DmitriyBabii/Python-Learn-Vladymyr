"""
Виведіть кожен 3 елемент списку, починаючи з першого і закінчуючи передостаннім.

Список:
list = [3.4, 56, "Some", "Hi", 7, 3.8, 44]
"""
#  1 й варіант
print("1 й варіант:")
list = [3.4, 56, "Some", "Hi", 7, 3.8, 44]

num = len(list)
print(list[0])

for i in range(2, num, 3):
    print(list[i])
print("\n")
#  2 й варіант
print("2 й варіант:")
list = [3.4, 56, "Some", "Hi", 7, 3.8, 44]

num = len(list)
now_list = []
now_list.append(list[0])

for i in range(2, num, 3):
    now_list.append(list[i])

print(now_list)