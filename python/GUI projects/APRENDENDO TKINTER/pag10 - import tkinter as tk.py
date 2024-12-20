import tkinter as tk

window = tk.Tk()
window.title("TKINTER")
valor = tk.IntVar()
radio1 = tk.Radiobutton(
    window,
    text = "Higino",
    variable = valor,
    command = lambda: print(valor.get()),
    value = 2
)
radio1.pack()
radio2 = tk.Radiobutton(
    window,
    text = "Higino",
    command = lambda: print(valor.get()),
    variable = valor,
    value = 0
)
radio2.pack()
radio3 = tk.Radiobutton(
    window,
    text = "Higino",
    command = lambda: print(valor.get()),
    variable = valor,
    value = 3
)
radio3.pack()
window.mainloop()