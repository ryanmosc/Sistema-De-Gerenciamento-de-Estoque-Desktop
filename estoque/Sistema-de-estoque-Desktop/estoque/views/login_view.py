# Importando bibliotecas e funções
import tkinter as tk
from auth.login import verificar_login
from views.registro_view import tela_registro  

def exibir_tela_login(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    # Criando um frame centralizado para os widgets
    frame = tk.Frame(janela)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

   

    # Campo de usuário
    tk.Label(frame, text="Usuário").pack(pady=5)
    entrada_usuario = tk.Entry(frame, width=30)  # Aumentado para dados maiores
    entrada_usuario.pack()

    # Campo de senha
    tk.Label(frame, text="Senha").pack(pady=5)
    entrada_senha = tk.Entry(frame, show="*", width=30)
    entrada_senha.pack()

    # Botão de login
    tk.Button(frame, text="Entrar", width=20, command=lambda: verificar_login(
        entrada_usuario.get().strip(),
        entrada_senha.get(),
        janela
    )).pack(pady=10)

    # Botão de cadastro
    # tk.Button(frame, text="Cadastre-se", width=20, command=lambda: tela_registro(janela)).pack()

    # Espaço para outras opções futuramente:
    # tk.Button(frame, text="Esqueci minha senha").pack(pady=5)
