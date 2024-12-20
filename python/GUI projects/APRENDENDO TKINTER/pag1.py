import tkinter as tk

window = tk.Tk()
window.title("Adicionar Produto")
width = 500
height = 500
x = (window.winfo_screenwidth() - width)//2
y = (window.winfo_screenheight() - height)//2
window.geometry(f"{width}x{height}+{x}+{y}")


window.mainloop()