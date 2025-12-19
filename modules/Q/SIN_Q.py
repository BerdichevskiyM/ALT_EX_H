# Бердичевский Максим, гр. 4381

from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.Q.Q_NUM import QNum, NNum
from modules.N.ADD_1N_N import ADD_1N_N_f
from modules.N.com_nn_d import COM_NN_D_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.Z.TRANS_N_Z import TRANS_N_Z_f
from modules.Q.TRANS_Z_Q import TRANS_Z_Q_f
from modules.Q.POW_Q import POW_Q_f
from modules.N.FACT_N import FACT_N_f
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f
from modules.Q.DEF_Q import DEF_Q_f


def SIN_Q_f(radians: QNum) -> QNum:
    """
    Вычисляет синус угла в радианах.

    radians - значение типа QNum.

    Возврат - QNum.
    """
    x = radians
    sin = DEF_Q_f()
    sign = 1
    i = NNum(1, [0])
    two = NNum(1, [2])
    border = NNum(1, [5])
    while COM_NN_D_f(i, border) != 0:
        k = ADD_1N_N_f(MUL_NN_N_f(two, i))
        term = DIV_QQ_Q_f(POW_Q_f(x, k), TRANS_Z_Q_f(TRANS_N_Z_f(FACT_N_f(k))))
        if sign == 1:
            sin = ADD_QQ_Q_f(sin, term)
        else:
            sin = SUB_QQ_Q_f(sin, term)
        sign *= -1
        i = ADD_1N_N_f(i)
    return sin