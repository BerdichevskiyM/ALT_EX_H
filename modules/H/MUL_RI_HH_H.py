# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.Q.DEF_Q import DEF_Q_f
from modules.H.MUL_QH_H import MUL_QH_H_f


def MUL_RI_HH_H_f(num_r: HNum, num_i: HNum) -> HNum:
    """
    Умножает скалярную часть одного кватерниона на мнимую часть другого.

    num1 и num2 - значение типа HNum.

    Возврат - HNum.
    """
    pure = MUL_QH_H_f(num_r.s, num_i)
    return HNum(DEF_Q_f(), pure.x, pure.y, pure.z)