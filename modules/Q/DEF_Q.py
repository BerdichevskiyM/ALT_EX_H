# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum, ZNum, NNum


def DEF_Q_f() -> QNum:
    """
    Возвращает ноль.

    Возврат - QNum.
    """
    return QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))