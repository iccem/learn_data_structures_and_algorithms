# как бы массивы

"""
A = [0] * 1000
top = 0
x = int(input())
while x != 0:
    A[top] = x
    top += 1
    x = int(input())
    
for k in range(4, -1, -1):
    print(A[k])
    
# копирование массива

N = int(input())
A = [0]*N
B = [0]*N

for k in range(N):
    A[k] = int(input())
    
for k in range(N):
    B[k] = A[k]
    
C = A # второе имя того же объекта
"""

# линейный поиск

def array_search(A:list, N:int, x:int):
    """
    Осуществляет поиск числа x в массиве A 
    длинны N от 0 до N-1 включительно.
    Возвращает индекс элемента x в массиве А
    или -1, если такого нет.
    Если в массиве несколько одинаковых
    элементов х, вернуть индекс первого по счету.
    
    Массив А длины N, x -- целое число.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    print("case: в массиве нет искомого элемента")
    if m == -1:
        print('#test1 - ok')
    else:
        print('#test1 - fail')
        
    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    print("case: в массиве есть искомый элемент и функция возвращает верный индекс")
    if m == 2:
        print('#test2 - ok')
    else:
        print('#test2 - fail')
        
    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    print("case: в массиве есть несколько искомых элементов")
    if m == 0:
        print('#test3 - ok')
    else:
        print('#test3 - fail')
        
        
test_array_search()


# Обращение массива

def invert_array(A:list, N:int):
    """
    Обращение массива в себе
    (поворот задом-наперед)
    в рамках индексов от 0 до N-1.
    """
    for k in range(N//2): # N
        # A[k] = A[N-1-k]
        # A[k], A[N-1-k] = A[N-1-k], A[k]
        A[k], A[N-1-k] = A[N-1-k], A[k]
    

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print('#test1 - ok')
    else:
        print('#test1 - fail')
        
    A2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2, 10)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        print('#test2 - ok')
    else:
        print('#test2 - fail')


# test_invert_array()


# Циклический сдвиг в массиве
def circular_shift(A:list):
    # влево в прямом порядке
    # A = []
    N = len(A)
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp

    # вправо - в обратном
    tmp = A[N-1]
    for k in range(N-2, -1, -1):
        A[k+1] = A[k]
    A[0] = tmp


# Решето Эратосфена
# Не требуется использовать умножение. 
# массив хранится ложь или истина
# предположим все числа простые
# N до которого я хочу найти все простые числа
# если число просто, то все кратные ему - правда

def sieve_of_eratosthenes(N:int):
    # N = 10
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        # if A[k] == True: ТАК ПИСАТЬ НЕ НАДО
        # чему равно 2 * 2 = 4? TRUE
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False # число составное
                
    print(A)
    for k in range(N):
        print(k,'-', 'простое' if A[k] else 'составное')
