import tkinter as tk
from tkinter import messagebox, font
from modules.GUI.additionally import *
from modules.H.ADD_HH_H import ADD_HH_H_f
from modules.H.SUB_HH_H import SUB_HH_H_f
from modules.H.MUL_HH_H import MUL_HH_H_f
from modules.H.DIV_HQ_H import DIV_HQ_H_f
from modules.H.MUL_QH_H import MUL_QH_H_f
from modules.H.NEG_H import NEG_H_f
from modules.H.CON_H import CON_H_f
from modules.H.INV_H import INV_H_f
from modules.H.NORML_H import NORML_H_f
from modules.H.NORM_H_Q import NORM_H_Q_f
from modules.H.SCAL_HH_Q import SCAL_HH_Q_f
from modules.H.COS_HH_Q import COS_HH_Q_f
from modules.H.MUL_RI_HH_H import MUL_RI_HH_H_f
from modules.H.ROT_Q_H import ROT_Q_H_f
from modules.H.DEF_H import DEF_H_f


class QuaternionApp:
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
        self.root.title("Операции над кватернионами")
        self.root.geometry("500x750")
        self.root.configure(bg=self.bg_color)
        self.center_window(500, 750)

        self.method_var = tk.StringVar(value="Сложение кватернионов")

        # Заголовок
        title_font = font.Font(family="Segoe GUI", size=20, weight="bold")
        title_label = tk.Label(root, text="Операции над кватернионами", 
                              bg=self.bg_color, fg=self.backlight, font=title_font)
        title_label.pack(pady=(20, 15))

        # Выбор метода
        methods = [
            "Сложение кватернионов",
            "Вычитание кватернионов",
            "Умножение кватернионов",
            "Деление кватерниона на число",
            "Умножение числа на кватернион",
            "Смена знака",
            "Сопряжённый кватернион",
            "Обратный кватернион",
            "Нормализация",
            "Норма кватерниона",
            "Скалярное произведение",
            "Косинус угла",
            "Умножение Re × Im",
            "Кватернион поворота",
            "Дефолтный кватернион (чистый)"
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

        # Ввод первого кватерниона
        input_font = font.Font(family="Segoe GUI", size=10)
        self.first_quaternion_label = tk.Label(input_frame, text="Первый кватернион (формат: s x y z, например: 1/1 2/3 -1/2 5/1):", 
                                               bg=self.bg_color, fg=self.label_color, font=input_font)
        self.first_quaternion_label.pack(anchor=tk.W, pady=(0, 5))
        self.first_quaternion_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                               insertbackground='white', 
                                               font=font.Font(family="Segoe GUI", size=12),
                                               relief=tk.FLAT, bd=2, highlightthickness=1,
                                               highlightbackground=self.entry_border,
                                               highlightcolor=self.backlight)
        self.first_quaternion_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Ввод второго кватерниона / рационального числа / угла
        self.second_input_label = tk.Label(input_frame, text="Второй кватернион:", 
                                            bg=self.bg_color, fg=self.text_color, font=input_font)
        self.second_input_label.pack(anchor=tk.W, pady=(0, 5))
        self.second_input_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                            insertbackground='white', 
                                            font=font.Font(family="Segoe GUI", size=12),
                                            relief=tk.FLAT, bd=2, highlightthickness=1,
                                            highlightbackground=self.entry_border,
                                            highlightcolor=self.backlight)
        self.second_input_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)


        # Фрейм для результата с прокруткой
        result_frame = tk.Frame(input_frame, bg=self.bg_color)
        result_frame.pack(pady=10, fill=tk.BOTH, expand=False)

        # Скроллбар
        result_scrollbar = tk.Scrollbar(result_frame, bg=self.window_color, troughcolor=self.bg_color)
        result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text виджет вместо Label
        result_font = font.Font(family="Segoe GUI", size=12, weight="bold")
        self.result_text = tk.Text(result_frame, bg=self.entry_bg, fg=self.backlight,
                                   font=result_font, wrap=tk.WORD,
                                   height=6, relief=tk.FLAT, bd=2,
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
        
        # Сбрасываем все подсветки
        self.first_quaternion_label.config(fg=self.text_color)
        self.second_input_label.config(fg=self.text_color)
        
        # Операции с двумя кватернионами (H + H → H)
        if method_name in ["Сложение кватернионов",
                          "Вычитание кватернионов",
                          "Умножение кватернионов",
                          "Скалярное произведение",
                          "Косинус угла",
                          "Умножение Re × Im"]:
            self.first_quaternion_label.config(fg=self.backlight, text="Первый кватернион (формат: s x y z, например: 1/1 2/3 -1/2 5/1): ✓")
            self.second_input_label.config(fg=self.backlight, text="Второй кватернион: ✓")
            # Показываем второе поле, если скрыто
            if not self._is_packed(self.second_input_label):
                self.second_input_label.pack(anchor=tk.W, pady=(0, 5))
            if not self._is_packed(self.second_input_entry):
                self.second_input_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)
            # Показываем первое поле, если скрыто
            if not self._is_packed(self.first_quaternion_label):
                self.first_quaternion_label.pack(anchor=tk.W, pady=(0, 5))
            if not self._is_packed(self.first_quaternion_entry):
                self.first_quaternion_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)
        
        # Операции с кватернионом и рациональным числом
        elif method_name in ["Деление кватерниона на число",
                            "Умножение числа на кватернион"]:
            self.first_quaternion_label.config(fg=self.backlight, text="Кватернион (формат: s x y z, например: 1/1 2/3 -1/2 5/1): ✓")
            self.second_input_label.config(fg=self.backlight, text="Рациональное число (например: 3/4): ✓")
            # Показываем все поля
            if not self._is_packed(self.first_quaternion_label):
                self.first_quaternion_label.pack(anchor=tk.W, pady=(0, 5))
            if not self._is_packed(self.first_quaternion_entry):
                self.first_quaternion_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)
            if not self._is_packed(self.second_input_label):
                self.second_input_label.pack(anchor=tk.W, pady=(0, 5))
            if not self._is_packed(self.second_input_entry):
                self.second_input_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)
        
        # Унарные операции с кватернионом (H → H или H → Q)
        elif method_name in ["Смена знака",
                            "Сопряжённый кватернион",
                            "Обратный кватернион",
                            "Нормализация",
                            "Норма кватерниона"]:
            self.first_quaternion_label.config(fg=self.backlight, text="Кватернион (формат: s x y z, например: 1/1 2/3 -1/2 5/1): ✓")
            # Показываем первое поле
            if not self._is_packed(self.first_quaternion_label):
                self.first_quaternion_label.pack(anchor=tk.W, pady=(0, 5))
            if not self._is_packed(self.first_quaternion_entry):
                self.first_quaternion_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)
            # Скрываем второе поле
            if self._is_packed(self.second_input_label):
                self.second_input_label.pack_forget()
            if self._is_packed(self.second_input_entry):
                self.second_input_entry.pack_forget()
        
        # Кватернион поворота (Q, H → H)
        elif method_name == "Кватернион поворота":
            self.first_quaternion_label.config(fg=self.backlight, text="Угол в радианах (рациональное число, например: 3/4): ✓")
            self.second_input_label.config(fg=self.backlight, text="Ось вращения (кватернион, например: 0/1 1/1 0/1 0/1): ✓")
            # Показываем все поля
            if not self._is_packed(self.first_quaternion_label):
                self.first_quaternion_label.pack(anchor=tk.W, pady=(0, 5))
            if not self._is_packed(self.first_quaternion_entry):
                self.first_quaternion_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)
            if not self._is_packed(self.second_input_label):
                self.second_input_label.pack(anchor=tk.W, pady=(0, 5))
            if not self._is_packed(self.second_input_entry):
                self.second_input_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)
        
        # Дефолтный кватернион (ничего не требует)
        elif method_name == "Дефолтный кватернион":
            # Скрываем все поля
            if self._is_packed(self.first_quaternion_label):
                self.first_quaternion_label.pack_forget()
            if self._is_packed(self.first_quaternion_entry):
                self.first_quaternion_entry.pack_forget()
            if self._is_packed(self.second_input_label):
                self.second_input_label.pack_forget()
            if self._is_packed(self.second_input_entry):
                self.second_input_entry.pack_forget()
    
    def _is_packed(self, widget):
        """Проверяет, упакован ли виджет"""
        try:
            widget.pack_info()
            return True
        except:
            return False

    def calculate(self):
        method_name = self.method_var.get()
        self._set_result('')

        try:
            if method_name == "Дефолтный кватернион":
                result = DEF_H_f()
                self._set_result(f"Результат: {HNum_to_string(result)}")
                return

            # Операции с двумя кватернионами (H + H → H)
            if method_name in ["Сложение кватернионов",
                              "Вычитание кватернионов",
                              "Умножение кватернионов",
                              "Скалярное произведение",
                              "Косинус угла",
                              "Умножение Re × Im"]:
                first_str = self.first_quaternion_entry.get()
                second_str = self.second_input_entry.get()

                try:
                    first_quat = get_Quaternion(first_str)
                except ValueError:
                    if first_str == '':
                        messagebox.showerror("Ошибка", "Первый кватернион не введен ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    else:
                        messagebox.showerror("Ошибка", "Неверный формат первого кватерниона ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    return

                try:
                    second_quat = get_Quaternion(second_str)
                except ValueError:
                    if second_str == '':
                        messagebox.showerror("Ошибка", "Второй кватернион не введен ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    else:
                        messagebox.showerror("Ошибка", "Неверный формат второго кватерниона ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    return

                if method_name == "Сложение кватернионов":
                    result = ADD_HH_H_f(first_quat, second_quat)
                    self._set_result(f"({HNum_to_string(first_quat)}) + ({HNum_to_string(second_quat)}) = {HNum_to_string(result)}")

                elif method_name == "Вычитание кватернионов":
                    result = SUB_HH_H_f(first_quat, second_quat)
                    self._set_result(f"({HNum_to_string(first_quat)}) - ({HNum_to_string(second_quat)}) = {HNum_to_string(result)}")

                elif method_name == "Умножение кватернионов":
                    result = MUL_HH_H_f(first_quat, second_quat)
                    self._set_result(f"({HNum_to_string(first_quat)}) ∙ ({HNum_to_string(second_quat)}) = {HNum_to_string(result)}")

                elif method_name == "Скалярное произведение":
                    result = SCAL_HH_Q_f(first_quat, second_quat)
                    self._set_result(f"scal({HNum_to_string(first_quat)}, {HNum_to_string(second_quat)}) = {QNum_to_string(result)}")

                elif method_name == "Косинус угла":
                    try:
                        result = COS_HH_Q_f(first_quat, second_quat)
                        self._set_result(f"cos(∠({HNum_to_string(first_quat)}, {HNum_to_string(second_quat)})) = {QNum_to_string(result)}")
                    except ValueError as e:
                        messagebox.showerror("Ошибка", f"Ошибка вычисления ( ´•︵•` )\n{str(e)}")
                        return

                elif method_name == "Умножение Re × Im":
                    result = MUL_RI_HH_H_f(first_quat, second_quat)
                    self._set_result(f"Re({HNum_to_string(first_quat)}) × Im({HNum_to_string(second_quat)}) = {HNum_to_string(result)}")

            # Операции с кватернионом и рациональным числом
            elif method_name in ["Деление кватерниона на число",
                                "Умножение числа на кватернион"]:
                first_str = self.first_quaternion_entry.get()
                second_str = self.second_input_entry.get()

                try:
                    first_quat = get_Quaternion(first_str)
                except ValueError:
                    if first_str == '':
                        messagebox.showerror("Ошибка", "Кватернион не введен ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    else:
                        messagebox.showerror("Ошибка", "Неверный формат кватерниона ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    return

                try:
                    rational = get_Rational(second_str)
                except ValueError:
                    if second_str == '':
                        messagebox.showerror("Ошибка", "Рациональное число не введено ( ´•︵•` )\nПример: 3/4")
                    else:
                        messagebox.showerror("Ошибка", "Неверный формат рационального числа ( ´•︵•` )\nПример: 3/4")
                    return

                if method_name == "Деление кватерниона на число":
                    try:
                        result = DIV_HQ_H_f(first_quat, rational)
                        self._set_result(f"({HNum_to_string(first_quat)}) / ({QNum_to_string(rational)}) = {HNum_to_string(result)}")
                    except ValueError:
                        messagebox.showerror("Ошибка", "Нельзя делить на ноль ( ´•︵•` )")
                        return

                elif method_name == "Умножение числа на кватернион":
                    result = MUL_QH_H_f(rational, first_quat)
                    self._set_result(f"{QNum_to_string(rational)} ∙ ({HNum_to_string(first_quat)}) = {HNum_to_string(result)}")

            # Унарные операции с кватернионом
            elif method_name in ["Смена знака",
                                "Сопряжённый кватернион",
                                "Обратный кватернион",
                                "Нормализация",
                                "Норма кватерниона"]:
                first_str = self.first_quaternion_entry.get()

                try:
                    quat = get_Quaternion(first_str)
                except ValueError:
                    if first_str == '':
                        messagebox.showerror("Ошибка", "Кватернион не введен ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    else:
                        messagebox.showerror("Ошибка", "Неверный формат кватерниона ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    return

                if method_name == "Смена знака":
                    result = NEG_H_f(quat)
                    self._set_result(f"-({HNum_to_string(quat)}) = {HNum_to_string(result)}")

                elif method_name == "Сопряжённый кватернион":
                    result = CON_H_f(quat)
                    self._set_result(f"conj({HNum_to_string(quat)}) = {HNum_to_string(result)}")

                elif method_name == "Обратный кватернион":
                    try:
                        result = INV_H_f(quat)
                        self._set_result(f"inv({HNum_to_string(quat)}) = {HNum_to_string(result)}")
                    except ValueError:
                        messagebox.showerror("Ошибка", "Норма кватерниона равна нулю, обратный не существует ( ´•︵•` )")
                        return

                elif method_name == "Нормализация":
                    try:
                        result = NORML_H_f(quat)
                        self._set_result(f"normalize({HNum_to_string(quat)}) = {HNum_to_string(result)}")
                    except ValueError:
                        messagebox.showerror("Ошибка", "Норма кватерниона равна нулю, нормализация невозможна ( ´•︵•` )")
                        return

                elif method_name == "Норма кватерниона":
                    try:
                        result = NORM_H_Q_f(quat)
                        self._set_result(f"norm({HNum_to_string(quat)}) = {QNum_to_string(result)}")
                    except ValueError:
                        messagebox.showerror("Ошибка", "Ошибка вычисления нормы ( ´•︵•` )")
                        return

            # Кватернион поворота
            elif method_name == "Кватернион поворота":
                angle_str = self.first_quaternion_entry.get()
                axis_str = self.second_input_entry.get()

                try:
                    angle = get_Rational(angle_str)
                except ValueError:
                    if angle_str == '':
                        messagebox.showerror("Ошибка", "Угол не введен ( ´•︵•` )\nПример: 3/4")
                    else:
                        messagebox.showerror("Ошибка", "Неверный формат угла ( ´•︵•` )\nПример: 3/4")
                    return

                try:
                    axis = get_Quaternion(axis_str)
                except ValueError:
                    if axis_str == '':
                        messagebox.showerror("Ошибка", "Ось вращения не введена ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    else:
                        messagebox.showerror("Ошибка", "Неверный формат оси вращения ( ´•︵•` )\nПример: 1/1 2/3 -1/2 5/1")
                    return

                try:
                    result = ROT_Q_H_f(angle, axis)
                    self._set_result(f"rot({QNum_to_string(angle)}, {HNum_to_string(axis)}) = {HNum_to_string(result)}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"Ошибка вычисления ( ´•︵•` )\n{str(e)}")
                    return

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка ( ´•︵•` )\n{str(e)}")
            return

    def _set_result(self, text):
        """Устанавливает текст результата в Text виджет"""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)
        self.result_text.config(state=tk.DISABLED)
        # Прокручиваем в начало
        self.result_text.see(1.0)


def create_QuaternionApp(root, theme):
    new_root = tk.Toplevel(root)
    app = QuaternionApp(new_root, theme=theme)
    return app

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Quaternion Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = QuaternionApp(root, theme=args.theme)
    root.mainloop()

