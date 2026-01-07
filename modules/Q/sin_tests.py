import pytest
import math
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.SIN_Q import SIN_Q_f
from modules.Q.PI_Q import PI_Q_f


def create_n(num: int) -> NNum:
    if num < 0:
        raise ValueError()
    digits = list(map(int, str(num)))[::-1]
    return NNum(len(digits), digits)


def create_z(num: int) -> ZNum:
    sign = 1 if num < 0 else 0
    digits = list(map(int, str(abs(num))))[::-1]
    return ZNum(sign, NNum(len(digits), digits))


def create_q(num: int, den: int = 1) -> QNum:
    if den == 0:
        raise ValueError()
    return QNum(create_z(num), create_n(den))


def q_to_float(q: QNum) -> float:
    num = int(''.join(map(str, q.num_tor.A[::-1]))) * (-1 if q.num_tor.b == 1 else 1)
    den = int(''.join(map(str, q.den_tor.A[::-1])))
    return num / den


def test_PI_Q():
    pi_q = PI_Q_f()
    pi_float = q_to_float(pi_q)

    expected_pi = 355 / 113
    math_pi = math.pi

    assert pi_float == pytest.approx(expected_pi, abs=1e-10)
    assert pi_float == pytest.approx(math_pi, abs=1e-6)


def test_SIN_Q_with_pi_approximation():
    pi_q = PI_Q_f()
    pi_value = q_to_float(pi_q)

    sin_pi = SIN_Q_f(pi_q)
    assert q_to_float(sin_pi) == pytest.approx(0.0, abs=0.01)

    pi_over_2 = create_q(355, 226)
    sin_pi_over_2 = SIN_Q_f(pi_over_2)
    assert q_to_float(sin_pi_over_2) == pytest.approx(1.0, abs=0.01)

    pi_over_4 = create_q(355, 452)
    sin_pi_over_4 = SIN_Q_f(pi_over_4)
    assert q_to_float(sin_pi_over_4) == pytest.approx(math.sqrt(2) / 2, abs=0.01)

    pi_over_6 = create_q(355, 678)
    sin_pi_over_6 = SIN_Q_f(pi_over_6)
    assert q_to_float(sin_pi_over_6) == pytest.approx(0.5, abs=0.01)


def test_SIN_Q_zero():
    q_zero = create_q(0)
    sin_zero = SIN_Q_f(q_zero)
    assert q_to_float(sin_zero) == pytest.approx(0.0, abs=1e-5)


def test_SIN_Q_small_angles():
    q_small1 = create_q(1, 10)
    sin_small1 = SIN_Q_f(q_small1)
    assert q_to_float(sin_small1) == pytest.approx(math.sin(0.1), abs=0.001)

    q_small2 = create_q(1, 2)
    sin_small2 = SIN_Q_f(q_small2)
    assert q_to_float(sin_small2) == pytest.approx(math.sin(0.5), abs=0.001)


def test_SIN_Q_negative_angles():
    q_neg = create_q(-1, 2)
    sin_neg = SIN_Q_f(q_neg)
    assert q_to_float(sin_neg) == pytest.approx(math.sin(-0.5), abs=0.001)

    pi_q = PI_Q_f()
    pi_over_4 = create_q(355, 452)
    neg_pi_over_4 = create_q(-355, 452)
    sin_neg_pi_over_4 = SIN_Q_f(neg_pi_over_4)
    assert q_to_float(sin_neg_pi_over_4) == pytest.approx(-math.sqrt(2) / 2, abs=0.01)


def test_SIN_Q_truncation():
    q_angle = create_q(123456, 100000)
    sin_result = SIN_Q_f(q_angle)

    assert len(sin_result.num_tor.A) <= 10
    assert len(sin_result.den_tor.A) <= 10

    expected = math.sin(1.23456)
    assert q_to_float(sin_result) == pytest.approx(expected, abs=0.001)


def test_SIN_Q_symmetry():
    pi_q = PI_Q_f()
    pi_value = q_to_float(pi_q)

    test_values = [0.1, 0.2, 0.3, 0.5, 0.8]

    for x in test_values:
        q_x = create_q(int(x * 1000), 1000)
        sin_x = SIN_Q_f(q_x)

        q_pi_minus_x = create_q(int((pi_value - x) * 1000), 1000)
        sin_pi_minus_x = SIN_Q_f(q_pi_minus_x)

        diff = abs(q_to_float(sin_x) - q_to_float(sin_pi_minus_x))
        assert diff < 0.01


def test_SIN_Q_periodicity():
    pi_q = PI_Q_f()
    pi_value = q_to_float(pi_q)
    two_pi = 2 * pi_value

    test_values = [0.1, 0.5, 1.0, 1.5]

    for x in test_values:
        q_x = create_q(int(x * 1000), 1000)
        sin_x = SIN_Q_f(q_x)

        q_x_plus_2pi = create_q(int((x + two_pi) * 1000), 1000)
        sin_x_plus_2pi = SIN_Q_f(q_x_plus_2pi)

        diff = abs(q_to_float(sin_x) - q_to_float(sin_x_plus_2pi))
        assert diff < 0.01


if __name__ == "__main__":
    pytest.main()