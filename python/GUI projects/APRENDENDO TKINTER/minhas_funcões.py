def centralizar_janela(window, w, h):
    x,y = ((window.winfo_screenwidth()- w)//2, (window.winfo_screenheight() - h )//2)
    window.geometry(f"{w}x{h}+{x}+{y}")