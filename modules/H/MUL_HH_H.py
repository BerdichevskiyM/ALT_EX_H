# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum, QNum
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f
from modules.Q.DEF_Q import DEF_Q_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f
from modules.H.MUL_RI_HH_H import MUL_RI_HH_H_f
from modules.H.ADD_HH_H import ADD_HH_H_f


def MUL_HH_H_f(num1: HNum, num2: HNum) -> HNum:
    """
    Умножает векторно один кватернион на другой.

    num1 и num2 - значение типа HNum.

    Возврат - HNum.
    """
    real = SUB_QQ_Q_f(MUL_QQ_Q_f(num1.s, num2.s), SCAL_I_HH_Q_f(num1, num2))
    pure = ADD_HH_H_f(ADD_HH_H_f(MUL_RI_HH_H_f(num1, num2), MUL_RI_HH_H_f(num2, num1)), VEC_I_HH_H_f(num1, num2))
    # формула-псевдокод: [num1.s * num2.s - num1.v * num2.v; num1.s * num2.v + num2.s * num1.v + num1.v x num2.v]
    return HNum(real, pure.x, pure.y, pure.z)


def SCAL_I_HH_Q_f(num1: HNum, num2: HNum) -> QNum:
    """
    Возвращает скалярное произведение мнимых частей кватернионов.

    num1 и num2 - значение типа HNum.

    Возврат - QNum.
    """
    # формула-псевдокод: num1.x * num2.x + num1.y * num2.y + num1.z * num2.z
    return ADD_QQ_Q_f(ADD_QQ_Q_f(MUL_QQ_Q_f(num1.x, num2.x), MUL_QQ_Q_f(num1.y, num2.y)), MUL_QQ_Q_f(num1.z, num2.z))


def VEC_I_HH_H_f(num1: HNum, num2: HNum) -> HNum:
    """
    Возвращает чистый кватернион, а именно векторное произведение мнимых частей кватернионов.

    num1 и num2 - значение типа HNum.

    Возврат - HNum.
    """
    # формула-псевдокод: [0; num1.y * num2.z - num2.y * num1.z, num1.z * num2.x - num2.z * num1.x,
    # num1.x * num2.y - num2.x * num1.y]
    return HNum(DEF_Q_f(), SUB_QQ_Q_f(MUL_QQ_Q_f(num1.y, num2.z), MUL_QQ_Q_f(num2.y, num1.z)),
                SUB_QQ_Q_f(MUL_QQ_Q_f(num1.z, num2.x), MUL_QQ_Q_f(num2.z, num1.x)),
                SUB_QQ_Q_f(MUL_QQ_Q_f(num1.x, num2.y), MUL_QQ_Q_f(num2.x, num1.y)))