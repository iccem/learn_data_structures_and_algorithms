# Квадратичные сортировки и TDD

# количество операция для сортировки = O(nˆ2)
# верхняя оценка - не хуже чем
# асимптотика по скорости обращения
# игнорируем требования памяти


# вставкой = insert sort
# солдаты прибегают по одному
# каждый раз массив пересортировывается

# методом выбором = choise sort
# ищем мин (или макс) - ставим "на место"
# мин = постамент == сравниваем каждый и меняем местами!
# инвариант цикла
# находим абсолютный минимум
# начало постепенно сдвигается
# N-1 проход

# методом пузырьком = bubble sort
# близорукий прапор. сортировка по два
# самый "тяжелый" элемент "всплывает"
# 4 человека = 3 сортировочных сравнения
# арифметическая прогрессия
# N(N-1) / 2

def insert_sort(A):
    '''Сортировка списка А вставками'''
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choise_sort(A):
    '''Сортировка списка А методом выбора'''
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    '''Сортировка списка А пузырьком'''
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    
def test_sort(sort_algorithm):
    print('testcase #1: ', end='')
    print('Тестируем: ', sort_algorithm.__doc__)
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    # if A == A_sorted: # len(A) операций
    #     print('OK')
    # else:
    #     print('Fail')
    print('OK' if A == A_sorted else 'Fail')
    
    print('testcase #2: ', end='')
    print('Тестируем: ', sort_algorithm.__doc__)
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')
    
    print('testcase #3: ', end='')
    print('Тестируем: ', sort_algorithm.__doc__)
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')
    

if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
