# Хведынич Варвара Андреевна, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.com_nn_d import COM_NN_D_f


def SUB_NN_N_f(a: NNum, b: NNum) -> NNum:
    """
    Функция вычитания из большего натурального числа
    меньшее или равное ему натуральное число

    a - первое натуральное число (уменьшаемое, a ≥ b).

    b - второе натуральное число (вычитаемое).

    Возврат - NNum.
    """

    if COM_NN_D_f(a, b) == 1:
        raise ValueError("Первое число должно быть больше или равно второму")
    
    # создание нового массива для результата
    # длина результата <= длина большего числа 
    # borrow - заем из старшего разряда
    result_digits = []
    borrow = 0

    # цикл для поразрядного вычитания, начиная с младших разрядов
    for i in range(a.n):
        digit_a = a.A[i]
        digit_b = b.A[i] if i < b.n else 0

        # происходит вычитание с учетом заема
        # если результат вычитания отрицательный то
        # занимается десяток 
        tmp_result = digit_a - digit_b - borrow

        if tmp_result < 0:
            tmp_result += 10
            borrow = 1
        else:
            borrow = 0

        result_digits.append(tmp_result)

    result_len = len(result_digits)

    # цикл для удаления ведущих нулей, начиная со старшего разряда
    while result_len > 1 and result_digits[result_len - 1] == 0:
        result_digits.pop()
        result_len -= 1

    return NNum(result_len, result_digits)