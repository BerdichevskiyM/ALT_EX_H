# Хохряков Пётр, гр. 4381

from modules.P.P_NUM import PNum
from modules.N.N_NUM import NNum


def DEG_P_N_f(p: PNum) -> NNum:

    # Валидация входных данных
    if p is None or not isinstance(p, PNum):
        raise TypeError("Аргумент должен быть типа PNum")

    if not p.C:
        raise ValueError("Многочлен не может иметь пустой список коэффициентов")

    if p.m == -1:
        return NNum(1, [0])

    # Константа (степень 0)
    if p.m == 0:
        return NNum(1, [0])

    # Преобразовать степень многочлена в NNum
    digits = [int(d) for d in str(p.m)][::-1]
    return NNum(len(digits), digits)
