# Бердичевский Максим, гр. 4381

from modules.N.N_NUM import NNum


class ZNum:
    """
    Структура хранения параметров для Z-модулей

    b — знак числа (1 - минус, 0 - плюс).

    n — номер старшей позиции (кол-во элементов в массиве A).

    A — массив цифр (первый разряд с индексом 0).
    """
    def __init__(self, b: int, natural: NNum):
        if b not in [1, 0]:
            raise ValueError
        self.b = b
        self.n = natural.n
        self.A = natural.A