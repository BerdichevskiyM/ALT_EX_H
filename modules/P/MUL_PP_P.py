# Вакух Виктор Сергеевич, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.P.MUL_Pxk_P import MUL_Pxk_P_f
from modules.P.ADD_PP_P import ADD_PP_P_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


def MUL_PP_P_f(poly1: PNum, poly2: PNum) -> PNum:
    """
    Умножение многочленов

    poly1, poly2 - многочлены для умножения.

    Возврат - произведение многочленов.
    """
    zero_natural = NNum(1, [0])
    zero_z = ZNum(0, zero_natural)
    one_natural = NNum(1, [1])
    zero_rational = QNum(zero_z, one_natural)

    if poly1.m == -1 or poly2.m == -1:
        return PNum(-1, [zero_rational])

    result_poly = PNum(-1, [zero_rational])
    for i in range(poly1.m + 1):
        if poly1.C[i].num_tor.A[0] == 0:
            continue

        for j in range(poly2.m + 1):
            if poly2.C[j].num_tor.A[0] == 0:
                continue

            # Умножаем коэффициенты при текущих степенях
            coeff_product = MUL_QQ_Q_f(poly1.C[i], poly2.C[j])
                
            # Создаем многочлен с одним коэффициентом
            single_term = PNum(0, [coeff_product])

            # Умножаем на x^(i+j)
            shifted_term = MUL_Pxk_P_f(single_term, i + j)

            # Добавляем к результату
            result_poly = ADD_PP_P_f(result_poly, shifted_term)

    return result_poly
