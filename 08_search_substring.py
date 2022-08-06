# Поиск подстроки в строке O(N*M)

# Проверка равенства строк O(N)
def equal(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

# s = 'abacabadabacabafabacabadabacabadabacabafba'
s = 'abacabadabacabafabacabadabacabadabacabdaba'
sub = 'dabac'


# Способ предобработать строку

# Префикс функция П строки
'''
Собственный суффикс - суффикс, не равный самой строке.
П-строки - длина максимального собтвенного суффикса, который является префиксом.
Попробуем применить идею динамического программирования.
Предположим, что префикс-функция для этой строки уже найдена.
Могу ли я узнать префикс функцию для данной строки с еще одним символом, если мне известна префикс-функция для всех подстрок П для s[: i] - это функция среза строки.


'''
#

def search_substring(s, sub):
    for i in range(0, len(s)-len(sub)):
        if equal(s[i:i+len(sub)], sub):
            print(i)