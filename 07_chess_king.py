'''
Сколько способов добраться 
из клетки [1, 1] в [N, M],
если шагать можно только 
вправо и вниз
(не по диагонали)
'''
'''
1) Строим рекуерентно задачу
Knm - клетка строка и номер элемента в строке
количество способов достичь клетки (N, M)

2) Смотрим итоговую клетку. Определяем клетки
из которых можно попасть в итоговую -
предпоследний шаг в решении
Kij = K(i-1)j + Ki(j-1)

Пусть первая строка и первый столбец
содержат единицу в каждой ячейке количество
способов попасть в любую клетку

Добавим барьерные строку и столбец с нулями

Нельзя общитать стартовую клетку 
надо декларировать, что ее нельзя изменять ее значение

0   0   0   0   0   0   0
0   1   1   1   1   1   1
0   1   2   3   4   5   6
0   1   3   6   10  15  21
0   1   4   10  20  35  56
0   1   5   15  35
0   1   6   21  56  126 252

рекурсивно 252 вызова

Треугольник Паскаля (повернутый)

Важный момент
Т к мы работаем не в рекурсией, а с динамичесим
программированием, важно определить последовательность
вычислений чтобы опираться на ранее вычисленное

Как обеспечить обход
Два вложенных цикла for
Нужно скипнуть пурвую единичку

Расширяем область определения 
этой фукнции на котором 
мне известны значения

Всегда следует задумываться можно ли запустить
алгоритм параллельно
ограничивается только взаимосвязь данных друг с другом
Синхронизация данных потоков
?   0   1   2   3
0   1   2   3
1   2   3
2   3
3

динамичное - 36 шагов О(N^2)
-----------------------------------------------
A, B - массивы чисел
len(A) == N
len(B) == M

Какая подпоследовательность у них общая

подпоследовательность А - некий список С, который
содержит элементы А в исходном порядке,
но возможно не все

пустая последовательность - подполедовательность любой последовательности

Начнем с поиске длины наибольшей возможной подпоследовательности
частей А и В
Fij - длина наибольшей подпоследовательности частей А и В
Аi = A[0:i] - часть А, первые i элементов
Bi = B[0:j] - часть B, первые j элементов

        1+F(i-1, j-1), ai = bj
Fij =   max(Fi(j-1), F(i-1)j), ai != bj

F0j = 0   0   0   0   0   0   0
Fi0 = 0

'''


# large common subsequence
def lcs(A, B):
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1]==B[j-1]:
                F[i][j]=1+F[i-1][j-1]
            else:
                F[i][j]=max(F[i-1][j], F[i][j-1])
    return F[-1][-1]