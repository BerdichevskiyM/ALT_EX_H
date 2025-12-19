# Вакух Виктор Сергеевич, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f
from modules.N.com_nn_d import COM_NN_D_f


def ADD_ZZ_Z_f(a: ZNum, b: ZNum) -> ZNum:
    """
    Сложение целых чисел
    a - первое целое число.
    b - второе целое число.
    Возврат - ZNum.
    """

    # Получаем знаки чисел
    sign_a = POZ_Z_D_f(a)
    sign_b = POZ_Z_D_f(b)

    # Получаем абсолютные значения
    abs_a = ABS_Z_N_f(a)
    abs_b = ABS_Z_N_f(b)

    # Оба числа положительные
    if sign_a == 2 and sign_b == 2:
        result_abs = ADD_NN_N_f(abs_a, abs_b)
        return ZNum(0, result_abs)

    # Оба числа отрицательные
    elif sign_a == 1 and sign_b == 1:
        result_abs = ADD_NN_N_f(abs_a, abs_b)
        return ZNum(1, result_abs)

    # Первое положительное, второе отрицательное
    elif sign_a == 2 and sign_b == 1:
        comparison = COM_NN_D_f(abs_a, abs_b)

        if comparison == 2:  # |a| > |b|
            result_abs = SUB_NN_N_f(abs_a, abs_b)
            return ZNum(0, result_abs)
        elif comparison == 1:  # |a| < |b|
            result_abs = SUB_NN_N_f(abs_b, abs_a)
            return ZNum(1, result_abs)
        else:  # |a| = |b|
            return ZNum(0, NNum(1, [0]))

    # Первое отрицательное, второе положительное
    elif sign_a == 1 and sign_b == 2:
        comparison = COM_NN_D_f(abs_a, abs_b)

        if comparison == 2:  # |a| > |b|
            result_abs = SUB_NN_N_f(abs_a, abs_b)
            return ZNum(1, result_abs)
        elif comparison == 1:  # |a| < |b|
            result_abs = SUB_NN_N_f(abs_b, abs_a)
            return ZNum(0, result_abs)
        else:  # |a| = |b|
            return ZNum(0, NNum(1, [0]))

    # Одно из чисел ноль
    elif sign_a == 0:
        return b
    else:
        return a