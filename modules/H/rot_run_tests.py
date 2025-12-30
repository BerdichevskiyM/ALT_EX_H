import pytest
import math

from modules.H.H_NUM import HNum
from modules.H.MUL_HH_H import MUL_HH_H_f
from modules.H.NORML_H import NORML_H_f
from modules.H.NORM_H_Q import NORM_H_Q_f
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.H.ROT_Q_H import ROT_Q_H_f
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


def create_h(s, x, y, z, s_den=1, x_den=1, y_den=1, z_den=1) -> HNum:
    return HNum(create_q(s, s_den), create_q(x, x_den), create_q(y, y_den), create_q(z, z_den))


def q_to_float(q: QNum) -> float:
    num = int(''.join(map(str, q.num_tor.A[::-1]))) * (-1 if q.num_tor.b == 1 else 1)
    den = int(''.join(map(str, q.den_tor.A[::-1])))
    return num / den


def h_to_tuple(h: HNum):
    return q_to_float(h.s), q_to_float(h.x), q_to_float(h.y), q_to_float(h.z)


def ROT_Q_H_zero_angle():
    axis_x = create_h(0, 1, 0, 0)
    zero_angle = create_q(0)

    # 0 радиан
    rot_zero = ROT_Q_H_f(zero_angle, axis_x)

    # При угле 0: cos(0)=1, sin(0)=0 → кватернион (1, 0, 0, 0) - единичный
    assert q_to_float(rot_zero.s) == pytest.approx(1.0, abs=1e-4)
    assert q_to_float(rot_zero.x) == pytest.approx(0.0, abs=1e-4)
    assert q_to_float(rot_zero.y) == pytest.approx(0.0, abs=1e-4)
    assert q_to_float(rot_zero.z) == pytest.approx(0.0, abs=1e-4)


def ROT_Q_H_pi_around_x():
    axis_x = create_h(0, 1, 0, 0)

    pi_q = PI_Q_f()

    rot_pi_x = ROT_Q_H_f(pi_q, axis_x)

    # При угле π: cos(π/2)=0, sin(π/2)=1
    # Кватернион: (0, 1, 0, 0)
    assert q_to_float(rot_pi_x.s) == pytest.approx(0.0, abs=0.01)
    assert q_to_float(rot_pi_x.x) == pytest.approx(1.0, abs=0.01)
    assert q_to_float(rot_pi_x.y) == pytest.approx(0.0, abs=0.01)
    assert q_to_float(rot_pi_x.z) == pytest.approx(0.0, abs=0.01)


def ROT_Q_H_pi_over_2_around_y():
    axis_y = create_h(0, 0, 1, 0)

    # π/2
    pi_over_2 = create_q(355, 226)

    rot_pi_over_2_y = ROT_Q_H_f(pi_over_2, axis_y)

    # При угле π/2: cos(π/4)=√2/2, sin(π/4)=√2/2
    # Кватернион: (√2/2, 0, √2/2, 0)
    sqrt2_over_2 = math.sqrt(2) / 2

    assert q_to_float(rot_pi_over_2_y.s) == pytest.approx(sqrt2_over_2, abs=0.01)
    assert q_to_float(rot_pi_over_2_y.x) == pytest.approx(0.0, abs=0.01)
    assert q_to_float(rot_pi_over_2_y.y) == pytest.approx(sqrt2_over_2, abs=0.01)
    assert q_to_float(rot_pi_over_2_y.z) == pytest.approx(0.0, abs=0.01)


def ROT_Q_H_small_angle():
    axis_z = create_h(0, 0, 0, 1)

    small_angle = create_q(1, 10)

    rot_small = ROT_Q_H_f(small_angle, axis_z)

    half_angle = 0.05
    expected_cos = math.cos(half_angle)
    expected_sin = math.sin(half_angle)

    assert q_to_float(rot_small.s) == pytest.approx(expected_cos, abs=0.001)
    assert q_to_float(rot_small.x) == pytest.approx(0.0, abs=0.001)
    assert q_to_float(rot_small.y) == pytest.approx(0.0, abs=0.001)
    assert q_to_float(rot_small.z) == pytest.approx(expected_sin, abs=0.001)


def ROT_Q_H_negative_angle():
    axis_x = create_h(0, 1, 0, 0)

    # -π/2
    neg_pi_over_2 = create_q(-355, 226)

    rot_neg = ROT_Q_H_f(neg_pi_over_2, axis_x)

    # При угле -π/2: cos(-π/4)=√2/2, sin(-π/4)=-√2/2
    # Кватернион: (√2/2, -√2/2, 0, 0)
    sqrt2_over_2 = math.sqrt(2) / 2

    assert q_to_float(rot_neg.s) == pytest.approx(sqrt2_over_2, abs=0.01)
    assert q_to_float(rot_neg.x) == pytest.approx(-sqrt2_over_2, abs=0.01)
    assert q_to_float(rot_neg.y) == pytest.approx(0.0, abs=0.01)
    assert q_to_float(rot_neg.z) == pytest.approx(0.0, abs=0.01)


