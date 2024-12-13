import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")  # Kengaytirilgan ekran o'lchami

        self.expression = ""

        # Ekran dizayni
        self.display = ttk.Entry(root, font=("Arial", 20), width=20, justify='right')  # Kattaroq ekran
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        # Butun tugmalarga rang berish uchun Style qo'shildi
        style = ttk.Style()
        style.configure('TButton', padding=10, font=('Arial', 15), background='#D3D3D3')
        style.configure('Operator.TButton', background='#FFA07A')
        style.configure('Number.TButton', background='#58D68D')
        style.configure('Function.TButton', background='#ADD8E6')

        buttons = [
            ('7', 1, 0, 'Number'), ('8', 1, 1, 'Number'), ('9', 1, 2, 'Number'), ('/', 1, 3, 'Operator'),
            ('4', 2, 0, 'Number'), ('5', 2, 1, 'Number'), ('6', 2, 2, 'Number'), ('*', 2, 3, 'Operator'),
            ('1', 3, 0, 'Number'), ('2', 3, 1, 'Number'), ('3', 3, 2, 'Number'), ('-', 3, 3, 'Operator'),
            ('C', 4, 0, 'Function'), ('0', 4, 1, 'Number'), ('=', 4, 2, 'Operator'), ('+', 4, 3, 'Operator'),
            ('<', 5, 0, 'Function'), ('x²', 5, 1, 'Function'), ('√', 5, 2, 'Function'), ('%', 5, 3, 'Function')
        ]

        for (text, row, col, style_name) in buttons:
            button = ttk.Button(self.root, text=text, style=f'{style_name}.TButton',
                                command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

        # Ekranni teng qilish uchun
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "<":
            self.expression = self.expression[:-1]
        elif char == "x²":
            try:
                self.expression = str(eval(self.expression) ** 2)
            except Exception:
                self.expression = "Error"
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif char == "√":
            try:
                self.expression = str(eval(self.expression) ** 0.5)
            except Exception:
                self.expression = "Error"
        elif char == "%":
            try:
                self.expression = str(eval(self.expression) / 100)
            except Exception:
                self.expression = "Error"
        else:
            self.expression += char

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
