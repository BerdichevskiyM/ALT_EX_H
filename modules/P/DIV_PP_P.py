# Тарасов Юрий Романович, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.P.DEG_P_N import DEG_P_N_f
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f
from modules.P.SUB_PP_P import SUB_PP_P_f


def DIV_PP_P_f(arg1: PNum, arg2: PNum) -> PNum:
    """
    Упрощенная реализация деления многочленов
    """
    if arg2.m == -1:
        raise ValueError("Деление на нулевой многочлен")
    
    # Нулевой многочлен / что-либо = нулевой многочлен
    if arg1.m == -1:
        return PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])
    
    # Если степень делимого меньше степени делителя
    if arg1.m < arg2.m:
        return PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])
    
    zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))
    
    # Инициализация результата
    result_degree = arg1.m - arg2.m
    result_coeffs = [zero_rational] * (result_degree + 1)
    
    # Рабочая копия остатка
    remainder = PNum(arg1.m, [c for c in arg1.C])
    
    while remainder.m >= arg2.m and remainder.m != -1:
        # Вычисляем коэффициент частного
        lead_remainder = remainder.C[remainder.m]  # старший коэффициент остатка
        lead_divisor = arg2.C[arg2.m]             # старший коэффициент делителя
        
        # Коэффициент для текущего члена частного
        coeff = DIV_QQ_Q_f(lead_remainder, lead_divisor)
        degree_diff = remainder.m - arg2.m
        
        # Сохраняем коэффициент в результат
        result_coeffs[degree_diff] = coeff
        
        # Вычитаем (делитель * coeff * x^degree_diff) из остатка
        # Создаем многочлен для вычитания: делитель * coeff
        subtract_poly_coeffs = [MUL_QQ_Q_f(c, coeff) for c in arg2.C]
        subtract_poly = PNum(arg2.m, subtract_poly_coeffs)
        
        # Сдвигаем на нужную степень
        shifted_subtract = MUL_Pxk_P_f(subtract_poly, degree_diff)
        
        # Вычитаем из остатка
        remainder = SUB_PP_P_f(remainder, shifted_subtract)
    
    # Убираем ведущие нули из результата
    actual_degree = result_degree
    while actual_degree >= 0:
        if not (result_coeffs[actual_degree].num_tor.n == 1 and 
                result_coeffs[actual_degree].num_tor.A[0] == 0):
            break
        actual_degree -= 1
    
    if actual_degree < 0:
        return PNum(-1, [zero_rational])
    
    return PNum(actual_degree, result_coeffs[:actual_degree + 1])