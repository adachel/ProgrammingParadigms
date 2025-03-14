# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

# Процедурный; императивный; структурный

def print_multiplication_table(number):
    for i in range(1, 10):
        print(f"{number} x {i} = {number * i}")

print_multiplication_table(1)