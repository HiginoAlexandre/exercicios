import tkinter as tk
def centralizar_janela(w, h):
    x,y = ((window.winfo_screenwidth()- w)//2, (window.winfo_screenheight() - h )//2)
    window.geometry(f"{w}x{h}+{x}+{y}")

window = tk.Tk()
window.title("TKINTER WIDGETS")
centralizar_janela(800, 200)
window.mainloop()