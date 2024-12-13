import tkinter as tk

# Ekranni yaratish
root = tk.Tk()
root.title("Kalkulyator")
root.geometry("400x600")
root.resizable(False, False)

# Ekranga kirish va natija chiqarish uchun oynacha
entry = tk.Entry(root, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Tugmachalar uchun funksiyalar
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_operation(op):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + op)

# Tugmachalarni yaratish va ekranga joylashtirish
button_params = {'padx': 20, 'pady': 20, 'font': ('Arial', 18)}

# Tugmachalarni tartibga solish uchun grid konfiguratsiyasi
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for j in range(6):
    root.grid_rowconfigure(j, weight=1)

# Tugmachalar qatori 1
tk.Button(root, text='7', command=lambda: button_click('7'), **button_params).grid(row=1, column=0, sticky="nsew")
tk.Button(root, text='8', command=lambda: button_click('8'), **button_params).grid(row=1, column=1, sticky="nsew")
tk.Button(root, text='9', command=lambda: button_click('9'), **button_params).grid(row=1, column=2, sticky="nsew")
tk.Button(root, text='/', command=lambda: button_operation('/'), **button_params).grid(row=1, column=3, sticky="nsew")

# Tugmachalar qatori 2
tk.Button(root, text='4', command=lambda: button_click('4'), **button_params).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text='5', command=lambda: button_click('5'), **button_params).grid(row=2, column=1, sticky="nsew")
tk.Button(root, text='6', command=lambda: button_click('6'), **button_params).grid(row=2, column=2, sticky="nsew")
tk.Button(root, text='*', command=lambda: button_operation('*'), **button_params).grid(row=2, column=3, sticky="nsew")

# Tugmachalar qatori 3
tk.Button(root, text='1', command=lambda: button_click('1'), **button_params).grid(row=3, column=0, sticky="nsew")
tk.Button(root, text='2', command=lambda: button_click('2'), **button_params).grid(row=3, column=1, sticky="nsew")
tk.Button(root, text='3', command=lambda: button_click('3'), **button_params).grid(row=3, column=2, sticky="nsew")
tk.Button(root, text='-', command=lambda: button_operation('-'), **button_params).grid(row=3, column=3, sticky="nsew")

# Tugmachalar qatori 4
tk.Button(root, text='0', command=lambda: button_click('0'), **button_params).grid(row=4, column=0, sticky="nsew")
tk.Button(root, text='.', command=lambda: button_click('.'), **button_params).grid(row=4, column=1, sticky="nsew")
tk.Button(root, text='+', command=lambda: button_operation('+'), **button_params).grid(row=4, column=2, sticky="nsew")
tk.Button(root, text='=', command=button_equal, **button_params).grid(row=4, column=3, sticky="nsew")

# Tozalash tugmasi qatori
tk.Button(root, text='C', command=button_clear, **button_params).grid(row=5, column=0, columnspan=4, sticky='nsew')

# Ilovani ishga tushirish
root.mainloop()
