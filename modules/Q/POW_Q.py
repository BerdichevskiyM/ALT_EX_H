# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.N.NZER_N_B import NZER_N_B_f
from modules.Q.TRUNC_Q import TRUNC_Q_f
from modules.Z.DIV_ZZ_Z import DIV_ZZ_Z_f
from modules.Z.MOD_ZZ_Z import MOD_ZZ_Z_f
from modules.Z.POZ_Z_D import POZ_Z_D_f


def POW_Q_f(num: QNum, k: NNum) -> QNum:
    """
    Возводит рациональное число в натуральную степень k через бинарный алгоритм.

    num1 - значение типа QNum и k - значение типа NNum.

    Возврат - QNum.
    """
    one = NNum(1, [1])
    res = QNum(ZNum(0, one), one)
    if NZER_N_B_f(k) == 'нет':
        return res
    temp = num
    two = ZNum(0, NNum(1, [2]))
    power = ZNum(0, k)
    while POZ_Z_D_f(power) != 0:
        if POZ_Z_D_f(MOD_ZZ_Z_f(power, two)) != 0:
            res = MUL_QQ_Q_f(res, temp)
        temp = MUL_QQ_Q_f(temp, temp)
        power = DIV_ZZ_Z_f(power, two)
    return TRUNC_Q_f(res, 6)