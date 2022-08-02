'''
Редакционное расстояние между строками
(Левенштейна)

A = 'колокол'
B = 'молоко'

Сколько типографических опечаток 
нужно совершить в первом слове,
чтобы получилось второе

Возможные ошибки:
1) перепутали символ
2) вставили лишний
3) потеряли нужный

- траектория редакционных правок
- множество - пространство слов


Fij - минимальное редакционное расстояние 
между срезами A[:i] и B[:j]
N - элементы по горизонтали
M - элементы по вертикали
Ответ: Fnm



Если последний символ совпадает
Ai == Bj => F _(i-1)(j-1)_ индексы

'''
# def 