# Хохряков Пётр Николаевич, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.GCF_NN_N import GCF_NN_N_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.N.DIV_NN_N import DIV_NN_N_f


def LCM_NN_N_f(a: NNum, b: NNum) -> NNum:
    """
    НОК натуральных чисел
    a - первое натуральное число.
    b - второе натуральное число.
    Возврат - NNum.
    """
    # GCF_NN_N
    # НОД натуральных чисел
    GCF = GCF_NN_N_f(a, b)

    # Умножение натуральных чисел
    MUL = MUL_NN_N_f(a, b)

    # Неполное частное от деления первого натурального числа на второе (делитель отличен от нуля)
    LCM = DIV_NN_N_f(MUL, GCF)

    return NNum(LCM.n, LCM.A)
