import tkinter as tk
from tkinter import messagebox
from modules.GUI.additionally import *
from modules.N.com_nn_d import COM_NN_D_f
from modules.N.NZER_N_B import NZER_N_B_f
from modules.N.ADD_1N_N import ADD_1N_N_f
from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f
from modules.N.MUL_Nk_N import MUL_Nk_N_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.N.SUB_NDN_N import SUB_NDN_N_f
from modules.N.DIV_NN_Dk import DIV_NN_Dk_f
from modules.N.DIV_NN_N import DIV_NN_N_f
from modules.N.MOD_NN_N import MOD_NN_N_f
from modules.N.GCF_NN_N import GCF_NN_N_f
from modules.N.LCM_NN_N import LCM_NN_N_f


class NaturalApp:
    def __init__(self, root, theme='orange'):
        # Оранжевая цветовая схема
        self.bg_color = "#1A1A1A"  # Темный фон
        self.window_color = "#2D2D2D"  # Темнее для полей ввода
        self.text_color = "#FFFFFF"  # Белый текст
        self.backlight = "#FF6B35"  # Оранжевый для активных элементов
        self.label_color = "#FFB366"  # Светло-оранжевый для меток
        self.hover_color = "#FF8C42"  # Светлее при наведении
        self.button_color = "#FF6B35"  # Оранжевая кнопка
        self.button_active = "#D45A2A"  # Темнее при нажатии
        self.entry_bg = "#2D2D2D"  # Фон полей ввода
        self.entry_fg = "#FFFFFF"  # Текст в полях ввода
        self.entry_border = "#FF6B35"  # Рамка полей ввода
        
        self.root = root
        self.root.title("Операции с натуральными числами")
        self.root.geometry("450x650")
        self.root.configure(bg=self.bg_color)
        
        # Центрируем окно
        self.center_window(450, 650)

        self.method_var = tk.StringVar(value="Сложение двух чисел")

        # Заголовок
        from tkinter import font
        title_font = font.Font(family="Segoe GUI", size=20, weight="bold")
        title_label = tk.Label(root, text="Операции с натуральными", 
                              bg=self.bg_color, fg=self.backlight, font=title_font)
        title_label.pack(pady=(20, 15))

        # Выбор метода
        methods = [
            "Сравнение чисел",
            "Проверка на ноль",
            "Прибавление единицы",
            "Сложение двух чисел",
            "Вычитание двух чисел",
            "Умножение на цифру",
            "Умножение на 10ⁿ",
            "Умножение двух чисел",
            "Вычитание умноженного на цифру",
            "DIV_NN_Dk",
            "Деление целочисленное",
            "Деление с остатком",
            "НОД",
            "НОК"
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=15, padx=20, fill=tk.X)

        label_font = font.Font(family="Segoe GUI", size=11)
        tk.Label(method_frame, text="Операция: ", bg=self.bg_color, fg=self.label_color, font=label_font).pack(side=tk.LEFT, padx=(0, 10))

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg=self.text_color, 
                                highlightbackground=self.button_color,
                                relief=tk.FLAT, 
                                activebackground=self.button_color,
                                activeforeground=self.text_color,
                                highlightthickness=2, 
                                font=label_font,
                                bd=0,
                                indicatoron=1)
        self.method_menu.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Настройка событий для изменения цвета фона
        self.method_menu.bind("<Enter>", lambda e: self.method_menu.config(bg=self.hover_color))
        self.method_menu.bind("<Leave>", lambda e: self.method_menu.config(bg=self.window_color))

        # Контейнер для полей ввода
        input_frame = tk.Frame(root, bg=self.bg_color)
        input_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=False)

        # Ввод первого числа
        input_font = font.Font(family="Segoe GUI", size=10)
        self.first_number_label = tk.Label(input_frame, text="Первое число (например: 123):", 
                                           bg=self.bg_color, fg=self.label_color, font=input_font)
        self.first_number_label.pack(anchor=tk.W, pady=(0, 5))
        self.first_number_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                           insertbackground='white', 
                                           font=font.Font(family="Segoe GUI", size=12),
                                           relief=tk.FLAT, bd=2, highlightthickness=1,
                                           highlightbackground=self.entry_border,
                                           highlightcolor=self.backlight)
        self.first_number_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Ввод второго числа
        self.second_number_label = tk.Label(input_frame, text="Второе число (например: 456):", 
                                            bg=self.bg_color, fg=self.text_color, font=input_font)
        self.second_number_label.pack(anchor=tk.W, pady=(0, 5))
        self.second_number_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                            insertbackground='white', 
                                            font=font.Font(family="Segoe GUI", size=12),
                                            relief=tk.FLAT, bd=2, highlightthickness=1,
                                            highlightbackground=self.entry_border,
                                            highlightcolor=self.backlight)
        self.second_number_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Ввод цифры
        self.digit_label = tk.Label(input_frame, text="Цифра:", 
                                    bg=self.bg_color, fg=self.text_color, font=input_font)
        self.digit_label.pack(anchor=tk.W, pady=(0, 5))
        self.digit_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                    insertbackground='white', 
                                    font=font.Font(family="Segoe GUI", size=12),
                                    relief=tk.FLAT, bd=2, highlightthickness=1,
                                    highlightbackground=self.entry_border,
                                    highlightcolor=self.backlight)
        self.digit_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Фрейм для результата с прокруткой
        result_frame = tk.Frame(input_frame, bg=self.bg_color)
        result_frame.pack(pady=10, fill=tk.BOTH, expand=False)

        # Скроллбар
        result_scrollbar = tk.Scrollbar(result_frame, bg=self.window_color, troughcolor=self.bg_color)
        result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text виджет вместо Label
        result_font = font.Font(family="Segoe GUI", size=13, weight="bold")  # для Polynomial_GUI.py size=12
        self.result_text = tk.Text(result_frame, bg=self.entry_bg, fg=self.backlight,
                                   font=result_font, wrap=tk.WORD,
                                   height=4, relief=tk.FLAT, bd=2,  # для Polynomial_GUI.py height=5
                                   highlightthickness=1, highlightbackground=self.entry_border,
                                   yscrollcommand=result_scrollbar.set, state=tk.DISABLED)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        result_scrollbar.config(command=self.result_text.yview)

        # Кнопка для выполнения операции
        button_font = font.Font(family="Segoe GUI", size=13, weight="bold")
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, 
                                         bg=self.button_color, fg="white", 
                                         font=button_font, 
                                         relief=tk.FLAT, bd=0,
                                         padx=30, pady=12,
                                         cursor="hand2",
                                         activebackground=self.button_active,
                                         activeforeground="white")
        self.calculate_button.pack(pady=20, ipadx=20, ipady=5)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))
    
    def center_window(self, width, height):
        """Центрирует окно на экране"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def to_superscript(self, n):
        superscripts = {
            '0': '⁰', '1': '¹', '2': '²', '3': '³',
            '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷',
            '8': '⁸', '9': '⁹'
        }
        return ''.join(superscripts[digit] for digit in str(n))

    def on_option_change(self, value):
        method_name = self.method_var.get()
        self.second_number_label.config(fg=self.text_color, text="Второе число:")
        self.digit_label.config(fg=self.text_color, text="Цифра:")
        if method_name in ["Сравнение чисел",
                           "Сложение двух чисел",
                           "Вычитание двух чисел",
                           "Умножение двух чисел",
                           "DIV_NN_Dk",
                           "Деление целочисленное",
                           "Деление с остатком",
                           "НОД",
                           "НОК",
                           "Вычитание умноженного на цифру"]:
            self.second_number_label.config(fg=self.backlight, text="Второе число: ✓")
            if method_name == "Вычитание умноженного на цифру":
                self.digit_label.config(fg=self.backlight, text="Цифра: ✓")
        else:
            if method_name in ["Проверка на ноль", "Прибавление единицы"]:
                return
            else:
                self.digit_label.config(fg=self.backlight, text="Цифра: ✓")

    def calculate(self):
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get()
        self._set_result('')

        try:
            first_number = get_Natural(first_number_str)
        except ValueError:
            if first_number_str == '':
                messagebox.showerror("Ошибка", f"Первое число не введено \nВведите натуральное число, например: 123")
            else:
                messagebox.showerror("Ошибка", f"Первое число должно быть натуральным \nВведите натуральное число, например: 123")
            return

        if method_name in ["Сравнение чисел",
                           "Сложение двух чисел",
                           "Вычитание двух чисел",
                           "Умножение двух чисел",
                           "Вычитание умноженного на цифру",
                           "DIV_NN_Dk",
                           "Деление целочисленное",
                           "Деление с остатком",
                           "НОД",
                           "НОК"]:

            second_number_str = self.second_number_entry.get()

            try:
                second_number = get_Natural(second_number_str)
            except ValueError:
                if second_number_str == '':
                    messagebox.showerror("Ошибка", f"Второе число не введено  ( ´•︵•` )\nВведите натуральное число, например: 456")
                else:
                    messagebox.showerror("Ошибка", f"Второе число должно быть натуральным  ( ´•︵•` )\nВведите натуральное число, например: 456")
                return

            if method_name == "Сравнение чисел":
                comparison_result = COM_NN_D_f(first_number, second_number)
                comparison_texts = {
                    2: f"{NNum_to_string(first_number)} > {NNum_to_string(second_number)}",
                    1: f"{NNum_to_string(first_number)} < {NNum_to_string(second_number)}",
                    0: f"{NNum_to_string(first_number)} == {NNum_to_string(second_number)}"
                }
                self._set_result(comparison_texts[comparison_result])

            elif method_name == "Сложение двух чисел":
                result = ADD_NN_N_f(first_number, second_number)
                self._set_result(f"{NNum_to_string(first_number)} + {NNum_to_string(second_number)} = {NNum_to_string(result)}")

            elif method_name == "Вычитание двух чисел":
                try:
                    result = SUB_NN_N_f(first_number, second_number)
                    self._set_result(f"{NNum_to_string(first_number)} - {NNum_to_string(second_number)} = {NNum_to_string(result)}")
                except ValueError:
                    messagebox.showerror("Ошибка", f"Результат должен быть натуральным  ( ´•︵•` )")
                    return

            elif method_name == "Умножение двух чисел":
                result = MUL_NN_N_f(first_number, second_number)
                self._set_result(f"{NNum_to_string(first_number)} ∙ {NNum_to_string(second_number)} = {NNum_to_string(result)}")

            elif method_name == "Вычитание умноженного на цифру":
                digit_str = self.digit_entry.get()
                if not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9  ( ´•︵•` )")
                    return
                digit = int(digit_str)
                try:
                    result = SUB_NDN_N_f(first_number, second_number, digit)
                    self._set_result(f"{NNum_to_string(first_number)} - {NNum_to_string(second_number)}∙{digit} = {NNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", "Результат должен быть натуральным  ( ´•︵•` )")
                    return

            elif method_name == "DIV_NN_Dk":
                k_str = self.digit_entry.get()
                if k_str == '' or not all(c.isdigit() for c in k_str):
                    messagebox.showerror("Ошибка", "k должно быть неотрицательным целым числом  ( ´•︵•` )")
                    return
                k = int(k_str)
                try:
                    digit, power = DIV_NN_Dk_f(first_number, second_number)
                    self._set_result(f"Результат: цифра {digit}, степень 10^{power}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Деление целочисленное":
                try:
                    result = DIV_NN_N_f(first_number, second_number)
                    self._set_result(f"{NNum_to_string(first_number)} div {NNum_to_string(second_number)} = {NNum_to_string(result)}")
                except:
                    messagebox.showerror("Ошибка", f"Нельзя делить на ноль  ( ´•︵•` )")
                    return

            elif method_name == "Деление с остатком":
                try:
                    result = MOD_NN_N_f(first_number, second_number)
                    self._set_result(f"{NNum_to_string(first_number)} mod {NNum_to_string(second_number)} = {NNum_to_string(result)}")
                except:
                    messagebox.showerror("Ошибка", f"Нельзя делить на ноль  ( ´•︵•` )")
                    return

            elif method_name == "НОД":
                result = GCF_NN_N_f(first_number, second_number)
                self._set_result(f"НОД({NNum_to_string(first_number)}; {NNum_to_string(second_number)}) = {NNum_to_string(result)}")

            elif method_name == "НОК":
                result = LCM_NN_N_f(first_number, second_number)
                self._set_result(f"НОК({NNum_to_string(first_number)}; {NNum_to_string(second_number)}) = {NNum_to_string(result)}")

        else:
            if method_name == "Прибавление единицы":
                result = ADD_1N_N_f(first_number)
                self._set_result(f"{NNum_to_string(first_number)} + 1 = {NNum_to_string(result)}")

            elif method_name == "Проверка на ноль":
                is_non_zero = NZER_N_B_f(first_number)
                if is_non_zero == "да":
                    self._set_result(f"{NNum_to_string(first_number)} ≠ 0")
                else:
                    self._set_result(f"{NNum_to_string(first_number)} = 0")

            elif method_name == "Умножение на цифру":
                digit_str = self.digit_entry.get()
                if digit_str == '' or not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9  ( ´•︵•` )")
                    return
                digit = int(digit_str)
                try:
                    result = MUL_ND_N_f(first_number, digit)
                    self._set_result(f"{NNum_to_string(first_number)} ∙ {digit} = {NNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Умножение на 10ⁿ":
                digit_str = self.digit_entry.get()
                try:
                    if is_Natural(digit_str):
                        digit = int(digit_str)
                    else:
                        second_number_str = self.second_number_entry.get()
                        if is_Natural(second_number_str):
                            digit = int(second_number_str)
                        else:
                            messagebox.showerror("Ошибка", "Степень должна быть натуральным числом  ( ´•︵•` )")
                            return
                except ValueError:
                    messagebox.showerror("Ошибка", "Степень должна быть натуральным числом  ( ´•︵•` )")
                    return
                try:
                    result = MUL_Nk_N_f(first_number, digit)
                    self._set_result(f"{NNum_to_string(first_number)} ∙ 10{self.to_superscript(digit)} = {NNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return
    def _set_result(self, text):
        """Устанавливает текст результата в Text виджет"""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)
        self.result_text.config(state=tk.DISABLED)
        # Прокручиваем в начало
        self.result_text.see(1.0)


def create_NaturalApp(root, theme):
    new_root = tk.Toplevel(root)
    app = NaturalApp(new_root, theme=theme)
    return app

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Natural Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = NaturalApp(root, theme=args.theme)
    root.mainloop()

