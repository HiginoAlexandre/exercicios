import tkinter as tk
def desabilitar():
    entry["state"] = "disable"
window = tk.Tk()
window.title("Desabilitando um entry")
label = tk.Label(window, text = "desabilitando esta entry abaixo:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text = "Desabilitar",command= desabilitar)
button.pack()

window.mainloop()