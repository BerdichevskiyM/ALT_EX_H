# Гайнутдинова Зарина, гр. 4381
from modules.P.GCF_PP_P import GCF_PP_P_f
from modules.P.DER_P_P import DER_P_P_f
from modules.P.DIV_PP_P import DIV_PP_P_f
from modules.P.P_NUM import PNum


def NMR_P_P_f(poly: PNum) -> PNum:
    """
    Преобразование кратных корней в простые.

    poly - входное значение типа PNum.

    Возврат - преобразованный многочлен с простыми корнями, значение типа PNum.

    Справка по преобразованию:
    1. Найти производную многочлена.
    2. Найти НОД многочлена и его производной.
    3. Разделить исходный многочлен на НОД.
    """
    derivative = DER_P_P_f(poly)
    gcp = GCF_PP_P_f(poly, derivative)
    res = DIV_PP_P_f(poly, gcp)

    return res
