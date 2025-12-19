# Гайнутдинова Зарина, гр. 4381

from modules.Z.Z_NUM import ZNum


def POZ_Z_D_f(num: ZNum) -> int:
    """
    Определяет положительность числа (положительное, отрицательное или нулевое)

    num - значение типа ZNum.

    Возврат - значение типа int: 0 при num = 0, 1 при num < 0, 2 при num > 0.
    """
    if num.b == 1:
        return 1
    else:
        return 0 if num.A[-1] == 0 else 2