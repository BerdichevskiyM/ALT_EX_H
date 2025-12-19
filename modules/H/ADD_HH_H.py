# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f


def ADD_HH_H_f(num1: HNum, num2: HNum) -> HNum:
    """
    Складывает кватернион с кватернионом

    num1 и num2 - значение типа HNum.

    Возврат - HNum.
    """
    return HNum(ADD_QQ_Q_f(num1.s, num2.s), ADD_QQ_Q_f(num1.x, num2.x), ADD_QQ_Q_f(num1.y, num2.y),
                ADD_QQ_Q_f(num1.z, num2.z))