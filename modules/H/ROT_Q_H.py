# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Q.COS_Q import COS_Q_f
from modules.Q.SIN_Q import SIN_Q_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


def ROT_Q_H_f(radians: QNum, axis: HNum) -> HNum:
    """
    Возвращает кватернион поворота некоторого угла в радианах относительно некоторой оси.

    num1 - значение типа QNum и num2 - значение типа HNum.

    Возврат - HNum.
    """
    half = MUL_QQ_Q_f(QNum(ZNum(0, NNum(1, [1])), NNum(1, [2])), radians)
    sin = SIN_Q_f(half)
    return HNum(COS_Q_f(half), MUL_QQ_Q_f(sin, axis.x), MUL_QQ_Q_f(sin, axis.y), MUL_QQ_Q_f(sin, axis.z))