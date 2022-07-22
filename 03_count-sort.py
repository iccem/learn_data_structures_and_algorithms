# Сортировка подсчетом = count sort

# массив частот frequency

def count_sort(A):
    ''' Сортировка массива чисел методом подсчета '''
    N = len(A)
    F = [0] * 10
    for i in range(N):
        x = int(input())
        F[x] += 1

def test_count_sort(sort_algoriths):
    print('testcase#1: ', end='')
    print('Testing: ', count_sort.__doc__)
    A = [6, 8, 1, 9, 2, 7, 3, 5, 4]
    A_sorted = list(range(1, 10))
    count_sort(A)
    print('OK' if A == A_sorted else 'Fail')
    
if __name__ == '__main__':
    test_count_sort(count_sort)