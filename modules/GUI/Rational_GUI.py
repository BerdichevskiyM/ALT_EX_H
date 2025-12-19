import tkinter as tk
from tkinter import messagebox, font
from modules.GUI.additionally import *
from modules.Q.RED_Q_Q import RED_Q_Q_f
from modules.Q.INT_Q_B import INT_Q_B_f
from modules.Q.TRANS_Z_Q import TRANS_Z_Q_f
from modules.Q.TRANS_Q_Z import TRANS_Q_Z_f
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f


class RationalApp:
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
        self.root.title("Операции с рациональными числами")
        self.root.geometry("450x650")
        self.root.configure(bg=self.bg_color)
        self.center_window(450, 650)

        self.method_var = tk.StringVar(value="Сложение дробей")

        # Заголовок
        title_font = font.Font(family="Segoe GUI", size=20, weight="bold")
        title_label = tk.Label(root, text="Операции с рациональными", 
                              bg=self.bg_color, fg=self.backlight, font=title_font)
        title_label.pack(pady=(20, 15))

        # Выбор метода
        methods = [
            "Сокращение дроби",
            "Проверка на целое",
            "Целое -> дробное",
            "Дробное -> целое",
            "Сложение дробей",
            "Вычитание дробей",
            "Умножение дробей",
            "Деление дробей",
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

        # Ввод первого числа
        input_font = font.Font(family="Segoe GUI", size=10)
        self.first_number_label = tk.Label(input_frame, text="Первая дробь:", 
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
        self.second_number_label = tk.Label(input_frame, text="Вторая дробь:", 
                                            bg=self.bg_color, fg=self.text_color, font=input_font)
        self.second_number_label.pack(anchor=tk.W, pady=(0, 5))
        self.second_number_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                            insertbackground='white', 
                                            font=font.Font(family="Segoe GUI", size=12),
                                            relief=tk.FLAT, bd=2, highlightthickness=1,
                                            highlightbackground=self.entry_border,
                                            highlightcolor=self.backlight)
        self.second_number_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

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
        if method_name in ["Сложение дробей",
                           "Вычитание дробей",
                           "Умножение дробей",
                           "Деление дробей"]:
            self.second_number_label.config(fg=self.backlight, text="Вторая дробь: ✓")
        else:
            self.second_number_label.config(fg=self.text_color, text="Вторая дробь:")

    def calculate(self):
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get()
        try:
            first_number = get_Rational(first_number_str)
        except ValueError:
            if first_number_str == '':
                messagebox.showerror("Ошибка", f"Первое число не введено  ( ´•︵•` )\nПример: -3/4")
            else:
                messagebox.showerror("Ошибка", f"Первое число должно быть рациональным  ( ´•︵•` )\nПример: -3/4")
            return

        if method_name in ["Сложение дробей",
                           "Вычитание дробей",
                           "Умножение дробей",
                           "Деление дробей"]:
            second_number_str = self.second_number_entry.get()
            try:
                second_number = get_Rational(second_number_str)
            except ValueError:
                if second_number_str == '':
                    messagebox.showerror("Ошибка", f"Второе число не введено  ( ´•︵•` )\nПример: -3/4")
                else:
                    messagebox.showerror("Ошибка", f"Второе число должно быть рациональным  ( ´•︵•` )\nПример: -3/4")
                return

            if method_name == "Сложение дробей":
                result = ADD_QQ_Q_f(first_number, second_number)
                if len(second_number_str) > 0 and second_number_str[0] == '-':
                    self._set_result(f"{QNum_to_string(first_number)} - {second_number_str[1:]} = {QNum_to_string(result)}")
                else:
                    self._set_result(f"{QNum_to_string(first_number)} + {QNum_to_string(second_number)} = {QNum_to_string(result)}")

            elif method_name == "Вычитание дробей":
                result = SUB_QQ_Q_f(first_number, second_number)
                if len(second_number_str) > 0 and second_number_str[0] == '-':
                    self._set_result(f"{QNum_to_string(first_number)} + {second_number_str[1:]} = {QNum_to_string(result)}")
                else:
                    self._set_result(f"{QNum_to_string(first_number)} - {QNum_to_string(second_number)} = {QNum_to_string(result)}")

            elif method_name == "Умножение дробей":
                result = MUL_QQ_Q_f(first_number, second_number)
                self._set_result(f"{QNum_to_string(first_number)} ∙ {QNum_to_string(second_number)} = {QNum_to_string(result)}")

            elif method_name == "Деление дробей":
                try:
                    result = DIV_QQ_Q_f(first_number, second_number)
                    self._set_result(f"{QNum_to_string(first_number)} ∶ {QNum_to_string(second_number)} = {QNum_to_string(result)}")
                except ValueError:
                    messagebox.showerror("Ошибка", f"Нельзя делить на ноль  ( ´•︵•` )")
                    return

        elif method_name == "Сокращение дроби":
            result = RED_Q_Q_f(first_number)
            self._set_result(f"{QNum_to_string(first_number)} = {QNum_to_string(result)}")

        elif method_name == "Проверка на целое":
            result = INT_Q_B_f(first_number)
            if result == 'да':
                self._set_result(f"Является целым")
            else:
                self._set_result(f"Не является целым")

        elif method_name == "Целое -> дробное":
            try:
                first_number = get_Integer(first_number_str)
            except ValueError:
                messagebox.showerror("Ошибка", "Первое число должно быть целым  ( ´•︵•` )")
                return
            result = TRANS_Z_Q_f(first_number)
            self._set_result(f"Результат: {QNum_to_string(result)}")

        elif method_name == "Дробное -> целое":
            try:
                result = TRANS_Q_Z_f(first_number)
                self._set_result(f"Результат: {ZNum_to_string(result)}")
            except ValueError:
                messagebox.showerror("Ошибка", "Знаменатель не равен 1  ( ´•︵•` )")
                return

    def _set_result(self, text):
        """Устанавливает текст результата в Text виджет"""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)
        self.result_text.config(state=tk.DISABLED)
        # Прокручиваем в начало
        self.result_text.see(1.0)



def create_RationalApp(root, theme):
    new_root = tk.Toplevel(root)
    app = RationalApp(new_root, theme=theme)
    return app

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Rational Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = RationalApp(root, theme=args.theme)
    root.mainloop()
