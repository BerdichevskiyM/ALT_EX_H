# Тарасов Юрий Романович, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f
from modules.N.MUL_NN_N import MUL_NN_N_f


def MUL_ZZ_Z_f(arg1: ZNum, arg2:ZNum)-> ZNum:
    """
    Умножение целых чисел

    arg1 - первое целое число

    arg2 - второе целое число

    Возврат - Znum
    """
    # получение знаков чисел
    flag1, flag2 = POZ_Z_D_f(arg1), POZ_Z_D_f(arg2)
    # получение модулей чисел
    marg1, marg2 = ABS_Z_N_f(arg1), ABS_Z_N_f(arg2)
    # получаем произведение модулей
    res = MUL_NN_N_f(marg1, marg2)
    # если одно из чисел 0
    if flag1 == 0 or flag2 == 0:
        return ZNum(0, NNum(1, [0]))
    # если оба числа с одинаковым знаком
    if flag1 == flag2:
        return ZNum(0, res)
    # знаки не сходятся -> число отрицательное
    else:
        return MUL_ZM_Z_f(ZNum(0, res))
