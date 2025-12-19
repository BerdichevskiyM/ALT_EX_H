# Тарасов Юрий Романович, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.N.DIV_NN_N import DIV_NN_N_f
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f


def DIV_ZZ_Z_f(arg1: ZNum, arg2: ZNum)-> ZNum:
    """
    Частное от деления целого на целое(делитель отличен от нуля)

    arg1 - первое целое число

    arg2 - делитель, целое число, не может быть 0

    Возврат - Znum
    """
    if arg2.n == 1 and arg2.A[0] == 0:
        raise ValueError("Ошибка. Делитель равен нулю")
    # если делимое является 0
    if arg1 == ZNum(0, NNum(1, [0])):
        return ZNum(0, NNum(1, [0]))
    # получаем знаки двух чисел
    flag1, flag2 = POZ_Z_D_f(arg1), POZ_Z_D_f(arg2)
    # получаем абсолютное значение двух чисел
    marg1, marg2 = ABS_Z_N_f(arg1), ABS_Z_N_f(arg2)
    # получаем модуль частное от деления
    res = DIV_NN_N_f(marg1, marg2)
    # сравниваем флаги
    # если == -> положительный znum
    if flag1 == flag2:
        return ZNum(0, res)
    # если != то -> отрицательное целое
    else:
        return MUL_ZM_Z_f(ZNum(0, res))
