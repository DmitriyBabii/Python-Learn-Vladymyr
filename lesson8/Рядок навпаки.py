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