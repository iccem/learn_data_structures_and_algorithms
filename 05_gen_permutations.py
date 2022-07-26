# Генерация всех перестановок
# рекурентный способ

def generate_number(N:int, M:int, prefix=None):
    '''
    Генерирует все числа с лидирующими нулями
    в N-ричной системе счисления (N <= 10)
    длины М.
    ''' 
    if M == 0:
        print(prefix)
        return 
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()
        
        
def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix)
        return
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")


def find(number, A):
    '''
    Ищет x в А и возвращает True, если такой есть
    False, если такого нет.
    '''
    for x in A:
        if number == x:
            return True
        return False


def generate_permutations(N:int, M:int=-1, prefix=None):
    '''
    Генерация всех перестановок N чисел в M позициях,
    в префиксом prefix.
    '''
    # if M == -1:
    #     M = N # по умолчанию N чисел в N позициях
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        # print(prefix)
        # print(*prefix)
        print(*prefix, end=", ", sep="") # FIXME
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

def test_func(some_func):
    N = 3
    M = 4


if __name__ == '__main__':
    # test_func(generate_numbers)
    # generate_number(3, 3)
    # gen_bin(5)
    generate_permutations(5)