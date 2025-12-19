from modules.GUI.Natural_GUI import create_NaturalApp
from modules.GUI.Integer_GUI import create_IntegerApp
from modules.GUI.Rational_GUI import create_RationalApp
from modules.GUI.Polynomial_GUI import create_PolynomialApp
from modules.GUI.Quaternion_GUI import create_QuaternionApp
import tkinter as tk
from tkinter import font


class App:
    def __init__(self, root):
        # Оранжевая цветовая схема
        self.orange_theme = {
            "bg": "#1A1A1A",  # Темный фон
            "title": "#FF6B35",  # Яркий оранжевый для заголовка
            "subtitle": "#FFB366",  # Светлый оранжевый
            "button_bg": "#FF6B35",  # Оранжевые кнопки
            "button_fg": "#FFFFFF",  # Белый текст
            "button_hover": "#FF8C42",  # Светлее при наведении
            "button_active": "#D45A2A",  # Темнее при нажатии
            "border": "#FF8C42",  # Оранжевая рамка
            "accent": "#FFB366"  # Акцентный цвет
        }

        self.current_theme = self.orange_theme

        # Определяем разрешение экрана и масштаб
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Для Full HD (1920x1080) уменьшаем на 20%, для 2560x1600 оставляем как есть
        if screen_width == 1920 and screen_height == 1080:
            self.scale = 0.8  # Уменьшение на 20%
        else:
            self.scale = 1.0  # Оригинальный размер
        
        # Базовые размеры
        base_window_size = 650
        base_title_size = 28
        base_subtitle_size = 11
        base_button_size = 13
        base_hint_size = 9
        base_padx = 70
        base_pady_header = (30, 20)
        base_pady_subtitle = (5, 0)
        base_pady_container = 10
        base_pady_footer = 10
        base_button_pady = 8
        base_button_padx = 5
        base_button_padx_inner = 30
        base_button_pady_inner = 13
        base_button_ipady = 11
        
        # Применяем масштаб
        self.window_size = int(base_window_size * self.scale)
        self.title_size = int(base_title_size * self.scale)
        self.subtitle_size = int(base_subtitle_size * self.scale)
        self.button_size = int(base_button_size * self.scale)
        self.hint_size = int(base_hint_size * self.scale)
        self.padx = int(base_padx * self.scale)
        self.pady_header = (int(base_pady_header[0] * self.scale), int(base_pady_header[1] * self.scale))
        self.pady_subtitle = (int(base_pady_subtitle[0] * self.scale), int(base_pady_subtitle[1] * self.scale))
        self.pady_container = int(base_pady_container * self.scale)
        self.pady_footer = int(base_pady_footer * self.scale)
        self.button_pady = int(base_button_pady * self.scale)
        self.button_padx = int(base_button_padx * self.scale)
        self.button_padx_inner = int(base_button_padx_inner * self.scale)
        self.button_pady_inner = int(base_button_pady_inner * self.scale)
        self.button_ipady = int(base_button_ipady * self.scale)

        # Создание окна
        self.root = root
        self.root.title("Калькулятор модулей")
        self.root.geometry(f"{self.window_size}x{self.window_size}")
        self.root.configure(bg=self.current_theme["bg"])
        self.root.resizable(False, False)
        
        # Центрируем окно
        self.center_window(self.window_size, self.window_size)

        # Создаем стильный заголовок
        header_frame = tk.Frame(root, bg=self.current_theme["bg"])
        header_frame.pack(pady=self.pady_header, fill=tk.X)
        
        # Главный заголовок
        title_font = font.Font(family="Segoe GUI", size=self.title_size, weight="bold")
        self.title_label = tk.Label(header_frame, text="Калькулятор модулей", 
                                     bg=self.current_theme["bg"],
                                     fg=self.current_theme["title"], 
                                     font=title_font)
        self.title_label.pack()
        
        # Подзаголовок
        subtitle_font = font.Font(family="Segoe GUI", size=self.subtitle_size)
        subtitle_label = tk.Label(header_frame, text="Выберите модуль для работы", 
                                  bg=self.current_theme["bg"],
                                  fg=self.current_theme["subtitle"], 
                                  font=subtitle_font)
        subtitle_label.pack(pady=self.pady_subtitle)

        # Основной контейнер для кнопок
        main_container = tk.Frame(root, bg=self.current_theme["bg"])
        main_container.pack(fill=tk.BOTH, expand=True, padx=self.padx, pady=self.pady_container)
        
        # Контейнер для кнопок (центрируем)
        buttons_frame = tk.Frame(main_container, bg=self.current_theme["bg"])
        buttons_frame.pack(expand=True)

        
        button_font = font.Font(family="Segoe GUI", size=self.button_size, weight="normal")
        
        
        btn_natural = self.create_button(buttons_frame, "🔢 Натуральные числа", self.run_file1, button_font)
        btn_integer = self.create_button(buttons_frame, "🔷 Целые числа", self.run_file2, button_font)
        btn_rational = self.create_button(buttons_frame, "➗ Рациональные числа", self.run_file3, button_font)
        btn_polynomial = self.create_button(buttons_frame, "📊 Многочлены", self.run_file4, button_font)
        btn_quaternion = self.create_button(buttons_frame, "🌀 Кватернионы", self.run_file5, button_font)
        
        # Добавляем подсказку внизу окна
        footer_frame = tk.Frame(root, bg=self.current_theme["bg"])
        footer_frame.pack(side=tk.BOTTOM, pady=self.pady_footer)
        
        hint_font = font.Font(family="Segoe GUI", size=self.hint_size)
        hint_label = tk.Label(footer_frame, text="Доступно 5 разделов",
                             bg=self.current_theme["bg"],
                             fg=self.current_theme["subtitle"],
                             font=hint_font)
        hint_label.pack()

    def center_window(self, width, height):
        """Центрирует окно на экране"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = max(0, (screen_width - width) // 2)
        y = max(0, (screen_height - height) // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_button(self, parent, text, command, font_style):
        """Создает стильную кнопку с эффектами"""
        # Фрейм для кнопки с отступами
        button_frame = tk.Frame(parent, bg=self.current_theme["bg"])
        button_frame.pack(pady=self.button_pady, fill=tk.X, padx=self.button_padx)
        
        button = tk.Button(button_frame, 
                          text=text,
                          command=command,
                          bg=self.current_theme["button_bg"],
                          fg=self.current_theme["button_fg"],
                          font=font_style,
                          relief=tk.FLAT,
                          bd=0,
                          padx=self.button_padx_inner,
                          pady=self.button_pady_inner,
                          cursor="hand2",
                          activebackground=self.current_theme["button_active"],
                          activeforeground=self.current_theme["button_fg"],
                          anchor=tk.CENTER,
                          justify=tk.CENTER)
        
        button.pack(fill=tk.X, ipady=self.button_ipady)
        
        # Эффекты при наведении
        def on_enter(e):
            button.config(bg=self.current_theme["button_hover"])
            button.config(relief=tk.RAISED, bd=2)
        
        def on_leave(e):
            button.config(bg=self.current_theme["button_bg"])
            button.config(relief=tk.FLAT, bd=0)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button

    def run_file1(self):
        window = create_NaturalApp(root, 'orange')

    def run_file2(self):
        window = create_IntegerApp(root, 'orange')

    def run_file3(self):
        window = create_RationalApp(root, 'orange')

    def run_file4(self):
        window = create_PolynomialApp(root, 'orange')

    def run_file5(self):
        window = create_QuaternionApp(root, 'orange')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

