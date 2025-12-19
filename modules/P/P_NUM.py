# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum


class PNum:
    """
    Структура хранения параметров для P-модулей

    m — степень многочлена.

    C — массив рациональных коэффициентов (первый коэффициент - свободный член).
    """
    def __init__(self, m: int, c: list[QNum]):
        normal_l = m + 2 if m == -1 else m + 1
        if m < -1 or len(c) == 0 or (c[-1].num_tor.A[-1] == 0 and m != -1) or (c[-1].num_tor.A[-1] != 0 and m == -1) \
                or len(c) != normal_l:
            raise ValueError
        self.m = m
        self.C = c