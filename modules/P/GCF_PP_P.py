# Гайнутдинова Зарина, гр.4381
from modules.P.MOD_PP_P import MOD_PP_P_f
from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum


def GCF_PP_P_f(poly1: PNum, poly2: PNum) -> PNum:
    """
    Ищет Наибольший Общий Делитель (НОД) двух многочленов.

    poly1 - первый аргумент типа PNum.
    poly2 - второй аргумент типа Pnum.

    Возврат - значение НОД(poly1, poly2) типа PNum.

    Справка для нахождения НОДа (можно убрать но с ней легче ориентироваться):
    1. Многочлен большей степени делится на многочлен меньшей степени.
    2. Предыдущий делитель делится на получившийся остаток пока не получим 0.
    3. НОД - предпоследний получившийся остаток.
    """
    # если оба многочлена нулевые, НОД - нулевой многочлен (степень -1, числитель 0)
    if poly1.m == -1 and poly2.m == -1:
        return PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])

    # если один из многочленов нулевой изначально - НОДом является второй многочлен
    if poly1.m == -1:
        return poly2
    if poly2.m == -1:
        return poly1

    # выбираем делимое - многочлен наибольшей степени
    divisible = poly1 if poly1.m >= poly2.m else poly2
    # выбираем делитель - многочлен меньшей степени
    divider = poly1 if poly1.m < poly2.m else poly2

    # пока не получили делитель-константу, так как следующим будет нулевой полином
    while divider.m > 0:

        # находим остаток от деления
        carry = MOD_PP_P_f(divisible, divider)

        # теперь делимое - предыдущий делитель
        divisible = divider

        # теперь делитель - получившийся остаток
        divider = carry

    # в конце предыдущий сохраненный делитель - и есть наш НОД
    return divisible
