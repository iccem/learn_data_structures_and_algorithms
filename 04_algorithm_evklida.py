'''
Алгоритм Евклида

На вход получаем два числа а и b.
Требуется найти НОД
(great common divisor = GCD).

НОД(а, b) - НОД(b, a % b)

            a, a = b
gcd(a, b)   gcd(a-b, b), a > b
            gcd(a, b-a), b > a
'''


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else: # a < b
        return gcd(a, b-a)

# упростим
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
# еще упростим
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)