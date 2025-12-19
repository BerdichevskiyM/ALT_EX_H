# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.H.CON_H import CON_H_f
from modules.H.NORM_H_Q import SQR_NORM_H_Q_f
from modules.H.DIV_HQ_H import DIV_HQ_H_f


def INV_H_f(num: HNum) -> HNum:
    """
    Возвращает обратный кватернион.

    num - значение типа HNum.

    Возврат - HNum.
    """
    return DIV_HQ_H_f(CON_H_f(num), SQR_NORM_H_Q_f(num))