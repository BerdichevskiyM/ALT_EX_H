# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.Z.TRANS_N_Z import TRANS_N_Z_f
from modules.Z.TRANS_Z_N import TRANS_Z_N_f
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f
from modules.Q.RED_Q_Q import RED_Q_Q_f


def DIV_QQ_Q_f(num1: QNum, num2: QNum) -> QNum:
    """
    Делит дробь на дробь

    num1 и num2 - значение типа QNum.

    Возврат - QNum.
    """
    # Преобразование знаменателей дробей в целые числа
    TRANS1 = TRANS_N_Z_f(num1.den_tor)
    TRANS2 = TRANS_N_Z_f(num2.den_tor)
    # Умножение числителя первой дроби на знаменатель второй и наоборот
    MUL1 = MUL_ZZ_Z_f(num1.num_tor, TRANS2)
    MUL2 = MUL_ZZ_Z_f(num2.num_tor, TRANS1)
    # Проверяем знак знаменателя
    if MUL2.b == 1:
        # Если знаменатель < 0, то умножаем числитель и знаменатель на -1
        MUL2 = MUL_ZM_Z_f(MUL2)
        MUL1 = MUL_ZM_Z_f(MUL1)
    # Полученная дробь
    DIV_Q = QNum(MUL1, TRANS_Z_N_f(MUL2))
    DIV_Q = RED_Q_Q_f(DIV_Q)
    return DIV_Q
