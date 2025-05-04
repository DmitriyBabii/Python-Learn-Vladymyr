"""
Створіть словник кількома способами:

через фігурні дужки;
за допомогою функції dict;
за допомогою методу fromkeys.
"""

data = {"aa": 1, "bb": 2, "cc": 3, "dd": "Yes"}
print(data)

data1 = dict(aa=1, bb= 2, cc=3, dd="Yes")
print(data1)

data2 = {}.fromkeys(["aa", "bb", "cc", "dd"],  "Ggggggg")
print(data2)