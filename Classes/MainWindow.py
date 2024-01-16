from tkinter import ttk
from functions import *

# Словарь
#   Ключи: названия цветов
#   Значения: коды цветов в шестнадцатеричном формате
COLORS: dict[str, str] = {
	'red': '#ff0000',
	'orange': '#ff7d00',
	'yellow': '#ffff00',
	'green': '#00ff00',
	'light_blue': '#007dff',
	'blue': '#0000ff',
	'purple': '#7d00ff'
}


class MainWindow:
	def __init__(self):
		# Создание и конфигурирование окна
		self.window: tk.Tk = tk.Tk()
		self.window.title('Rainbow')
		self.window.geometry('250x500')
		self.window.resizable(width = False, height = False)
		self.window.config(
			padx = 50,
			pady = 50
		)

		# Создание переменных для хранения виджетов
		self.label: ttk.Label = ttk.Label(master = self.window)
		self.entry: ttk.Entry = ttk.Entry(master = self.window)
		self.buttons: list[tk.Button] = []

		self.place_widgets()  # Создание и размещение виджетов
		self.set_listeners()  # Установление обработчиков событий

		# Главный цикл окна
		self.window.mainloop()

	# Метод для создания и размещение виджетов
	def place_widgets(self) -> 'MainWindow':
		# Создание и размещение виджета Label
		self.label.config(
			font = ('Arial', 10),
			justify = 'center'
		)
		self.label.pack()

		# Создание и размещение виджета Entry
		self.entry.config(
			justify = 'center',
			font = ('Arial', 10),
			width = 100,
		)
		self.entry.pack()

		# Создание и размещение кнопок
		for key, value in COLORS.items():
			self.buttons.append(tk.Button(
				master = self.window,
				bg = value,
				width = 100
			))
			self.buttons[-1].pack()

		return self

	# Метод для установление обработчиков событий
	def set_listeners(self) -> 'MainWindow':
		for button in self.buttons:
			# Обработчик события
			#   Событие: нажание левой кнопки мыши
			#   Обработчик: метод self.button_clicked
			button.bind(
				sequence = '<Button-1>',  # Событие
				func = self.button_clicked  # Обработчик
			)

		return self

	# Метод для обработки нажатия левой кнопки мыши по кнопке
	def button_clicked(self, event: tk.Event) -> None:
		button_color: str = event.widget['bg']

		self.entry.delete(0, tk.END)
		self.entry.insert(0, button_color.upper())

		self.label['text'] = f'COLOR: {transpose_dict(COLORS)[button_color].upper()}'
