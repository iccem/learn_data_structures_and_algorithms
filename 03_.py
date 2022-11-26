
A = [0] * N_max
n = 0
x = int(input())
A[n] = x
x += 1
n -= 1
x = A[n]

A = []
x = int(input())
A[n] = x
A.append(x)
n = len(A)
x = A.pop()

# list comprehension
A = [x ** 2 for x in range(10)]
B = [x ** 2 for x in A if x%2 == 0]
'''
x - временная переменная, создается только
на время создация цикла
ВАЖНО ЗАПОМНИТЬ! ЭТО работает быстрее!
'''
