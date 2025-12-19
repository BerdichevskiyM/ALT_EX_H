# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum, QNum
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.H.SCAL_HH_Q import SCAL_HH_Q_f
from modules.H.NORM_H_Q import NORM_H_Q_f


def COS_HH_Q_f(num1: HNum, num2: HNum) -> QNum:
    """
    Вычисляет косинус между кватернионами (угловую разницу)

    num1 и num2 - значение типа HNum.

    Возврат - HNum.
    """
    div = DIV_QQ_Q_f(SCAL_HH_Q_f(num1, num2), NORM_H_Q_f(num1))
    return DIV_QQ_Q_f(div, NORM_H_Q_f(num2))