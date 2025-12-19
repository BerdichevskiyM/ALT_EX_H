# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.H.NEG_H import NEG_H_f


def CON_H_f(num: HNum) -> HNum:
    """
    Возвращает сопряжённый кватернион.

    num - значение типа HNum.

    Возврат - HNum.
    """
    neg = NEG_H_f(num)
    return HNum(num.s, neg.x, neg.y, neg.z)