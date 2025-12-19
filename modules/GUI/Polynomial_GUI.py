import tkinter as tk
from tkinter import messagebox, font
from modules.GUI.additionally import *
from modules.P.ADD_PP_P import ADD_PP_P_f
from modules.P.SUB_PP_P import SUB_PP_P_f
from modules.P.MUL_PQ_P import MUL_PQ_P_f
from modules.P.MUL_PP_P import MUL_PP_P_f
from modules.P.DIV_PP_P import DIV_PP_P_f
from modules.P.MOD_PP_P import MOD_PP_P_f
from modules.P.DEG_P_N import DEG_P_N_f
from modules.P.DER_P_P import DER_P_P_f
from modules.P.LED_P_Q import LED_P_Q_f
from modules.P.FAC_P_Q import FAC_P_Q_f
from modules.P.GCF_PP_P import GCF_PP_P_f
from modules.P.NMR_P_P import NMR_P_P_f
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f


class PolynomialApp:
    def __init__(self, root, theme='orange'):
        # Оранжевая цветовая схема
        self.bg_color = "#1A1A1A"
        self.window_color = "#2D2D2D"
        self.text_color = "#FFFFFF"
        self.backlight = "#FF6B35"
        self.label_color = "#FFB366"
        self.hover_color = "#FF8C42"
        self.button_color = "#FF6B35"
        self.button_active = "#D45A2A"
        self.entry_bg = "#2D2D2D"
        self.entry_fg = "#FFFFFF"
        self.entry_border = "#FF6B35"
        
        self.root = root
        self.root.title("Операции с многочленами")
        self.root.geometry("500x700")
        self.root.configure(bg=self.bg_color)
        self.center_window(500, 700)

        self.method_var = tk.StringVar(value="Сложение многочленов")

        # Заголовок
        title_font = font.Font(family="Segoe GUI", size=20, weight="bold")
        title_label = tk.Label(root, text="Операции с многочленами", 
                              bg=self.bg_color, fg=self.backlight, font=title_font)
        title_label.pack(pady=(20, 15))

        # Выбор метода
        methods = [
            "Сложение многочленов",
            "Вычитание многочленов",
            "Умножение многочленов",
            "Умножение на дробь",
            "Умножение на xⁿ",
            "Деление многочленов",
            "Остаток от деления",
            "Степень многочлена",
            "Производная многочлена",
            "Старший коэффициент",
            "НОК знаменателей и НОД числителей",
            "НОД многочленов",
            "Преобразование кратных корней",
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=15, padx=20, fill=tk.X)

        label_font = font.Font(family="Segoe GUI", size=11)
        tk.Label(method_frame, text="Операция: ", bg=self.bg_color, fg=self.label_color, font=label_font).pack(side=tk.LEFT, padx=(0, 10))

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg=self.text_color, 
                                highlightbackground=self.button_color,
                                relief=tk.FLAT, activebackground=self.button_color,
                                activeforeground=self.text_color,
                                highlightthickness=2, font=label_font, bd=0)
        self.method_menu.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.method_menu.bind("<Enter>", lambda e: self.method_menu.config(bg=self.hover_color))
        self.method_menu.bind("<Leave>", lambda e: self.method_menu.config(bg=self.window_color))

        # Контейнер для полей ввода
        input_frame = tk.Frame(root, bg=self.bg_color)
        input_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=False)

        # Ввод первого многочлена
        input_font = font.Font(family="Segoe GUI", size=10)
        self.first_polynomial_label = tk.Label(input_frame, text="Первый многочлен:", 
                                               bg=self.bg_color, fg=self.label_color, font=input_font)
        self.first_polynomial_label.pack(anchor=tk.W, pady=(0, 5))
        self.first_polynomial_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                               insertbackground='white', 
                                               font=font.Font(family="Segoe GUI", size=12),
                                               relief=tk.FLAT, bd=2, highlightthickness=1,
                                               highlightbackground=self.entry_border,
                                               highlightcolor=self.backlight)
        self.first_polynomial_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Ввод второго многочлена
        self.second_polynomial_label = tk.Label(input_frame, text="Второй многочлен:", 
                                                bg=self.bg_color, fg=self.text_color, font=input_font)
        self.second_polynomial_label.pack(anchor=tk.W, pady=(0, 5))
        self.second_polynomial_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                                insertbackground='white', 
                                                font=font.Font(family="Segoe GUI", size=12),
                                                relief=tk.FLAT, bd=2, highlightthickness=1,
                                                highlightbackground=self.entry_border,
                                                highlightcolor=self.backlight)
        self.second_polynomial_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Ввод числа
        self.digit_label = tk.Label(input_frame, text="Число:", 
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
                                         font=button_font, relief=tk.FLAT, bd=0,
                                         padx=30, pady=12, cursor="hand2",
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

    def on_option_change(self, value):
        method_name = self.method_var.get()
        self.second_polynomial_label.config(fg=self.text_color, text="Второй многочлен:")
        self.digit_label.config(fg=self.text_color, text="Число:")
        if method_name in ["Сложение многочленов",
                           "Вычитание многочленов",
                           "Умножение многочленов",
                           "Деление многочленов",
                           "Остаток от деления",
                           "НОД многочленов"]:
            self.second_polynomial_label.config(fg=self.backlight, text="Второй многочлен: ✓")
        elif method_name in ["Умножение на дробь",
                             "Умножение на xⁿ"]:
            self.digit_label.config(fg=self.backlight, text="Число: ✓")

    def calculate(self):
        method_name = self.method_var.get()
        first_polynomial_str = self.first_polynomial_entry.get()

        try:
            first_polynomial = get_Polynomial(first_polynomial_str)
        except ValueError as e:
            if first_polynomial_str == '':
                messagebox.showerror("Ошибка", f"Первый многочлен не введен  ( ´•︵•` )")
            else:
                messagebox.showerror("Ошибка", f"Неверный ввод первого многочлена  ( ´•︵•` )\nПример ввода: 3/2 1/4 (коэффициенты через пробел)\nИли: 3x^2 + 2x + 1")
            return

        if method_name in ["Сложение многочленов",
                           "Вычитание многочленов",
                           "Умножение многочленов",
                           "Деление многочленов",
                           "Остаток от деления",
                           "НОД многочленов"]:

            second_polynomial_str = self.second_polynomial_entry.get()
            try:
                second_polynomial = get_Polynomial(second_polynomial_str)
            except ValueError:
                if second_polynomial_str == '':
                    messagebox.showerror("Ошибка", f"Второй многочлен не введен  ( ´•︵•` )")
                else:
                    messagebox.showerror("Ошибка", f"Неверный ввод второго многочлена  ( ´•︵•` )\nПример ввода: 3/2 1/4 (коэффициенты через пробел)\nИли: 3x^2 + 2x + 1")
                return

            if method_name == "Сложение многочленов":
                result = ADD_PP_P_f(first_polynomial, second_polynomial)
                self._set_result(f"Результат: {PNum_to_string(result)}")

            elif method_name == "Вычитание многочленов":
                result = SUB_PP_P_f(first_polynomial, second_polynomial)
                self._set_result(f"Результат: {PNum_to_string(result)}")

            elif method_name == "Умножение многочленов":
                result = MUL_PP_P_f(first_polynomial, second_polynomial)
                self._set_result(f"Результат: {PNum_to_string(result)}")

            elif method_name == "Деление многочленов":
                try:
                    result = DIV_PP_P_f(first_polynomial, second_polynomial)
                    self._set_result(f"Результат: {PNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Остаток от деления":
                try:
                    result = MOD_PP_P_f(first_polynomial, second_polynomial)
                    self._set_result(f"Результат: {PNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "НОД многочленов":
                result = GCF_PP_P_f(first_polynomial, second_polynomial)
                self._set_result(f"Результат: {PNum_to_string(result)}")

        elif method_name in ["Умножение на дробь", "Умножение на xⁿ"]:
            if method_name == "Умножение на дробь":
                number_str = self.digit_entry.get()
                if not is_Rational(number_str):
                    messagebox.showerror("Ошибка", "Число должно быть рациональным  ( ´•︵•` )\nПример: 3/4 или -5/2")
                    return
                try:
                    number = get_Rational(number_str)
                    result = MUL_PQ_P_f(first_polynomial, number)
                    self._set_result(f"Результат: {PNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Умножение на xⁿ":
                k_str = self.digit_entry.get()
                if not is_Natural(k_str):
                    messagebox.showerror("Ошибка", "k должно быть неотрицательным целым числом  ( ´•︵•` )")
                    return
                try:
                    k = int(k_str)
                    result = MUL_Pxk_P_f(first_polynomial, k)
                    self._set_result(f"Результат: {PNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

        else:
            if method_name == "Степень многочлена":
                degree_nnum = DEG_P_N_f(first_polynomial)
                degree_str = NNum_to_string(degree_nnum)
                self._set_result(f"Степень: {degree_str}")

            elif method_name == "Производная многочлена":
                result = DER_P_P_f(first_polynomial)
                self._set_result(f"Результат: {PNum_to_string(result)}")

            elif method_name == "Старший коэффициент":
                result = LED_P_Q_f(first_polynomial)
                self._set_result(f"Результат: {QNum_to_string(result)}")

            elif method_name == "НОК знаменателей и НОД числителей":
                result = FAC_P_Q_f(first_polynomial)
                self._set_result(f"Результат: {QNum_to_string(result)}")

            elif method_name == "Преобразование кратных корней":
                result = NMR_P_P_f(first_polynomial)
                self._set_result(f"Результат: {PNum_to_string(result)}")

    def _set_result(self, text):
        """Устанавливает текст результата в Text виджет"""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)
        self.result_text.config(state=tk.DISABLED)
        # Прокручиваем в начало
        self.result_text.see(1.0)


def create_PolynomialApp(root, theme):
    new_root = tk.Toplevel(root)
    app = PolynomialApp(new_root, theme=theme)
    return app

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Polynomial Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = PolynomialApp(root, theme=args.theme)
    root.mainloop()
