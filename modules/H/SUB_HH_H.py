# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f


def SUB_HH_H_f(num1: HNum, num2: HNum) -> HNum:
    """
    Вычитает кватернион num2 из кватерниона num1.

    num1 и num2 - значение типа HNum.

    Возврат - HNum.
    """
    return HNum(SUB_QQ_Q_f(num1.s, num2.s), SUB_QQ_Q_f(num1.x, num2.x), SUB_QQ_Q_f(num1.y, num2.y),
                SUB_QQ_Q_f(num1.z, num2.z))