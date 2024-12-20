import tkinter as tk
import minhas_funcões as func

window = tk.Tk()
window.title("INTRODUÇÃO AOS WIDGETS")
func.centralizar_janela(window, 800, 600)

#Criando elementos na pagina
label = tk.Label(window, text = "Higino Alexandre")
text = tk.Text(window)
entry = tk.Entry(window)
button = tk.Button(window, text = "Aperte aqui para criar alguma coisa")

#Adicionando os elementos à página
label.pack()
text.pack()
entry.pack()
button.pack()

window.mainloop()