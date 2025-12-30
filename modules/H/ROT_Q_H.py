# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.H.NORML_H import NORML_H_f
from modules.H.NORM_H_Q import SQR_NORM_H_Q_f
from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Q.COS_Q import COS_Q_f
from modules.Q.SIN_Q import SIN_Q_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f
from modules.Z.POZ_Z_D import POZ_Z_D_f


def ROT_Q_H_f(radians: QNum, axis: HNum) -> HNum:
    """
    Возвращает кватернион поворота некоторого угла в радианах относительно некоторой оси.

    num1 - значение типа QNum и num2 - значение типа HNum.

    Возврат - HNum.
    """
    normal_axis = axis
    if POZ_Z_D_f(SUB_QQ_Q_f(QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])),
                            SQR_NORM_H_Q_f(axis)).num_tor) == 1:
        normal_axis = NORML_H_f(axis)
    half = MUL_QQ_Q_f(QNum(ZNum(0, NNum(1, [1])), NNum(1, [2])), radians)
    sin = SIN_Q_f(half)
    return HNum(COS_Q_f(half), MUL_QQ_Q_f(sin, normal_axis.x), MUL_QQ_Q_f(sin, normal_axis.y),
                MUL_QQ_Q_f(sin, normal_axis.z))