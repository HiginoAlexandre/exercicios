import tkinter as tk
import minhas_funcões as func

#funcões para a pagina tkinter
def atualizar():
    label.config(text = entry.get())
    label2["text"] = text.get("1.0", "end-1c")
    entry["estate"] = "disabled"
window = tk.Tk()
window.title("OBTENDO O CONTEUDO DE ALGUNS WIDGETS NO TKINTER")
func.centralizar_janela(window, 800, 600)
#criação das labels que serão alteradas
label = tk.Label(window, text = "... Este texto será atulizando quando o botão atualizar for clicado")
label2 = tk.Label(window, text = "... Esta label tambem será altualizada")
label.pack()
label2.pack()

entry = tk.Entry(window)
entry.pack()
text = tk.Text(window)
text.pack()
button = tk.Button(window, text = "ATUALIZAR", command= atualizar)
button.pack()

window.mainloop()