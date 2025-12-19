# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum, QNum
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


def MUL_QH_H_f(num1: QNum, num2: HNum) -> HNum:
    """
    Умножает рациональное число на кватернион.

    num1 - значение типа QNum и num2 - значение типа HNum.

    Возврат - HNum.
    """
    return HNum(MUL_QQ_Q_f(num1, num2.s), MUL_QQ_Q_f(num1, num2.x), MUL_QQ_Q_f(num1, num2.y), MUL_QQ_Q_f(num1, num2.z))