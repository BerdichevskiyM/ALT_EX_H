# Землякова Анастасия, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f
from modules.N.MUL_Nk_N import MUL_Nk_N_f


def MUL_NN_N_f(a: NNum, b: NNum) -> NNum:
    """
    Умножение натуральных чисел.

    a - первое натуральное число.
    b - второе натуральное число.
    Возврат - NNum (произведение a * b).
    """

    # Если одно из чисел равно нулю, возвращаем ноль
    if (a.n == 1 and a.A[0] == 0) or (b.n == 1 and b.A[0] == 0):
        return NNum(1, [0])

    # Начинаем с результата = 0
    result = NNum(1, [0])

    # Умножение в столбик: для каждой цифры b
    for i in range(b.n):
        # Умножаем a на текущую цифру b
        temp1 = MUL_ND_N_f(a, b.A[i])

        # Сдвигаем результат на i разрядов влево
        temp2 = MUL_Nk_N_f(temp1, i)

        # Добавляем к общему результату
        result = ADD_NN_N_f(result, temp2)

    return result