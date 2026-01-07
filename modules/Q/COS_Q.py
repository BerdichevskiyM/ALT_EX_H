# Бердичевский Максим, гр. 4381
from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.PI_Q import PI_Q_f
from modules.Q.Q_NUM import QNum, NNum
from modules.N.com_nn_d import COM_NN_D_f
from modules.Q.TRUNC_Q import TRUNC_Q_f
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f
from modules.Q.NEG_Q import NEGDEF_Q_f
from modules.Z.Z_NUM import ZNum


def COS_Q_f(radians: QNum) -> QNum:
    """
    Вычисляет косинус угла в радианах.

    radians - значение типа QNum.

    Возврат - QNum.
    """
    x = radians
    # cos(x) = cos(-x)
    sign = 1
    # убираем знак
    if POZ_Z_D_f(x.num_tor) == 1:
        x = QNum(ZNum(0, NNum(x.num_tor.n, x.num_tor.A)), NNum(x.den_tor.n, x.den_tor.A))
    pi = PI_Q_f()
    two_pi = MUL_QQ_Q_f(pi, QNum(ZNum(0, NNum(1, [2])), NNum(1, [1])))
    # приводим к диапазону [0, 2п]
    while POZ_Z_D_f(SUB_QQ_Q_f(x, two_pi).num_tor) == 2:
        x = SUB_QQ_Q_f(x, two_pi)
    # приводим к диапазону [0, п]
    if POZ_Z_D_f(SUB_QQ_Q_f(pi, x).num_tor) == 1:
        x = SUB_QQ_Q_f(x, pi)
        sign *= -1
    # приводим к диапазону [0, п/2]
    if POZ_Z_D_f(SUB_QQ_Q_f(DIV_QQ_Q_f(pi, QNum(ZNum(0, NNum(1, [2])), NNum(1, [1]))),
                            x).num_tor) == 1:
        x = SUB_QQ_Q_f(pi, x)
        sign *= -1
    i = NNum(1, [2])
    two = NNum(1, [2])
    one = NNum(1, [1])
    border = NNum(2, [0, 1])
    temp = QNum(ZNum(0, one), one)
    sin = temp
    # Вычисляем косинус, сохраняя результат факториалов, и используем их в дальнейшем.
    # Ряд Маклорена: 1 - x^2/2! + x^4/4! - x^6/6! и т.д. Начинаем сразу с x^2/2!
    while COM_NN_D_f(i, border) != 0:
        temp = MUL_QQ_Q_f(MUL_QQ_Q_f(NEGDEF_Q_f(), temp), MUL_QQ_Q_f(x, x))
        temp = DIV_QQ_Q_f(temp, QNum(ZNum(0, i), one))
        temp = DIV_QQ_Q_f(temp, QNum(ZNum(0, SUB_NN_N_f(i, one)), one))
        sin = ADD_QQ_Q_f(sin, temp)
        i = ADD_NN_N_f(i, two)
    sin.num_tor.b = 1 if sign == -1 else 0
    return TRUNC_Q_f(sin, 6)