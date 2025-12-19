# Вакух Виктор Сергеевич, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f
from modules.Z.ADD_ZZ_Z import ADD_ZZ_Z_f


def SUB_ZZ_Z_f(a: ZNum, b: ZNum) -> ZNum:
    """
    Вычитание целых чисел

    a - уменьшаемое (целое число).

    b - вычитаемое (целое число).

    Возврат - ZNum (разность a - b).
    """

    # Умножаем b на -1 и складываем с a
    neg_b = MUL_ZM_Z_f(b)
    return ADD_ZZ_Z_f(a, neg_b)