# Бердичевский Максим, гр. 4381

from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Q.PI_Q import PI_Q_f


def RAD_Q_f(degrees: QNum) -> QNum:
    """
    Переводит градусы в радианы.

    degrees - значение типа QNum.

    Возврат - QNum.
    """
    return DIV_QQ_Q_f(MUL_QQ_Q_f(degrees, PI_Q_f()), QNum(ZNum(0, NNum(3, [0, 8, 1])), NNum(1, [1])))