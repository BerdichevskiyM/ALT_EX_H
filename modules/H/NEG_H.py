# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.Q.NEG_Q import NEG_Q_f


def NEG_H_f(num: HNum) -> HNum:
    """
    Меняет знак кватерниона (умножает на -1).

    num - значение типа HNum.

    Возврат - HNum.
    """
    return HNum(NEG_Q_f(num.s), NEG_Q_f(num.x), NEG_Q_f(num.y), NEG_Q_f(num.z))