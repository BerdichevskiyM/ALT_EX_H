# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.INT_Q_B import INT_Q_B_f


def TRANS_Q_Z_f(num: QNum) -> ZNum:
    """
    Преобразует сокращённое дробное число в целое

    num - значение типа QNum.

    Возврат - ZNum.
    """
    if INT_Q_B_f(num) == 'да':
        return ZNum(num.num_tor.b, NNum(num.num_tor.n, num.num_tor.A))
    else:
        raise ValueError("Знаменатель не равен 1.")