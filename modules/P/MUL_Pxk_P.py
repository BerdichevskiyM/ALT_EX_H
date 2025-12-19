# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.P.P_NUM import PNum


def MUL_Pxk_P_f(poly: PNum, k: int) -> PNum:
    """
    Умножает многочлен на x^k

    poly - значение типа PNum.

    Возврат - PNum.
    """
    if k >= 0:
        new_poly = [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))] * k + poly.C
        return PNum(poly.m + k, new_poly)
    else:
        raise ValueError('k отрицательное.')