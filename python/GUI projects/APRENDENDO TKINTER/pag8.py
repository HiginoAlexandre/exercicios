import tkinter as tk

window = tk.Tk()
window.title("Variáveis do tkinter")
texto = tk.StringVar()
label = tk.Label(window, text = "higino", textvariable= texto)
label.pack()
entry = tk.Entry(window, textvariable=texto)
entry.pack()

window.mainloop()