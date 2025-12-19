# Землякова Анастасия, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.DIV_NN_Dk import DIV_NN_Dk_f
from modules.N.SUB_NDN_N import SUB_NDN_N_f


def DIV_NN_N_f(a: NNum, b: NNum) -> NNum:
    """
    Неполное частное от деления первого натурального числа на второе
    с остатком (делитель отличен от нуля).

    a - делимое (натуральное число).

    b - делитель (натуральное число, не ноль).

    Возврат - NNum (неполное частное).
    """

    # Проверка, что делитель не ноль
    if b.n == 1 and b.A[0] == 0:
        raise ValueError("Деление на ноль")

    # Начинаем с частного = 0
    quotient_digits = [0]
    remainder = a

    # Алгоритм деления в столбик
    while True:
        try:
            # Пытаемся найти следующую цифру
            digit, power = DIV_NN_Dk_f(remainder, b)
        except ValueError:
            # Если remainder < b, завершаем деление
            break

        if digit == 0:
            break

        # Добавляем digit на позицию power к частному
        # Увеличиваем массив частного если нужно
        while len(quotient_digits) <= power:
            quotient_digits.append(0)
        
        # Добавляем цифру на нужную позицию
        # Обрабатываем сложение с переносом
        current_pos = power
        current_digit = digit
        while current_digit > 0:
            if current_pos >= len(quotient_digits):
                quotient_digits.append(0)
            
            total = quotient_digits[current_pos] + current_digit
            quotient_digits[current_pos] = total % 10
            current_digit = total // 10
            current_pos += 1

        try:
            # Создаем b×10^power через сдвиг разрядов
            if power > 0:
                b_shifted_digits = [0] * power + b.A
                b_shifted = NNum(len(b_shifted_digits), b_shifted_digits)
            else:
                b_shifted = b
            
            # Вычитаем 1 раз
            remainder = SUB_NDN_N_f(remainder, b_shifted, digit)


                
        except ValueError:
            # Если вычитание привело к отрицательному результату,
            # значит мы перебрали - откатываем последнее вычитание и завершаем
            break

    # Удаляем ведущие нули из частного
    while len(quotient_digits) > 1 and quotient_digits[-1] == 0:
        quotient_digits.pop()
    
    return NNum(len(quotient_digits), quotient_digits)
