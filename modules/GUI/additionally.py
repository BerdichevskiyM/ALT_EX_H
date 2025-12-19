from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum
from modules.Q.Q_NUM import QNum
from modules.P.P_NUM import PNum
from modules.H.H_NUM import HNum
from modules.Z.TRANS_N_Z import TRANS_N_Z_f
from modules.Z.TRANS_Z_N import TRANS_Z_N_f
from modules.Q.TRANS_Z_Q import TRANS_Z_Q_f
from modules.Q.TRANS_Q_Z import TRANS_Q_Z_f


def is_Natural(number):
    """Проверяет, является ли строка натуральным числом"""
    if not isinstance(number, str) or number == '':
        return False
    return all(c.isdigit() for c in number)


def is_Integer(number):
    """Проверяет, является ли строка целым числом"""
    if not isinstance(number, str) or number == '':
        return False
    if number[0] == '-':
        return len(number) > 1 and is_Natural(number[1:])
    else:
        return is_Natural(number)


def is_Rational(number):
    """Проверяет, является ли строка рациональным числом (дробью)"""
    if not isinstance(number, str) or number == '':
        return False
    if number.count('/') > 1:
        return False
    elif number.count('/') == 1:
        num1, num2 = number.split('/')
    else:
        num1, num2 = number, '1'
    return is_Integer(num1) and is_Natural(num2) and num2 != '0'


def is_Polynomial(polynomial_str):
    """Проверяет, является ли строка многочленом (коэффициенты через пробел)"""
    if not isinstance(polynomial_str, str) or polynomial_str == '':
        return False
    coefficients = polynomial_str.split()
    return len(coefficients) > 0 and all(is_Rational(coefficient) for coefficient in coefficients)


def polynomial_to_coefficients(polynomial_str):
    """Преобразует строку многочлена в формате '3x^2 + 2x + 1' в формат коэффициентов через пробел"""
    if polynomial_str == '':
        return ''
    if is_Polynomial(polynomial_str):
        return polynomial_str
    
    # Обработка строкового формата многочлена
    polynomial_str = polynomial_str.replace('-', '+-').replace(' ', '').replace('**', '^')
    if polynomial_str[0] == '+':
        polynomial_str = polynomial_str[1:]
    
    coefficients = {}
    max_degree = 0
    
    for term in polynomial_str.split("+"):
        if term == '':
            continue
        if 'x' in term:
            if "*" in term:
                coefficient, power = term.split("*")
                power = power.split("^")[1]
            elif '^' in term:
                if 'x^' in term:
                    parts = term.split("x^")
                    coefficient = parts[0] if parts[0] else '1'
                    if coefficient == '-':
                        coefficient = '-1'
                    power = parts[1]
                else:
                    coefficient = term.split("x")[0]
                    if coefficient == '':
                        coefficient = '1'
                    elif coefficient == '-':
                        coefficient = '-1'
                    power = '1'
            else:
                coefficient = term.split("x")[0]
                if coefficient == '':
                    coefficient = '1'
                elif coefficient == '-':
                    coefficient = '-1'
                power = '1'
        else:
            coefficient, power = term, '0'
        
        if not is_Natural(power):
            raise ValueError('Степени должны быть натуральными числами')
        if not is_Rational(coefficient):
            raise ValueError('Коэффициенты должны быть рациональными числами')
        if power in coefficients:
            raise ValueError('Дублирование степеней')
        
        power = int(power)
        coefficients[power] = coefficient
        max_degree = max(max_degree, power)
    
    # Формирование массива коэффициентов
    result = ['0/1'] * (max_degree + 1)
    for power, coefficient in coefficients.items():
        result[power] = coefficient
    
    return ' '.join(result)


def get_Natural(string):
    """Преобразует строку в объект NNum
    Числа хранятся в обратном порядке: младшие разряды первыми
    Например: "100" -> NNum(3, [0, 0, 1]) (0 единиц, 0 десятков, 1 сотня)
    """
    if not is_Natural(string):
        raise ValueError('Введенное число не является натуральным')
    
    # Убираем ведущие нули из начала строки (они станут нулями в конце массива)
    string = string.lstrip('0')
    if string == '':
        string = '0'
    
    # Переворачиваем строку, чтобы младшие разряды были первыми
    digits = [int(c) for c in reversed(string)]
    
    return NNum(len(digits), digits)


