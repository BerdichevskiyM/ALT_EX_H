# Бердичевский Максим, гр. 4381

from modules.H.H_NUM import HNum
from modules.Q.DEF_Q import DEF_Q_f
from modules.Q.NEG_Q import NEG_Q_f, NEGDEF_Q_f


def DEF_H_f() -> HNum:
    """
    Возвращает чистый единичный кватернион.

    Возврат - HNum.
    """
    one = NEG_Q_f(NEGDEF_Q_f())
    return HNum(DEF_Q_f(), one, one, one)