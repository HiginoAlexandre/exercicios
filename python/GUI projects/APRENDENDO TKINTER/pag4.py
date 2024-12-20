import tkinter as tk
from tkinter import messagebox
import minhas_funcões as func
def clique():
    messagebox.showinfo("BOTAO CLICADO", "Muito obrigado por clicar no botão")
    print("Botão clicado")
window = tk.Tk()
window.title("HIGINO ALEXANDRE")
func.centralizar_janela(window, 800, 500)
label = tk.Label(window, text = "Texto escrito pelo Higino Alexandre")
label.pack()
text = tk.Text(window)
text.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text = "Aperte para gerar um alerta", command=clique)
button.pack()

window.mainloop()