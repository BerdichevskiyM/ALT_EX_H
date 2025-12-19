# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.H.DIV_HQ_H import DIV_HQ_H_f
from modules.H.NORM_H_Q import NORM_H_Q_f


def NORML_H_f(num: HNum) -> HNum:
    """
    Возвращает нормализованный кватернион.

    num - значение типа HNum.

    Возврат - HNum.
    """
    return DIV_HQ_H_f(num, NORM_H_Q_f(num))