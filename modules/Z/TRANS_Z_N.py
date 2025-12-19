# Гайнутдинова Зарина гр. 4381

from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum


def TRANS_Z_N_f(num: ZNum) -> NNum:
    """
    Преобразует целое неотрицательное число в натуральное

    num - значение типа ZNum для преобразования.

    Возврат - значение типа NNum, преобразованное из num.
    """
    if num.b == 1:
        raise ValueError("Число должно быть неотрицательным.")
    return NNum(num.n, num.A)