def get_Integer(string):
    """Преобразует строку в объект ZNum"""
    if not is_Integer(string):
        raise ValueError('Введенное число не является целым')
    if string[0] == '-':
        natural = get_Natural(string[1:])
        return ZNum(1, natural)
    else:
        natural = get_Natural(string)
        return ZNum(0, natural)


def get_Rational(string):
    """Преобразует строку в объект QNum"""
    if not is_Rational(string):
        raise ValueError('Введенное число не является рациональным')
    if '/' in string:
        num_str, den_str = string.split('/')
    else:
        num_str, den_str = string, '1'
    numerator = get_Integer(num_str)
    denominator = get_Natural(den_str)
    return QNum(numerator, denominator)


def get_Polynomial(string):
    """Преобразует строку в объект PNum"""
    string = polynomial_to_coefficients(string)
    if not is_Polynomial(string):
        raise ValueError('Введенное выражение не является многочленом')
    
    coefficients_str = string.split()
    coefficients = [get_Rational(coef) for coef in coefficients_str]
    
    # Находим степень многочлена (последний ненулевой коэффициент)
    degree = len(coefficients) - 1
    while degree >= 0:
        # Проверяем, не равен ли коэффициент нулю
        # Коэффициент равен нулю, если числитель равен нулю (одна цифра 0)
        coeff = coefficients[degree]
        if not (coeff.num_tor.n == 1 and coeff.num_tor.A[0] == 0):
            break
        degree -= 1
    
    if degree < 0:
        # Нулевой многочлен
        zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))
        return PNum(-1, [zero_rational])
    
    # Обрезаем массив коэффициентов до реальной степени
    coefficients = coefficients[:degree + 1]
    return PNum(degree, coefficients)


def NNum_to_string(nnum: NNum) -> str:
    """Преобразует NNum в строку
    Числа хранятся в обратном порядке, поэтому переворачиваем массив
    Например: NNum(3, [0, 0, 1]) -> "100"
    """
    # Переворачиваем массив, так как младшие разряды хранятся первыми
    digits = list(reversed(nnum.A))
    
    # Убираем ведущие нули (кроме случая, когда число равно 0)
    result = ''.join(str(d) for d in digits).lstrip('0')
    
    # Если результат пустой (все нули), возвращаем "0"
    return result if result else '0'


def ZNum_to_string(znum: ZNum) -> str:
    """Преобразует ZNum в строку
    Числа хранятся в обратном порядке, поэтому переворачиваем массив
    """
    # Переворачиваем массив, так как младшие разряды хранятся первыми
    digits = list(reversed(znum.A))
    
    # Убираем ведущие нули (кроме случая, когда число равно 0)
    result = ''.join(str(d) for d in digits).lstrip('0')
    
    # Если результат пустой (все нули), возвращаем "0"
    if not result:
        result = '0'
    
    # Добавляем знак минус, если число отрицательное
    if znum.b == 1 and result != '0':
        result = '-' + result
    
    return result


def QNum_to_string(qnum: QNum) -> str:
    """Преобразует QNum в строку"""
    numerator_str = ZNum_to_string(qnum.num_tor)
    denominator_str = NNum_to_string(qnum.den_tor)
    if denominator_str == '1':
        return numerator_str
    return f"{numerator_str}/{denominator_str}"


def PNum_to_string(pnum: PNum) -> str:
    """Преобразует PNum в строку"""
    if pnum.m == -1:
        return "0"
    
    terms = []
    for i in range(pnum.m, -1, -1):  # Идем от старшей степени к младшей
        coeff = pnum.C[i]
        # Пропускаем нулевые коэффициенты
        if coeff.num_tor.n == 1 and coeff.num_tor.A[0] == 0:
            continue
        
        coeff_str = QNum_to_string(coeff)
        
        if i == 0:
            terms.append(coeff_str)
        elif i == 1:
            if coeff_str == '1' or coeff_str == '1/1':
                terms.append('x')
            elif coeff_str == '-1' or coeff_str == '-1/1':
                terms.append('-x')
            else:
                terms.append(f"{coeff_str}x")
        else:
            if coeff_str == '1' or coeff_str == '1/1':
                terms.append(f"x^{i}")
            elif coeff_str == '-1' or coeff_str == '-1/1':
                terms.append(f"-x^{i}")
            else:
                terms.append(f"{coeff_str}x^{i}")
    
    if not terms:
        return "0"
    
    # Собираем результат, правильно обрабатывая знаки
    # terms уже отсортированы от старшей степени к младшей
    result_parts = []
    for term in terms:
        if term[0] == '-':
            # Отрицательный коэффициент - добавляем с минусом
            if result_parts:
                result_parts.append(" - " + term[1:])
            else:
                result_parts.append(term)
        else:
            # Положительный коэффициент - добавляем с плюсом (кроме первого)
            if result_parts:
                result_parts.append(" + " + term)
            else:
                result_parts.append(term)
    
    return ''.join(result_parts)


