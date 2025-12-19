# Бердичевский Максим, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.NZER_N_B import NZER_N_B_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.N.ADD_1N_N import ADD_1N_N_f
from modules.N.com_nn_d import COM_NN_D_f


def FACT_N_f(num: NNum) -> NNum:
    """
    Возвращает факториал натурального числа.

    num - значение типа NNum.

    Возврат - NNum.
    """
    fact = NNum(1, [1])
    if NZER_N_B_f(num) == 'нет':
        return fact
    add = fact
    while COM_NN_D_f(add, num) != 0:
        add = ADD_1N_N_f(add)
        fact = MUL_NN_N_f(fact, add)
    return fact