# Гайнутдинова Зарина гр. 4381

from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum


def TRANS_N_Z_f(num: NNum) -> ZNum:
    """
    Преобразует натуральное число NNum в целое число ZNum

    num - значение типа NNum для преобразования.

    Возврат - значение типа ZNum, преобразованное из num.
    """
    return ZNum(0, num)
