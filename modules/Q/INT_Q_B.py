# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum


def INT_Q_B_f(num: QNum) -> str:
    """
    Проверяет сокращенное дробное на целое

    num - значение типа QNum.

    Возврат - str.
    """
    # Если знаменатель 1, значит целое
    if num.den_tor.n == 1 and num.den_tor.A[0] == 1:
        return 'да'
    else:
        return 'нет'