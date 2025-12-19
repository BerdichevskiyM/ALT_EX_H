# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f


def NEGDEF_Q_f() -> QNum:
    """
    Возвращает единичное отрицательное рациональное число.

    Возврат - QNum.
    """
    return QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))


def NEG_Q_f(num: QNum) -> QNum:
    """
    Меняет знак рационального числа (умножает на -1).

    num - значение типа QNum.

    Возврат - QNum.
    """
    return QNum(MUL_ZM_Z_f(num.num_tor), num.den_tor)