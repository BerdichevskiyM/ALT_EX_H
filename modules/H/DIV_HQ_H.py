# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


def DIV_HQ_H_f(num1: HNum, num2: QNum) -> HNum:
    """
    Делит кватернион на рациональное число.

    num1 - значение типа HNum и num2 - значение типа QNum.

    Возврат - HNum.
    """
    trans_norm = QNum(ZNum(num2.num_tor.b, num2.den_tor), NNum(num2.num_tor.n, num2.num_tor.A))
    return HNum(MUL_QQ_Q_f(num1.s, trans_norm), MUL_QQ_Q_f(num1.x, trans_norm), MUL_QQ_Q_f(num1.y, trans_norm),
                MUL_QQ_Q_f(num1.z, trans_norm))