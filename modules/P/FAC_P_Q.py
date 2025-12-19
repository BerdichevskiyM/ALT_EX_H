# Вакух Виктор Сергеевич, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.N.LCM_NN_N import LCM_NN_N_f
from modules.N.GCF_NN_N import GCF_NN_N_f
from modules.Z.TRANS_N_Z import TRANS_N_Z_f


def FAC_P_Q_f(poly: PNum) -> QNum:
    """
    Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей

    poly - многочлен.

    Возврат - рациональное число (НОД числителей / НОК знаменателей).
    """
    # Создаем корректное нулевое рациональное число
    zero_natural = NNum(1, [0])  # Натуральный ноль
    zero_z = ZNum(0, zero_natural)  # Целый ноль
    one_natural = NNum(1, [1])  # Натуральная единица
    zero_rational = QNum(zero_z, one_natural)

    # Обработка нулевого многочлена
    if poly.m == -1:
        return zero_rational

    denominators = []
    numerators = []

    # Собираем знаменатели и числители всех ненулевых коэффициентов
    for i in range(poly.m + 1):
        coeff = poly.C[i]
        denominators.append(coeff.den_tor)

        # Берем абсолютное значение числителя
        abs_num = ABS_Z_N_f(coeff.num_tor)

        # Проверяем, что числитель не нулевой
        if not (abs_num.n == 1 and abs_num.A[0] == 0):
            numerators.append(abs_num)

    # Если все коэффициенты нулевые, возвращаем 0/1
    if not numerators:
        return zero_rational

    # Вычисляем НОК знаменателей
    lcm_den = denominators[0]
    for i in range(1, len(denominators)):
        lcm_den = LCM_NN_N_f(lcm_den, denominators[i])

    # Вычисляем НОД числителей
    gcd_num = numerators[0]
    for i in range(1, len(numerators)):
        gcd_num = GCF_NN_N_f(gcd_num, numerators[i])

    # Преобразуем НОД в целое число
    gcd_num_z = TRANS_N_Z_f(gcd_num)

    return QNum(gcd_num_z, lcm_den)