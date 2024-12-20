import tkinter as tk
from tkinter import messagebox
def packall(*widgets):
    for i in widgets:
        i.pack()

window = tk.Tk()
window.title("tkinter testes")
dinamica = tk.StringVar()
label = tk.Label(window, text = "Higino Alexandre", textvariable= dinamica)
entry = tk.Entry(window, textvariable=dinamica)
button = tk.Button(window, text = "mundar dinamico para'gino'", command= lambda: dinamica.set("gino"))
check_var = tk.IntVar(value=1)
checkbutton  = tk.Checkbutton(window, text = "Peixe?", variable=check_var, command= lambda: print(check_var.get()))
button2 = tk.Button(window, text = "saber o valor do checkbutton", command= lambda: messagebox.showinfo("Informação", f"O estado do botão é: {str(check_var.get())}"))
button3 = tk.Button(window, text = "desativado", command= lambda: check_var.set(0))
button4 = tk.Button(window, text = "activado", command= lambda: check_var.set(1))
packall(label, entry, button, checkbutton, button2, button3, button4)
window.mainloop()