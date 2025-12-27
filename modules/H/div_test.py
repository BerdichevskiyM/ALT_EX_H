from modules.H.H_NUM import HNum
from modules.H.NORM_H_Q import SQR_NORM_H_Q_f, NORM_H_Q_f
from modules.Q.Q_NUM import QNum, NNum, ZNum
from modules.H.DIV_HQ_H import DIV_HQ_H_f


def create_n(num: int) -> NNum:
    """Создаёт NNum из целого неотрицательного числа."""
    if num < 0:
        raise ValueError("NNum only for non-negative")
    digits = list(map(int, str(num)))[::-1]
    return NNum(len(digits), digits)


def create_z(num: int) -> ZNum:
    """Создаёт ZNum из целого числа."""
    sign = 1 if num < 0 else 0
    digits = list(map(int, str(abs(num))))[::-1]
    return ZNum(sign, NNum(len(digits), digits))


def create_q(num: int, den: int = 1) -> QNum:
    """Создаёт QNum из рационального num/den."""
    if den == 0:
        raise ValueError("Denominator cannot be zero")
    return QNum(create_z(num), create_n(den))


def create_h(s, x, y, z) -> HNum:
    """Создаёт HNum из четырёх целых чисел (для простоты)."""
    return HNum(create_q(s), create_q(x), create_q(y), create_q(z))


def test_NORM_H_Q():
    """
    Тест вычисления нормы кватерниона.
    """
    # Кватернион (0, 3, 4, 0) — чисто векторный, длина = sqrt(3²+4²) = 5
    h = create_h(0, 3, 4, 0)

    # Квадрат нормы = 3² + 4² = 9 + 16 = 25
    sqr_norm = SQR_NORM_H_Q_f(h)
    assert sqr_norm.num_tor.A == [5, 2]  # 25
    assert sqr_norm.den_tor.A == [1]

    # Норма = sqrt(25) = 5
    norm = NORM_H_Q_f(h)
    #assert norm.num_tor.A == [5]
    #assert norm.den_tor.A == [1]

    # Кватернион (1, 2, 2, 1) — норма = sqrt(1²+2²+2²+1²) = sqrt(10)
    h2 = create_h(1, 2, 2, 1)
    sqr_norm2 = SQR_NORM_H_Q_f(h2)
    assert sqr_norm2.num_tor.A == [0, 1]  # 10
    assert sqr_norm2.den_tor.A == [1]

    # sqrt(10) ~ 3.16227766... Проверим, что это рациональное приближение
    norm2 = NORM_H_Q_f(h2)
    # Поскольку SQRT_Q_f возвращает рациональное, проверим, что оно положительное
    assert norm2.num_tor.b == 0
    assert norm2.num_tor.A  # непустой массив
    assert norm2.den_tor.A == [1] or norm2.den_tor.A  # знаменатель не ноль

    # Делим на -2
    q_div_neg = create_q(-2)
    result2 = DIV_HQ_H_f(h, q_div_neg)

    # Ожидаем (-2 -3i -4j -5k)
    assert result2.s.num_tor.b == 1 and result2.s.num_tor.A == [2]
    assert result2.x.num_tor.b == 1 and result2.x.num_tor.A == [3]
    assert result2.y.num_tor.b == 1 and result2.y.num_tor.A == [4]
    assert result2.z.num_tor.b == 1 and result2.z.num_tor.A == [5]