def ROT_Q_H_arbitrary_axis():
    axis_raw = create_h(0, 1, 2, 3)

    # π/3
    pi_over_3 = create_q(355, 339)

    rot = ROT_Q_H_f(pi_over_3, axis_raw)

    # Проверяем основные свойства:
    # 1. Скалярная часть cos(θ/2)
    # 2. Векторная часть пропорциональна оси

    half_angle = math.pi / 6
    expected_cos = math.cos(half_angle)
    expected_sin = 0.5

    normal = NORML_H_f(axis_raw)

    assert q_to_float(rot.s) == pytest.approx(expected_cos, abs=0.01)
    assert q_to_float(rot.x) / expected_sin == pytest.approx(q_to_float(normal.x), abs=0.01)
    assert q_to_float(rot.y) / expected_sin == pytest.approx(q_to_float(normal.y), abs=0.01)
    assert q_to_float(rot.z) / expected_sin == pytest.approx(q_to_float(normal.z), abs=0.01)

    x = q_to_float(rot.x)
    y = q_to_float(rot.y)
    z = q_to_float(rot.z)

    ratio_xy = x / y if y != 0 else float('inf')
    ratio_xz = x / z if z != 0 else float('inf')

    assert ratio_xy == pytest.approx(0.5, abs=0.1)
    assert ratio_xz == pytest.approx(1 / 3, abs=0.1)


def ROT_Q_H_angle_doubling():
    axis_x = create_h(0, 1, 0, 0)

    # π/4
    pi_over_4 = create_q(355, 452)
    rot1 = ROT_Q_H_f(pi_over_4, axis_x)

    # π/2
    pi_over_2 = create_q(355, 226)
    rot2 = ROT_Q_H_f(pi_over_2, axis_x)

    # rot1 * rot1 (π/4 поворачиваем на π/4 = π/2)
    rot1_squared = MUL_HH_H_f(rot1, rot1)

    assert q_to_float(rot1_squared.s) == pytest.approx(q_to_float(rot2.s), abs=0.01)
    assert q_to_float(rot1_squared.x) == pytest.approx(q_to_float(rot2.x), abs=0.01)
    assert q_to_float(rot1_squared.y) == pytest.approx(q_to_float(rot2.y), abs=0.01)
    assert q_to_float(rot1_squared.z) == pytest.approx(q_to_float(rot2.z), abs=0.01)


def ROT_Q_H_unit_norm():
    test_cases = [
        (create_q(0), create_h(0, 1, 0, 0)),  # 0 вокруг X
        (create_q(355, 226), create_h(0, 0, 1, 0)),  # π/2 вокруг Y
        (create_q(355, 113), create_h(0, 0, 0, 1)),  # π вокруг Z
        (create_q(1, 2), create_h(5, 5, 5, 5, 10, 10, 10, 10)),  # 0.5 вокруг (1,1,1)
    ]

    for angle, axis in test_cases:
        rot = ROT_Q_H_f(angle, axis)
        norm = NORM_H_Q_f(rot)
        norm_float = q_to_float(norm)
        assert norm_float == pytest.approx(1.0, abs=0.01)


def ROT_Q_H_conjugate_inverse():
    from modules.H.CON_H import CON_H_f
    from modules.H.MUL_HH_H import MUL_HH_H_f

    axis = create_h(0, 1, 2, 3)
    angle = create_q(1, 3)

    rot = ROT_Q_H_f(angle, axis)

    conj = CON_H_f(rot)

    product = MUL_HH_H_f(rot, conj)

    assert q_to_float(product.s) == pytest.approx(1.0, abs=0.01)
    assert q_to_float(product.x) == pytest.approx(0.0, abs=0.01)
    assert q_to_float(product.y) == pytest.approx(0.0, abs=0.01)
    assert q_to_float(product.z) == pytest.approx(0.0, abs=0.01)


def run_all():
    ROT_Q_H_zero_angle()
    ROT_Q_H_pi_around_x()
    ROT_Q_H_pi_over_2_around_y()
    ROT_Q_H_small_angle()
    ROT_Q_H_negative_angle()
    ROT_Q_H_arbitrary_axis()
    ROT_Q_H_angle_doubling()
    ROT_Q_H_unit_norm()
    ROT_Q_H_conjugate_inverse()