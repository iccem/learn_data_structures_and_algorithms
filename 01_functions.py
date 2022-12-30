# Проектирование сверху вниз.

# мок-функция.
# название ф-ции должно отражать ее назначение
# документ-строка
# детализация: параметры, возвращаемые значения

# функции-заглушки
# функция консистентна. версия 1 "ура дом построен"
# функция еще ничего не делает

# прописываются зависимые функции
# названия и параметры - наброски
# док строки, описания параметров
# добиваемся, что все работает
# версия 2 творческий этап
# мечтания - описание функционала
# в каждый момент времени программа работает


# import graphics as gr

# def build_house(window, upper_left_corner, width):
#     """ Функция рисует дом """
#     height = calculate_height(width)
#     # print('дом построен')

# window = gr.GraphWin('Game', 300, 300)
# # build_house(window, gr.Point(100, 100), 100)
# # build_house()

# print('Yeah!')


# my_circle = gr.Circle(gr.Point(50, 50), 10)
# my_line = gr.Line(gr.Point(2, 4), gr.Point(4, 8))
# my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))

# метод решения задач "метод грубой силы" Brute Force
# есть исходные данные, область определения и множества значений
# если множество значений конечно, можно сказать
# если перебирать все ответы - рано или поздно попасть в правильный
# реализация "в лоб" 

def is_simple_number(x):
    """Определяет, является ли число простым.
    х - челове положительное число.
    Если простое - вернуть True, иначе False.
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

# print(is_sumple_number(int(input())))

def factorize_number(x):
    """
    Раскладывает число на множители.
    Печатает их на экран.
    х - целое положительное число.
    """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1
            
print(factorize_number(int(input())))
