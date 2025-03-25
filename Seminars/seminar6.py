# Task 1. Секундомер
# Контекст.
# В каждом телефоне есть это замечательное приложение.
# Секундомер - это программа, которая засекает сколько времени прошло от момента запуска до момента остановки.
# Также, как правило, там присутствует функция “паузы”, которая позволяет временно приостановить секундомер,
# с возможностью продолжить отсчет в будущем.
# Ваша задача реализовать секундомер на любом языке программирования в любой парадигме.
# Секундомер должен поддерживать следующий функционал:
#   ○ Запуск
#   ○ Пауза
#   ○ Выход из паузы
#   ○ Остановка
import time
from functools import reduce


class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.pause_accum_time = None
        self.status = 'idle'
        print('Нажмите "Enter" чтобы запустить..')
    def start(self):
        if self.status != 'idle':
            return 'Запустить можно только сброшенный секундомер'
        self.status = 'running'
        self.start_time = time.time()
        return 'Секундомер запущен'
    def stop(self):
        if self.status != 'running':
            return 'Нельзя остановить секундомер, если он не запущен'
        self.status = 'stopped'
        self.end_time = time.time()
        return 'Прошло: {} секунд.'.format(Stopwatch.elapsed_time())
    def pause(self):
        if self.status != 'running':
            return 'Нельзя приостановить секундомер, если он не запущен'
        self.status = 'paused'
        self.end_time = time.time()
        self.pause_accum_time = self.end_time - self.start_time + self.pause_accum_time
        return f'Секундомер приостановлен. Текущее время: {self.pause_accum_time}'
    def unpause(self):
        if self.status != 'paused':
            return 'Нельзя снова запустить секундомер, если он не приостановлен.'
        self.status = 'running'
        self.start_time = time.time()
        return 'Секундомер снова запущен'
    def elapsed_time(self):
        if self.start_time is None:
            raise ValueError('Секундомер не запущен')
        if self.end_time is None:
            raise ValueError('Секундомер не остановлен')
        return self.end_time - self.start_time + self.pause_accum_time

# stopwatch = Stopwatch()
# stopwatch.start()


# Task2. Среднеквадратичная ошибка(MSE)
# Контекст.
# Предположим, у нас есть модель, которая предсказывает прогноз продаж,
# и теперь мы хотим оценить насколько модель точно это делает.
# Для получения оценки “точности” модели можно использовать много разных метрик.
# Одна из популярных метрик - это “среднеквадратичная ошибка” (mean squared error или MSE).

# Пусть у нас есть два массива длины n: один с предсказаниями нашей модели - Ŷ,
# а другой с истиной (правильными ответами) - Y. Тогда можно вычислить MSE по простой формуле.
#                        n
# Формула: MSE = 1/n * S U M (Y_i - Ŷ_i)^2
#                      i = 1

# Ваша задача.
# Реализовать процедуру для вычисления MSE на любом языке в любой парадигме.
# Программа получает на вход два вектора и возвращает число - оценку MSE для этих векторов.

def calculate_mse(y_pred, y_true):
    squared_errors = \
        map(lambda x, y: (x - y) ** 2, y_pred, y_true)
    mse = \
        reduce(lambda y_i_0, y_i_1: y_i_0 + y_i_1, squared_errors) / len(y_pred)
    return mse

pred_values = [1.7, 2.2, 3.5, 7.1]
target_values = [2.0, 2.0, 4.0, 7.5]

# mse = calculate_mse(pred_values, target_values)
# print('MSE', mse)


# Task3. Сортировка слиянием
# Контекст.
# Ещё один известный и довольно эффективный алгоритм сортировки массива - сортировка слиянием (merge sort).
# Алгоритм делится на два этапа:
#  ○ этап разбиения - массив разбивается на пару массивов до тех пор, пока,
#    полученные массивы не станут массивами длины 1 (состоящими из одного элемента).
#  ○ этап слияния - соединяем пары массивов в большие массивы так, чтобы полученные массивы были отсортированы.

# Ваша задача.
# Реализовать сортировку слиянием на любом языке в любой парадигме.
# На вход ваша программа получает массив из чисел, а вернуть должна отсортированный массив.

def merge_sort(arr):
    # Тривиальный случай
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Recursive call до тех пор, пока не упадет в тривиальный случай
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    merget = []
    left_index = right_index = 0

    # Поэтапная сортировка
    while left_index < len(left_half) and right_index < len(right_half):
        # Текущий левый элемент меньше правого
        if left_half[left_index] < right_half[right_index]:
            merget.append(left_half[left_index])
            left_index += 1
        # Текущий левый элемент не меньше правого
        else:
            merget.append(right_half[right_index])
            right_index += 1

    # Добавляем остатки, если они есть
    merget.extend(left_half[left_index:])
    merget.extend(right_half[right_index:])

    return merget

arr = [5, 6, 1, 9, 3, 8, 0]
sorted_arr = merge_sort(arr)
print(sorted_arr)