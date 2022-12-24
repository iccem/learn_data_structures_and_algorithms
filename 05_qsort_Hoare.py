'''
Сортировка Тони Хоара (быстрая сортировка)
'''

def hoare_sort(A: list):
    if len(A) <= 1:
        return None
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoare_sort(L)
    hoare_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1
        
        
def check_sorted(A, assending=True):
    '''
    Проверка отсортированости за О(len(A)=O(n))
    '''
    flg = True
    N = len(A)
    s = 2 * int(assending)-1
    # for i in range(0, N-1):
        # if A[i] > A[i+1]:
        #     flg = False
        # break
    # return flg
    # int(True) = 1
    # int(False) = 0
    # s = 2 * x - 1
    for i in range(0, N-1):
        if s * A[i] > s * A[i+1]:
            flg = False
            break
        return flg
    