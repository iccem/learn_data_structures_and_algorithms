'''
Для реализации бинарного поиска
массив должен быть отсортирован.
'''


def left_bound(A:list, key:int):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A:list, key:int):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


A = [1, 3, 3, 6, 7, 9]
key = 2
left_bound(A, key)
