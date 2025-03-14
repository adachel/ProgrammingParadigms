# Задача №1 Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру
# для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = temp
    return numbers

# Задача №2. Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers

print(sort_list_imperative([2, 4, 1, 9, 3]))
print(sort_list_declarative([2, 4, 1, 9, 3]))