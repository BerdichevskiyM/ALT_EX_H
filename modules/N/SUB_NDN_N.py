# Землякова Анастасия, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.SUB_NN_N import SUB_NN_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f
from modules.N.com_nn_d import COM_NN_D_f


def SUB_NDN_N_f(a: NNum, b: NNum, digit: int) -> NNum:
    """
    Вычитание из натурального другого натурального, умноженного на цифру
    для случая с неотрицательным результатом.

    a - уменьшаемое натуральное число.
    b - вычитаемое натуральное число.
    digit - цифра для умножения (0-9).
    Возврат - NNum (результат a - b * digit).
    """

    # Проверка, что digit является цифрой
    if digit < 0 or digit > 9:
        raise ValueError("Цифра должна быть от 0 до 9")

    # Умножаем b на цифру
    b_multiplied = MUL_ND_N_f(b, digit)

    # Проверяем, что результат будет неотрицательным
    if COM_NN_D_f(a, b_multiplied) == 1:
        raise ValueError("Результат будет отрицательным")

    # Вычитаем b * digit из a
    result = SUB_NN_N_f(a, b_multiplied)

    return result