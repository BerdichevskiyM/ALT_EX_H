# Хохряков Пётр, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum

def LED_P_Q_f(p : PNum)->QNum:
    """
    Возвращает старший коэффициент многочлена

    p - многочлен (типа PNum)

    Возврат — QNum.
    """
    if p is None or not isinstance(p, PNum):
        raise TypeError("Аргумент должен быть типа PNum")
    
    if not p.C:
        raise ValueError("Невозможно получить старший коэффициент пустого многочлена")
    

    return p.C[-1]
