# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f


def SQRT_Q_f(num: QNum) -> QNum:
    """
    Возвращает квадратный корень из рационального числа.

    num - значение типа QNum.

    Возврат - QNum.
    """
    if POZ_Z_D_f(num.num_tor) == 1:
        raise ValueError('Невозможно вычислить корень из отрицательного числа')
    sqrt = num
    half = QNum(ZNum(0, NNum(1, [1])), NNum(1, [2]))
    while True:
        next_sqrt = MUL_QQ_Q_f(half, ADD_QQ_Q_f(sqrt, DIV_QQ_Q_f(num, sqrt)))
        diff = SUB_QQ_Q_f(next_sqrt, sqrt)
        if diff.den_tor.n - diff.num_tor.n >= 9:
            break
        sqrt = next_sqrt
    return sqrt