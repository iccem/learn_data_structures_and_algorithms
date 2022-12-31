import random


def merge(A: list, B: list) -> list:
    """
    Сортировка слиянием. Merge sort.
    """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n]=B[k]
            k += 1
            n += 1
    
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C


# Рекурсивная функция
def merge_sort(A: list) -> list:
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


def get_randomlist(n: int, m: int) -> list:
    """
    Создает массив длиной n,
    содержащий набор целых чисел
    в диапазоне от 0 до m.
    """
    randomlist = []
    for i in range(0, n):
        n = random.randint(1, m)
        randomlist.append(n)
    return randomlist


if __name__ == '__main__':
    A = get_randomlist(8, 110)
    print(*A)
    merge_sort(A)
    print(*A)
    
