# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum, QNum
from modules.H.CON_H import CON_H_f
from modules.H.MUL_HH_H import MUL_HH_H_f
from modules.Q.SQRT_Q import SQRT_Q_f


def NORM_H_Q_f(num: HNum) -> QNum:
    """
    Возвращает норму кватерниона.

    num - значение типа HNum.

    Возврат - QNum.
    """
    return SQRT_Q_f(SQR_NORM_H_Q_f(num))


def SQR_NORM_H_Q_f(num: HNum) -> QNum:
    """
    Возвращает квадрат нормы кватерниона.

    num - значение типа HNum.

    Возврат - QNum.
    """
    return MUL_HH_H_f(CON_H_f(num), num).s