# Корреляция.
# Контекст.
# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# Ваша задача.
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
# Можете использовать любую парадигму, но рекомендую использовать функциональную,
# т.к. в этом примере она значительно упростит вам жизнь.
# Формула корреляции Пирсона: r_xy = SUM([ (x_i - M_x) * (y_i - M_y)] ) / SQR( SUM((x_i - M_x)^2) * SUM((y_i - M_y)^2) )
import math
from statistics import mean

data_x = [1, 2, 3, 4, 4, 3, 2, 3, 4, 5]
data_y = [1, 2, 3, 4, 5, 3, 2, 3, 4, 5]

def correlation_coefficient(data_x, data_y):
    m_x = mean(data_x)
    m_y = mean(data_y)
    sum_one = 0
    sum_two_1 = 0
    sum_two_2 = 0
    for i in range(len(data_x)):
        sum_one = sum_one + (data_x[i] - m_x) * (data_y[i] - m_y)
        sum_two_1 = sum_two_1 + (data_x[i] - m_x) ** 2
        sum_two_2 = sum_two_2 + (data_y[i] - m_y) ** 2

    result = sum_one / math.sqrt(sum_two_1 * sum_two_2)

    return result

print(correlation_coefficient(data_x, data_y))
