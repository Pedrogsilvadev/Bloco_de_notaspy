import tkinter as tk
from tkinter import filedialog, messagebox

def novo_arquivo():
    texto.delete(1.0, tk.END)

def abrir_arquivo():
    try:
        arquivo = filedialog.askopenfile(mode="r", defaultextension=".txt")
        if arquivo:
            conteudo = arquivo.read()
            texto.delete(1.0, tk.END)
            texto.insert(tk.INSERT, conteudo)
            arquivo.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")

def salvar_arquivo():
    try:
        arquivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if arquivo:
            conteudo = texto.get(1.0, tk.END).rstrip()  # Remove a quebra de linha extra no final
            arquivo.write(conteudo)
            arquivo.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível salvar o arquivo: {e}")

# Criar a janela principal
bloco = tk.Tk()
bloco.title("Bloco de Notas")

# Configurar a barra de menu
menu_barra = tk.Menu(bloco)
bloco.config(menu=menu_barra)

arquivo_menu = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Arquivo", menu=arquivo_menu)

arquivo_menu.add_command(label="Novo", command=novo_arquivo)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=bloco.quit)

# Adicionar o widget de texto
texto = tk.Text(bloco)
texto.pack(expand=True, fill=tk.BOTH)

# Iniciar o loop principal da interface gráfica
bloco.mainloop()
