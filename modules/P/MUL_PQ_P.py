# Хведынич Варвара Андреевна, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


def MUL_PQ_P_f(poly: PNum, number: QNum) -> PNum:
    """
    Умножение многочлена на рациональное число.
    
    poly - многочлен.

    number - рациональное число.
    
    Возвращает - PNum: многочлен, умноженный на число.
    """
    # создание нулеового рац числа 
    zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))

    # Проверка на ноль: если умножаем на ноль или полином нулевой,
    # возвращаем нулевой полином
    if all(digit == 0 for digit in number.num_tor.A) or poly.m == -1:
        return PNum(-1, [zero_rational])

    # Умножение всех коэффициентов на число
    result_coeffs = [MUL_QQ_Q_f(poly.C[i], number) for i in range(poly.m + 1)] 
    
    
    return PNum(poly.m, result_coeffs)
