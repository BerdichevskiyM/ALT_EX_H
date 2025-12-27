import pytest
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.SQRT_Q import SQRT_Q_f


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


def test_SQRT_Q_basic():
    q_zero = create_q(0)
    sqrt_zero = SQRT_Q_f(q_zero)
    assert q_to_float(sqrt_zero) == pytest.approx(0.0, abs=0.001)

    q_one = create_q(1)
    sqrt_one = SQRT_Q_f(q_one)
    assert q_to_float(sqrt_one) == pytest.approx(1.0, abs=0.001)

    q_four = create_q(4)
    sqrt_four = SQRT_Q_f(q_four)
    assert q_to_float(sqrt_four) == pytest.approx(2.0, abs=0.001)

    q_nine = create_q(9)
    sqrt_nine = SQRT_Q_f(q_nine)
    assert q_to_float(sqrt_nine) == pytest.approx(3.0, abs=0.01)


def test_SQRT_Q_fraction():
    q_quarter = create_q(1, 4)
    sqrt_quarter = SQRT_Q_f(q_quarter)
    assert q_to_float(sqrt_quarter) == pytest.approx(0.5, abs=0.001)

    q_four_ninths = create_q(4, 9)
    sqrt_four_ninths = SQRT_Q_f(q_four_ninths)
    assert q_to_float(sqrt_four_ninths) == pytest.approx(2 / 3, abs=0.001)

    q_twenty_five = create_q(25, 36)
    sqrt_twenty_five = SQRT_Q_f(q_twenty_five)
    assert q_to_float(sqrt_twenty_five) == pytest.approx(5 / 6, abs=0.001)


def test_SQRT_Q_approximation():
    q_two = create_q(2)
    sqrt_two = SQRT_Q_f(q_two)
    assert q_to_float(sqrt_two) == pytest.approx(1.4142, abs=0.001)

    q_three = create_q(3)
    sqrt_three = SQRT_Q_f(q_three)
    assert q_to_float(sqrt_three) == pytest.approx(1.7321, abs=0.001)

    q_ten = create_q(10)
    sqrt_ten = SQRT_Q_f(q_ten)
    assert q_to_float(sqrt_ten) == pytest.approx(3.1623, abs=0.001)


def test_SQRT_Q_negative():
    q_neg_one = create_q(-1)

    with pytest.raises(ValueError) as exc_info:
        SQRT_Q_f(q_neg_one)
    assert "Невозможно вычислить корень из отрицательного числа" in str(exc_info.value)

    q_neg_four = create_q(-4)
    with pytest.raises(ValueError):
        SQRT_Q_f(q_neg_four)

    q_neg_half = create_q(-1, 2)
    with pytest.raises(ValueError):
        SQRT_Q_f(q_neg_half)


def test_SQRT_Q_property():
    from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f

    test_values = [
        create_q(2),
        create_q(3),
        create_q(5),
        create_q(10),
        create_q(1, 2),
        create_q(3, 7),
        create_q(100),
    ]

    for q in test_values:
        sqrt_q = SQRT_Q_f(q)
        squared = MUL_QQ_Q_f(sqrt_q, sqrt_q)

        original_val = q_to_float(q)
        squared_val = q_to_float(squared)

        assert squared_val == pytest.approx(original_val, rel=0.01)


def test_SQRT_Q_large_numbers():
    q_10000 = create_q(10000)
    sqrt_10000 = SQRT_Q_f(q_10000)
    assert q_to_float(sqrt_10000) == pytest.approx(100.0, abs=0.01)

    q_big = create_q(123456789)
    sqrt_big = SQRT_Q_f(q_big)
    assert q_to_float(sqrt_big) == pytest.approx(11111.111, abs=0.01)

    q_small = create_q(1, 10000)
    sqrt_small = SQRT_Q_f(q_small)
    assert q_to_float(sqrt_small) == pytest.approx(0.01, abs=0.001)


if __name__ == "__main__":
    pytest.main()