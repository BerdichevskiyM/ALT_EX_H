from modules.P.P_NUM import PNum
from modules.P.DIV_PP_P import DIV_PP_P_f
from modules.P.MUL_PP_P import MUL_PP_P_f
from modules.P.SUB_PP_P import SUB_PP_P_f

#Выполнил Тарасов Юрий 4381.

def MOD_PP_P_f(arg1: PNum, arg2: PNum) -> PNum:
    """
    Остаток от деления многочлена на многочлен при делении с остатком

    arg1 - первый многочлен.

    arg2 - второй многочлен, не может быть 0.

    Возврат - PNum.
    """
    if arg2.m == -1:
        raise ValueError("Ошибка. Делитель равен нулю")

    # Получим частное
    quotient = DIV_PP_P_f(arg1, arg2)
    # Получаем остаток
    res = SUB_PP_P_f(arg1, MUL_PP_P_f(arg2, quotient))
    return res
