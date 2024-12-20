import tkinter as tk

window = tk.Tk()
window.title("HBA PAGINA")
dados = tk.StringVar(value = "Ligado")
caixaverificacao = tk.Checkbutton(
    window,
    text= "ARROZ",
    command=lambda: print(dados.get()),
    variable = dados,
    onvalue= "Ligado",
    offvalue="Desligado"
)
caixaverificacao.pack()
radio_val = tk.StringVar(value="M")
radio = tk.Radiobutton(
    window,
    text = "Homem",
    value = "H",
    variable= radio_val
)
radio2 = tk.Radiobutton(
    window,
    text = "Mulher",
    value = "M",
    variable= radio_val
)
radio.pack()
radio2.pack()
window.mainloop()