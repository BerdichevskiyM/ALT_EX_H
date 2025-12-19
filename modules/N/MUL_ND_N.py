# Двойникова Валерия Алексеевна, гр. 4381.

from modules.N.N_NUM import NNum


def MUL_ND_N_f(num: NNum, k: int) -> NNum:
    """
    Умножение натурального числа на цифру

    num — словарь с ключом 'a': список цифр числа (list[int]), старшая к младшей.

    k — цифра, на которую нужно умножить (int 0–9).

    Возврат — новое число того же формата (dict).
    """
    if k < 0 or k > 9:
        raise ValueError("k должно быть натуральным числом от 0 до 9")
    if k == 0:
        return NNum(1,[0])
    
    #  получаем массив цифр числа, создаем список
    #  для результата и переменную для переноса
    a = num.A
    result = []
    carry = 0

    # проходим по всем цифрам, умножаем на k с учетом
    # переноса, записываем единицы в результат, десятки в перенос
    for digit in a:
        total = digit * k + carry
        result.append(total % 10)
        carry = total // 10

    # если после цикла остался перенос, 
    # добавляем его как новые разряды
    while carry:
        result.append(carry % 10)
        carry //= 10

    return NNum(len(result), result)
