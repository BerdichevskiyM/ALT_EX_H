# Гайнутдинова Зарина, гр. 4381

from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum


def MUL_ZM_Z_f(num: ZNum) -> ZNum:
    """
    Умножает целое число на (-1)

    num - значение типа ZNum.

    Возврат - значение типа ZNum.
    """
    # если исходное число 0, просто оставляем его
    if POZ_Z_D_f(num) == 0:
        return num
    # иначе меняем знак числа
    else:
        new_sign = 1 if num.b == 0 else 0
    return ZNum(new_sign, NNum(num.n, num.A))