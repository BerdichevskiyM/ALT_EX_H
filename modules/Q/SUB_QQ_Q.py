# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.N.LCM_NN_N import LCM_NN_N_f
from modules.N.DIV_NN_N import DIV_NN_N_f
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.Z.SUB_ZZ_Z import SUB_ZZ_Z_f
from modules.Z.TRANS_N_Z import TRANS_N_Z_f
from modules.Q.RED_Q_Q import RED_Q_Q_f


def SUB_QQ_Q_f(num1: QNum, num2: QNum) -> QNum:
    """
    Вычитает из дроби дробь

    num1 и num2 - значение типа QNum.

    Возврат - QNum.
    """
    # НОК знаменателей дробей
    LCM = LCM_NN_N_f(num1.den_tor, num2.den_tor)
    # Частное от деления НОК на знаменатель
    # Далее это частное умножается на числитель соответсвующей дроби
    DIV1 = DIV_NN_N_f(LCM, num1.den_tor)
    DIV2 = DIV_NN_N_f(LCM, num2.den_tor)
    # Преобразование DIV1 и DIV2 в целые числа для дальнейшего умножения числителей дробей на DIV1 и DIV2
    TRANS1 = TRANS_N_Z_f(DIV1)
    TRANS2 = TRANS_N_Z_f(DIV2)
    # Умножение числителей дробей на DIV1 и DIV2
    MUL1 = MUL_ZZ_Z_f(num1.num_tor, TRANS1)
    MUL2 = MUL_ZZ_Z_f(num2.num_tor, TRANS2)
    # Вычитание числителей дробей
    SUB_Z = SUB_ZZ_Z_f(MUL1, MUL2)
    # Полученная дробь
    SUB_Q = QNum(SUB_Z, LCM)
    SUB_Q = RED_Q_Q_f(SUB_Q)
    return SUB_Q