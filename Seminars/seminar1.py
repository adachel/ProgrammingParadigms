# Task 1
# Реализовать императивную ф-цию поиска эл-та в массиве
def search_imperative(array, target):
    for el in array:
        if el == target:
            return True
    return False

search_imperative([1,2,3,4,5], 2,)

# Реализовать декларативную ф-цию поиска эл-та в массиве
def search_declarative(array, target):
    return target in array          # оператор in проверяет наличие target в массиве


# Task 2
# Реализовать императивную ф-цию, кот возвращает три числа:
#   долю позитивных чисел
#   долю нулей
#   долю отрицательных чисел

def numbers_share(array):
    pos_cnt, neg_cnt, zero_cnt = 0, 0, 0 # каскадное присваивание в питоне
    for el in array:
        if el > 0:
            pos_cnt += 1
        elif el < 0:
            neg_cnt +=1
        else: zero_cnt += 1
    pos_shr, neg_shr, zero_shr = pos_cnt/len(array), neg_cnt/len(array), zero_cnt/len(array)
    return pos_shr, neg_shr, zero_shr

# тоже-самое в декларативном стиле
def numbers_share_declarative(array):
    pos_cnt = len(list(filter(lambda x: x > 0, array)))
    neg_cnt = len(list(filter(lambda x: x < 0, array)))
    zero_cnt = len(list(filter(lambda x: x == 0, array)))
    counts = [pos_cnt, neg_cnt, zero_cnt]
    shares = list(map(lambda x: x / len(array), counts))
    return shares