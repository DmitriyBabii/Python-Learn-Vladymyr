"""
Створіть функцію, яка буде знаходити найбільший елемент у списку.

Важливо: не використовуйте вбудовані функції в Python.
"""

def max_el(j):
    num = j[0]
    for el in j:
        if el > num:
            num = el
    print(num)

data = input("Введіть елементи списку через кому: ")
data = data.split(",")

nums=[]

for i in range(len(data)):
    nums.append(float(data[i]))

max_el(nums)