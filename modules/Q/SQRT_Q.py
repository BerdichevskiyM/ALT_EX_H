# Бердичевский Максим, гр. 4381

from modules.Q.DEF_Q import DEF_Q_f
from modules.Q.NEG_Q import NEG_Q_f, NEGDEF_Q_f
from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Q.TRUNC_Q import TRUNC_Q_f
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f


def SQRT_Q_f(num: QNum, count=5) -> QNum:
    """
    Возвращает квадратный корень из рационального числа.

    num - значение типа QNum.
    count - кол-во итераций цикла.

    Возврат - QNum.
    """
    if POZ_Z_D_f(num.num_tor) == 1:
        raise ValueError('Невозможно вычислить корень из отрицательного числа')
    if POZ_Z_D_f(num.num_tor) == 0:
        return DEF_Q_f()
    sqrt = NEG_Q_f(NEGDEF_Q_f())
    if num.num_tor.n > num.den_tor.n:
        sqrt = DIV_QQ_Q_f(num, QNum(ZNum(0, NNum(1, [2])), NNum(1, [1])))
    half = QNum(ZNum(0, NNum(1, [1])), NNum(1, [2]))
    # Используется метод Ньютона для квадратного корня # x{n+1} = 0.5 * (x{n} + num / x{n})
    for _ in range(count):
        next_sqrt = MUL_QQ_Q_f(half, ADD_QQ_Q_f(sqrt, DIV_QQ_Q_f(num, sqrt)))
        sqrt = next_sqrt
    return TRUNC_Q_f(sqrt)