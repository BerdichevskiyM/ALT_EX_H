import pytest

from modules.H.H_NUM import HNum
from modules.H.NORML_H import NORML_H_f
from modules.H.NORM_H_Q import SQR_NORM_H_Q_f
from modules.N.N_NUM import NNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum


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


def test_NORML_H():
        # Кватернион (0, 6, 0, 8) — длина = 10
    h = create_h(0, 6, 0, 8)
    norm_h = NORML_H_f(h)

        # Ожидаем (0, 6/10, 0, 8/10) = (0, 0.6, 0, 0.8)
    assert norm_h.s.num_tor.A == [0]
    assert norm_h.x.num_tor.A == [6] and norm_h.x.den_tor.A == [0, 1]  # 6/10
    assert norm_h.y.num_tor.A == [0]
    assert norm_h.z.num_tor.A == [8] and norm_h.z.den_tor.A == [0, 1]  # 8/10

        # Норма нормализованного кватерниона должна быть 1
        # Проверим, что квадрат нормы ~ 1 (рационально)
    sqr_norm = SQR_NORM_H_Q_f(norm_h)
        # Должно быть 1/1
    assert sqr_norm.num_tor.A == [1] and sqr_norm.den_tor.A == [1]

if __name__ == '__main__':
    pytest.main()