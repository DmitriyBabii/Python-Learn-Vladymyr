"""
Попросіть користувача ввести рядок. Перевірте, чи є цей рядок паліндромом чи ні.

Підказка: паліндром є рядком, який читається однаково в обидва боки (уперед і назад).
"""

text = list(input("Введіть рядок: "))
text_reverse = text[::-1]
print(text)
print(text_reverse)
if text == text_reverse:
    print("Цей рядок паліндром !")
else:
    print("Це не паліндром !")