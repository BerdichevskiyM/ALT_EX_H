# Вакух Виктор Сергеевич, гр. 4381

import pytest
from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.P.FAC_P_Q import FAC_P_Q_f
from modules.P.MUL_PP_P import MUL_PP_P_f


def create_rational(num: int, den: int) -> QNum:
    abs_num = abs(num)
    if abs_num == 0:
        num_digits = [0]
    else:
        num_digits = [int(d) for d in str(abs_num)[::-1]]

    num_z = ZNum(0 if num >= 0 else 1, NNum(len(num_digits), num_digits))

    den_digits = [int(d) for d in str(den)[::-1]]
    den_n = NNum(len(den_digits), den_digits)

    return QNum(num_z, den_n)


def test_for_FAC_P_Q():
    #Простой многочлен с одинаковыми знаменателями
    poly1 = PNum(2, [create_rational(2, 3), create_rational(4, 3), create_rational(6, 3)])
    result = FAC_P_Q_f(poly1)
    assert result.num_tor.b == 0
    assert result.num_tor.A == [2]
    assert result.den_tor.A == [3]

    #Многочлен с разными знаменателями
    poly2 = PNum(2, [create_rational(1, 2), create_rational(1, 3), create_rational(1, 4)])
    result = FAC_P_Q_f(poly2)
    assert result.num_tor.b == 0
    assert result.num_tor.A == [1]
    assert result.den_tor.A == [2, 1]  # 12 = [2, 1]

    #Многочлен с одним коэффициентом
    poly3 = PNum(0, [create_rational(5, 7)])
    result = FAC_P_Q_f(poly3)
    assert result.num_tor.b == 0
    assert result.num_tor.A == [5]
    assert result.den_tor.A == [7]

    #Нулевой многочлен
    zero_poly = PNum(-1, [create_rational(0, 1)])
    result = FAC_P_Q_f(zero_poly)
    assert result.num_tor.b == 0
    assert result.num_tor.A == [0]
    assert result.den_tor.A == [1]



def test_for_MUL_PP_P():
    #Умножение констант
    poly1 = PNum(0, [create_rational(2, 1)])  # 2
    poly2 = PNum(0, [create_rational(3, 1)])  # 3
    result = MUL_PP_P_f(poly1, poly2)  # 2 * 3 = 6
    assert result.m == 0
    assert result.C[0].num_tor.A[0] != 0

    #Умножение на нулевой многочлен
    zero_poly = PNum(-1, [create_rational(0, 1)])
    poly3 = PNum(0, [create_rational(5, 1)])  # 5
    result = MUL_PP_P_f(poly3, zero_poly)  # Должен вернуть нулевой многочлен
    assert result.m == -1
    assert result.C[0].num_tor.A == [0]

    #Умножение линейного на константу
    poly4 = PNum(1, [create_rational(1, 1), create_rational(2, 1)])  # 2x + 1
    poly5 = PNum(0, [create_rational(3, 1)])  # 3
    result = MUL_PP_P_f(poly4, poly5)  # 3(2x+1) = 6x + 3
    assert result.m == 1
    assert result.C[0].num_tor.A[0] != 0  # свободный член
    assert result.C[1].num_tor.A[0] != 0  # коэффициент при x

    #Умножение одинаковых линейных многочленов
    poly6 = PNum(1, [create_rational(1, 1), create_rational(1, 1)])  # x + 1
    result = MUL_PP_P_f(poly6, poly6)
    assert result.m == 2
    for i in range(3):
        assert result.C[i].num_tor.A[0] != 0

    #Умножение многочленов с целыми коэффициентами
    poly7 = PNum(1, [create_rational(2, 1), create_rational(3, 1)])  # 3x + 2
    poly8 = PNum(1, [create_rational(1, 1), create_rational(4, 1)])  # 4x + 1
    result = MUL_PP_P_f(poly7, poly8)
    assert result.m == 2
    assert len(result.C) == 3

    #Проверка, что умножение на 1 дает тот же многочлен
    one_poly = PNum(0, [create_rational(1, 1)])
    poly9 = PNum(1, [create_rational(2, 1), create_rational(3, 1)])  # 3x + 2
    result = MUL_PP_P_f(poly9, one_poly)
    assert result.m == 1
    assert result.C[0].num_tor.A == [2]
    assert result.C[1].num_tor.A == [3]
    #Умножение многочленов с пропущенными степенями
    poly10 = PNum(2, [create_rational(2, 1), create_rational(0, 1), create_rational(3, 1)])  # 3x² + 2
    poly11 = PNum(1, [create_rational(1, 1), create_rational(4, 1)])  # 4x + 1
    result = MUL_PP_P_f(poly10, poly11)
    assert result.m == 3
    assert len(result.C) == 4

test_for_FAC_P_Q()
test_for_MUL_PP_P()
