# Хведынич Варвара Андреевна, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f


def ADD_PP_P_f(poly1: PNum, poly2: PNum) -> PNum:
    """
    Функция сложения двух многочленов с рациональными коэффициентами
    
    poly1 - первый многочлен.

    poly2 - второй многочлен.
    
    Возвращает - PNum: сумма.
    """
    # здесь просто создание рационального нулевого числа в виде дроби 0/1
    zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))
    
    max_degree = max(poly1.m, poly2.m)
    result_coeffs = []
    
    # цикл, где i принимает значения всех степеней ( максимальных )
    for i in range(max_degree + 1):
        # если степень не вышла за рамки то берем существуюзий коэффициент,
        # а иначе созданный нами нулевойю после суммируем и добавляем в массив 
        coeff1 = poly1.C[i] if i <= poly1.m else zero_rational
        coeff2 = poly2.C[i] if i <= poly2.m else zero_rational
    
        sum_coeff = ADD_QQ_Q_f(coeff1, coeff2)
        
        result_coeffs.append(sum_coeff)

    # проверяем только старший коэффициент на ноль, 
    # ибо по структуре он нулем быть не может. 
    # происходит поиск первой ненулевойЮ начиная с максимальной и лвигаясь вниз 
    actual_degree = max_degree

    # Так будет проще
    while actual_degree >= 0 and \
          all(digit == 0 for digit in result_coeffs[actual_degree].num_tor.A):
        actual_degree -= 1


    # если actual_degree стал нулем это значит, что все коэффициенты оказались нулевые. 
    # тогда возвращаем нулевой полином. как я поняла из структуры степнь -1 как раз нулевой полином 
    if actual_degree < 0:
        return PNum(-1, [zero_rational])

    # если реальная степень стала меньше исходной, то массив обрезается до фактической + 1 
    if actual_degree < max_degree:
        result_coeffs = result_coeffs[:actual_degree + 1]
    
    return PNum(actual_degree, result_coeffs)

