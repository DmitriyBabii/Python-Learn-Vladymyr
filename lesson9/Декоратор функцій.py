"""
Створіть декоратор, який обгорне будь-яку функцію і буде виконувати:

виведення рядка до виконання функції: «Код до виконання функції»;
виконання переданої функції;
виведення рядка після виконання функції: «Код після виконання функції».
"""
import time


def decorator_timer(func):
    def wrapper(line):
        start = time.perf_counter()
        result = func(line)
        end = time.perf_counter()
        print(f"Час виконання: {end - start:.4f} секунд")
        return result

    return wrapper


@decorator_timer
def show(line):
    print(line)


# show("Я звичайна функція")
@decorator_timer
def new_func(num_str):
    num = int(num_str)
    time.sleep(1)
    # print(num ** 2)
    return num ** 2

show("Show")
print(new_func("5"))

# decorator_timer(new_func)("5")
