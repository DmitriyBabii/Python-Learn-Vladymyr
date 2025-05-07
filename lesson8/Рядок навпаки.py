"""
Напишіть програму, яка буде писати рядок навпаки.

Наприклад: 1234abcd -> dcba4321
"""


# Варіант 1
text = "1234abcd"
print(text[::-1])

# Варіант 2
def reverse(text):
    rev = ""
    i = len(text)
    while i > 0:
        rev += text[i - 1]
        i -= 1
    return rev

text = "1234abcd"
print(reverse(text))

# Варіант 3
def reverse(text):
    rev = ""
    n = len(text)
    for i in range(1, n + 1):
        rev += text[n - i]
    return rev


text = "1234abcd"
print(reverse(text))
