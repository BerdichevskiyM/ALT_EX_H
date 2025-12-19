# Бердичевский Максим, гр. 4381

from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum


class QNum:
    """
    Структура хранения параметров для Q-модулей

    num_tor — целое число, числитель.

    den_tor — натуральное число, знаменатель.
    """
    def __init__(self, num_tor: ZNum, den_tor: NNum):
        if den_tor.A[-1] == 0:
            raise ValueError
        self.num_tor = num_tor
        self.den_tor = den_tor