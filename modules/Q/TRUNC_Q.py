# Бердичевский Максим, гр. 4381

from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.Q.Q_NUM import QNum, ZNum, NNum
from modules.Q.RED_Q_Q import RED_Q_Q_f
from modules.Z.ADD_ZZ_Z import ADD_ZZ_Z_f


def TRUNC_Q_f(num: QNum, count=4) -> QNum:
    """
    Возвращает квадратный корень из рационального числа.

    num - значение типа QNum.

    Возврат - QNum.
    """
    new_num = QNum(ZNum(num.num_tor.b, NNum(num.num_tor.n, num.num_tor.A.copy())),
                   NNum(num.den_tor.n, num.den_tor.A.copy()))
    one = NNum(1, [1])
    num_tor_c = count if num.num_tor.n >= num.den_tor.n else max(1, count - (num.den_tor.n - num.num_tor.n))
    den_tor_c = count if num.den_tor.n >= num.num_tor.n else max(1, count - (num.num_tor.n - num.den_tor.n))
    if num.num_tor.n > num_tor_c:
        last_elem = new_num.num_tor.A[-num_tor_c - 1]
        new_num.num_tor.A = new_num.num_tor.A[-num_tor_c:]
        new_num.num_tor.n = num_tor_c
        if last_elem >= 5:
            new_num.num_tor = ADD_ZZ_Z_f(new_num.num_tor, ZNum(0, one))
    if num.den_tor.n > den_tor_c:
        last_elem = new_num.den_tor.A[-den_tor_c - 1]
        new_num.den_tor.A = new_num.den_tor.A[-den_tor_c:]
        new_num.den_tor.n = den_tor_c
        if last_elem >= 5:
            new_num.den_tor = ADD_NN_N_f(new_num.den_tor, one)
    return RED_Q_Q_f(new_num)