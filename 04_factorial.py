'''
Факториал

n! = (n-1)!*n

        1, n <= 1
f(n)    None, n < 0
        f(n)*n, n>1
'''

def f(n: int):
    assert n >= 0, "Факториал отрицательного числа не определен"
    if n == 0:
        return
    return f(n-1)*n
