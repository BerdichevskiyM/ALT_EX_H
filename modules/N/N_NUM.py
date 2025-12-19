# Бердичевский Максим, гр. 4381

class NNum:
    """
    Структура хранения параметров для N-модулей

    n — номер старшей позиции (кол-во элементов в массиве A).

    A — массив цифр (первый разряд с индексом 0).
    """
    def __init__(self, n: int, a: list[int]):
        if n < 1 or len(a) != n or (a[-1] == 0 and n > 1) or min(a) < 0 or max(a) > 9:
            raise ValueError
        self.n = n
        self.A = a