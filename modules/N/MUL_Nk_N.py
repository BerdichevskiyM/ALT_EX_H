# Двойникова Валерия Алексеевна, гр. 4381.

from modules.N.N_NUM import NNum


def MUL_Nk_N_f(num: NNum, k: int) -> NNum:
    """
    Умножает число на 10^k

    Принимает экземпляр класса NNum и (натуральное число).

    k это int >=0, показатель степени 10.

    Возврат - NNum.
    """
    if not isinstance(k, int) or k < 0:
        raise ValueError("k должно быть натуральным числом >= 0")
    # если число равно нулю, результат тоже будет нулем
    if num.A[-1] == 0:
        return num
    a = [0] * k + num.A  # добавляем k нулей в начало (младший разряд первый)
    return NNum(len(a), a)
