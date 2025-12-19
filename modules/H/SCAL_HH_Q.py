# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum, QNum
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f


def SCAL_HH_Q_f(num1: HNum, num2: HNum) -> QNum:
    """
    Возвращает скалярное произведение кватернионов.

    num1 и num2 - значение типа HNum.

    Возврат - QNum.
    """
    return ADD_QQ_Q_f(ADD_QQ_Q_f(MUL_QQ_Q_f(num1.s, num2.s), MUL_QQ_Q_f(num1.x, num2.x)),
                      ADD_QQ_Q_f(MUL_QQ_Q_f(num1.y, num2.y), MUL_QQ_Q_f(num1.z, num2.z)))