def is_Quaternion(string):
    """Проверяет, является ли строка кватернионом
    Формат: "s/d x/d y/d z/d" - четыре рациональных числа через пробел
    Например: "1/1 2/3 -1/2 5/1"
    """
    if not isinstance(string, str) or string == '':
        return False
    parts = string.split()
    if len(parts) != 4:
        return False
    return all(is_Rational(part) for part in parts)


def get_Quaternion(string):
    """Преобразует строку в объект HNum
    Формат: "s/d x/d y/d z/d" - четыре рациональных числа через пробел
    """
    if not is_Quaternion(string):
        raise ValueError('Введенное выражение не является кватернионом')
    
    parts = string.split()
    if len(parts) != 4:
        raise ValueError('Кватернион должен содержать 4 компоненты')
    
    s = get_Rational(parts[0])
    x = get_Rational(parts[1])
    y = get_Rational(parts[2])
    z = get_Rational(parts[3])
    
    return HNum(s, x, y, z)


def HNum_to_string(hnum: HNum) -> str:
    """Преобразует HNum в строку
    Формат вывода: "s + x∙i + y∙j + z∙k"
    """
    s_str = QNum_to_string(hnum.s)
    x_str = QNum_to_string(hnum.x)
    y_str = QNum_to_string(hnum.y)
    z_str = QNum_to_string(hnum.z)
    
    # Проверяем, является ли компонента нулем
    def is_zero(q_str):
        return q_str == '0' or q_str == '0/1'
    
    # Формируем части кватерниона
    parts = []
    
    # Вещественная часть
    if not is_zero(s_str):
        parts.append(s_str)
    
    # Мнимая часть i
    if not is_zero(x_str):
        if parts:  # Если уже есть части, добавляем знак
            if x_str[0] == '-':
                x_abs = x_str[1:]
                if x_abs == '1' or x_abs == '1/1':
                    parts.append(' - i')
                else:
                    parts.append(f" - {x_abs}∙i")
            else:
                if x_str == '1' or x_str == '1/1':
                    parts.append(' + i')
                else:
                    parts.append(f" + {x_str}∙i")
        else:
            if x_str == '1' or x_str == '1/1':
                parts.append('i')
            elif x_str == '-1' or x_str == '-1/1':
                parts.append('-i')
            else:
                parts.append(f"{x_str}∙i")
    
    # Мнимая часть j
    if not is_zero(y_str):
        if parts:  # Если уже есть части, добавляем знак
            if y_str[0] == '-':
                y_abs = y_str[1:]
                if y_abs == '1' or y_abs == '1/1':
                    parts.append(' - j')
                else:
                    parts.append(f" - {y_abs}∙j")
            else:
                if y_str == '1' or y_str == '1/1':
                    parts.append(' + j')
                else:
                    parts.append(f" + {y_str}∙j")
        else:
            if y_str == '1' or y_str == '1/1':
                parts.append('j')
            elif y_str == '-1' or y_str == '-1/1':
                parts.append('-j')
            else:
                parts.append(f"{y_str}∙j")
    
    # Мнимая часть k
    if not is_zero(z_str):
        if parts:  # Если уже есть части, добавляем знак
            if z_str[0] == '-':
                z_abs = z_str[1:]
                if z_abs == '1' or z_abs == '1/1':
                    parts.append(' - k')
                else:
                    parts.append(f" - {z_abs}∙k")
            else:
                if z_str == '1' or z_str == '1/1':
                    parts.append(' + k')
                else:
                    parts.append(f" + {z_str}∙k")
        else:
            if z_str == '1' or z_str == '1/1':
                parts.append('k')
            elif z_str == '-1' or z_str == '-1/1':
                parts.append('-k')
            else:
                parts.append(f"{z_str}∙k")
    
    # Если все компоненты нулевые
    if not parts:
        return '0'
    
    return ''.join(parts)

