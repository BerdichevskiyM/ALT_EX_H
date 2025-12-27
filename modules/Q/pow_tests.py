import pytest
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.POW_Q import POW_Q_f


def create_n(num: int) -> NNum:
    digits = list(map(int, str(num)))[::-1]
    return NNum(len(digits), digits)


def create_z(num: int) -> ZNum:
    sign = 1 if num < 0 else 0
    digits = list(map(int, str(abs(num))))[::-1]
    return ZNum(sign, NNum(len(digits), digits))


def create_q(num: int, den: int = 1) -> QNum:
    return QNum(create_z(num), create_n(den))


def q_to_float(q: QNum) -> float:
    num = int(''.join(map(str, q.num_tor.A[::-1]))) * (-1 if q.num_tor.b == 1 else 1)
    den = int(''.join(map(str, q.den_tor.A[::-1])))
    return num / den


def test_POW_Q_basic():
    q_zero = create_q(0)
    k_zero = create_n(0)
    pow_zero_zero = POW_Q_f(q_zero, k_zero)
    assert q_to_float(pow_zero_zero) == pytest.approx(1.0, abs=0.001)

    q_five = create_q(5)
    pow_five_zero = POW_Q_f(q_five, k_zero)
    assert q_to_float(pow_five_zero) == pytest.approx(1.0, abs=0.001)

    k_one = create_n(1)
    q_two = create_q(2)
    pow_two_one = POW_Q_f(q_two, k_one)
    assert q_to_float(pow_two_one) == pytest.approx(2.0, abs=0.001)

    k_two = create_n(2)
    q_three = create_q(3)
    pow_three_two = POW_Q_f(q_three, k_two)
    assert q_to_float(pow_three_two) == pytest.approx(9.0, abs=0.001)

    k_three = create_n(3)
    q_four = create_q(4)
    pow_four_three = POW_Q_f(q_four, k_three)
    assert q_to_float(pow_four_three) == pytest.approx(64.0, abs=0.001)


def test_POW_Q_fraction():
    q_half = create_q(1, 2)
    k_zero = create_n(0)
    pow_half_zero = POW_Q_f(q_half, k_zero)
    assert q_to_float(pow_half_zero) == pytest.approx(1.0, abs=0.001)

    k_one = create_n(1)
    pow_half_one = POW_Q_f(q_half, k_one)
    assert q_to_float(pow_half_one) == pytest.approx(0.5, abs=0.001)

    k_two = create_n(2)
    pow_half_two = POW_Q_f(q_half, k_two)
    assert q_to_float(pow_half_two) == pytest.approx(0.25, abs=0.001)

    k_three = create_n(3)
    pow_half_three = POW_Q_f(q_half, k_three)
    assert q_to_float(pow_half_three) == pytest.approx(0.125, abs=0.001)

    q_two_thirds = create_q(2, 3)
    pow_two_thirds_two = POW_Q_f(q_two_thirds, k_two)
    assert q_to_float(pow_two_thirds_two) == pytest.approx(4 / 9, abs=0.001)

    q_three_fourths = create_q(3, 4)
    pow_three_fourths_three = POW_Q_f(q_three_fourths, k_three)
    assert q_to_float(pow_three_fourths_three) == pytest.approx(27 / 64, abs=0.001)


def test_POW_Q_negative_base():
    q_neg_two = create_q(-2)
    k_zero = create_n(0)
    pow_neg_two_zero = POW_Q_f(q_neg_two, k_zero)
    assert q_to_float(pow_neg_two_zero) == pytest.approx(1.0, abs=0.001)

    k_one = create_n(1)
    pow_neg_two_one = POW_Q_f(q_neg_two, k_one)
    assert q_to_float(pow_neg_two_one) == pytest.approx(-2.0, abs=0.001)

    k_two = create_n(2)
    pow_neg_two_two = POW_Q_f(q_neg_two, k_two)
    assert q_to_float(pow_neg_two_two) == pytest.approx(4.0, abs=0.001)

    k_three = create_n(3)
    pow_neg_two_three = POW_Q_f(q_neg_two, k_three)
    assert q_to_float(pow_neg_two_three) == pytest.approx(-8.0, abs=0.001)

    q_neg_half = create_q(-1, 2)
    pow_neg_half_two = POW_Q_f(q_neg_half, k_two)
    assert q_to_float(pow_neg_half_two) == pytest.approx(0.25, abs=0.001)

    pow_neg_half_three = POW_Q_f(q_neg_half, k_three)
    assert q_to_float(pow_neg_half_three) == pytest.approx(-0.125, abs=0.001)


def test_POW_Q_large_exponents():
    # 2^10 = 1024
    q_two = create_q(2)
    k_ten = create_n(10)
    pow_two_ten = POW_Q_f(q_two, k_ten)
    assert q_to_float(pow_two_ten) == pytest.approx(1024.0, abs=0.1)

    q_half = create_q(1, 2)
    pow_half_ten = POW_Q_f(q_half, k_ten)
    assert q_to_float(pow_half_ten) == pytest.approx(1 / 1024, abs=0.0001)

    q_ten = create_q(10)
    k_three = create_n(3)
    pow_ten_three = POW_Q_f(q_ten, k_three)
    assert q_to_float(pow_ten_three) == pytest.approx(1000.0, abs=0.1)


def test_POW_Q_truncation():
    q = create_q(1, 3)
    k = create_n(2)
    result = POW_Q_f(q, k)

    assert len(result.num_tor.A) <= 4
    assert len(result.den_tor.A) <= 4

    assert q_to_float(result) == pytest.approx(1 / 9, abs=0.001)

    q = create_q(2, 7)
    k = create_n(3)
    result = POW_Q_f(q, k)

    assert len(result.num_tor.A) <= 4
    assert len(result.den_tor.A) <= 4
    assert q_to_float(result) == pytest.approx(8 / 343, abs=0.001)


def test_POW_Q_edge_cases():
    q_one = create_q(1)
    k_hundred = create_n(100)
    pow_one_hundred = POW_Q_f(q_one, k_hundred)
    assert q_to_float(pow_one_hundred) == pytest.approx(1.0, abs=0.001)

    q_neg_one = create_q(-1)
    pow_neg_one_hundred = POW_Q_f(q_neg_one, k_hundred)
    assert q_to_float(pow_neg_one_hundred) == pytest.approx(1.0, abs=0.001)

    k_101 = create_n(101)
    pow_neg_one_101 = POW_Q_f(q_neg_one, k_101)
    assert q_to_float(pow_neg_one_101) == pytest.approx(-1.0, abs=0.001)

    q_zero = create_q(0)
    k_five = create_n(5)
    pow_zero_five = POW_Q_f(q_zero, k_five)
    assert q_to_float(pow_zero_five) == pytest.approx(0.0, abs=0.001)


def test_POW_Q_binary_algorithm():
    q = create_q(3, 2)

    k_seven = create_n(7)
    result_seven = POW_Q_f(q, k_seven)
    expected_seven = (1.5 ** 7)
    assert q_to_float(result_seven) == pytest.approx(expected_seven, abs=0.01)

    k_eight = create_n(8)
    result_eight = POW_Q_f(q, k_eight)
    expected_eight = (1.5 ** 8)
    assert q_to_float(result_eight) == pytest.approx(expected_eight, abs=0.01)

    k_15 = create_n(15)
    result_15 = POW_Q_f(q, k_15)
    expected_15 = (1.5 ** 15)
    assert q_to_float(result_15) == pytest.approx(expected_15, abs=0.5)


if __name__ == "__main__":
    pytest.main()