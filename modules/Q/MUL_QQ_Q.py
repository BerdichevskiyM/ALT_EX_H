# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.Q.RED_Q_Q import RED_Q_Q_f


def MUL_QQ_Q_f(num1: QNum, num2: QNum) -> QNum:
    """
    Умножает дробь на дробь

    num1 и num2 - значение типа QNum.

    Возврат - QNum.
    """
    return RED_Q_Q_f(MULWR_QQ_Q_f(num1, num2))


def MULWR_QQ_Q_f(num1: QNum, num2: QNum) -> QNum:
    """
    Умножает дробь на дробь

    num1 и num2 - значение типа QNum.

    Возврат - QNum.
    """
    # Умножение числителей дробей
    MUL_num_tor = MUL_ZZ_Z_f(num1.num_tor, num2.num_tor)
    # Умножение знаменателей дробей
    MUL_den_tor = MUL_NN_N_f(num1.den_tor, num2.den_tor)
    # Полученная дробь
    MUL_Q = QNum(MUL_num_tor, MUL_den_tor)
    return MUL_Q

