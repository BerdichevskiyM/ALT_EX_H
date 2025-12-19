# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum, ZNum, NNum


def PI_Q_f() -> QNum:
    """
    Возвращает константу пи (3.14).

    Возврат - QNum.
    """
    return QNum(ZNum(0, NNum(3, [5, 5, 3])), NNum(3, [3, 1, 1]))