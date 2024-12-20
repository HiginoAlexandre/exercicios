import tkinter as tk
import minhas_funcões as func

window = tk.Tk()

window.title("saber as propriedade dos widgets")
func.centralizar_janela(window, 500, 400)
label = tk.Label(window, text = "Higino é bom programador.")
label.pack()
button = tk.Button(window, text = "saber informações", command= lambda : print(label.configure()))
button.pack()

window.mainloop()