# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum


def TRANS_Z_Q_f(num: ZNum) -> QNum:
    """
    Преобразует целое число в дробное

    num - значение типа ZNum.

    Возврат - QNum.
    """
    # Создаем знаменатель = 1
    denominator = NNum(1, [1])

    # Создаем дробное число
    return QNum(num, denominator)