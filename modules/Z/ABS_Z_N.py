# Двойникова Валерия Алексеевна, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum


def ABS_Z_N_f(num: ZNum) -> NNum:
    """
    Возвращает абсолютное значение целого числа

    num — экземпляр ZNum.

    Возврат — NNum с теми же цифрами, без знака.
    """
    return NNum(num.n, num.A)