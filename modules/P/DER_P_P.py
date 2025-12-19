# Хохряков Пётр, гр. 4381

from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum
from modules.Q.Q_NUM import QNum
from modules.P.P_NUM import PNum
from modules.Z.TRANS_N_Z import TRANS_N_Z_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


def DER_P_P_f(p: PNum) -> PNum:
    """
    Производная многочлена

    p - многочлен (типа PNum)

    Возврат - PNum.
    """

    if p is None or not isinstance(p, PNum):
        raise TypeError("Аргумент должен быть типа PNum")

    M = p.m
    if M in [-1, 0]:
        return PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])
    # Новый список коэффициентов, чтобы не было мутаций
    new_coefficients = []
    for i in range(1, p.m + 1):
        # Преобразуем степень i в QNum
        digits = [int(d) for d in str(i)][::-1]
        degree_qnum = QNum(TRANS_N_Z_f(NNum(len(digits), digits)), NNum(1, [1]))

        # Умножаем коэффициент на степень и СОХРАНЯЕМ результат
        new_coeff = MUL_QQ_Q_f(p.C[i], degree_qnum)
        new_coefficients.append(new_coeff)

    return PNum(len(new_coefficients) - 1, new_coefficients)




