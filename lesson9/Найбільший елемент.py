"""
Створіть функцію, яка буде знаходити найбільший елемент у списку.

Важливо: не використовуйте вбудовані функції в Python.
"""

def max_el(nums):
    max_num = nums[0]
    for el in nums:
        if el > max_num:
            max_num = el
    print(max_num)

data = input("Введіть елементи списку через кому: ")
data_list = data.split(",")

nums=[]

for el in data_list:
    nums.append(float(el))

max_el(nums)