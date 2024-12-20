import requests
import tkinter as tk
from tkinter import messagebox

def baixar_pagina():
    url = url_entry.get()
    nome_arquivo = nome_arquivo_entry.get()

    if not url or not nome_arquivo:
        messagebox.showerror("Erro", "Por favor, insira a URL e o nome do arquivo.")
        return

    nome_arquivo_com_extensao = f"{nome_arquivo}.html"

    # Cabeçalho para simular um navegador
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        resposta = requests.get(url, headers=headers)

        if resposta.status_code == 200:
            with open(nome_arquivo_com_extensao, "w", encoding="utf-8") as arquivo:
                arquivo.write(resposta.text)
            messagebox.showinfo("Sucesso", f"Página salva como {nome_arquivo_com_extensao} no diretório atual.")
            label.config(text="Adicionado: "+nome_arquivo_com_extensao)
        else:
            messagebox.showerror("Erro", f"Erro ao baixar a página. Código HTTP: {resposta.status_code}")
            label.config(text="Erro ao Adicionar: "+nome_arquivo_com_extensao)
    except Exception as e:
        label.config(text="Erro ao Adicionar: "+nome_arquivo_com_extensao)
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da interface
janela = tk.Tk()
janela.title("Baixador de Páginas HTML")

# Labels e Entradas
tk.Label(janela, text="URL da página:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
url_entry = tk.Entry(janela, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Nome do arquivo (sem extensão):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
nome_arquivo_entry = tk.Entry(janela, width=50)
nome_arquivo_entry.grid(row=1, column=1, padx=10, pady=5)

# Botão para baixar
baixar_button = tk.Button(janela, text="Baixar Página", command=baixar_pagina)
baixar_button.grid(row=2, column=0, columnspan=2, pady=10)
label = tk.Label(janela, text = "texto")
label.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface
janela.mainloop()