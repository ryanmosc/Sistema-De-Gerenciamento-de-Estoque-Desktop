import tkinter as tk
from tkinter import messagebox
import requests
from estoque.views_estoque.ler_view import exibir_tela_pesquisa
from funcionarios.views_funcionarios.ler_view import exibir_tela_funcionarios
from saidas.views_saidas.ler_view_saidas import abrir_tela_saidas
from views.sobre_view import abrir_sobre
from others.estoque_baixo import verificar_estoque_baixo
import datetime

def criar_tela_inicial():
    from auth.login import usuario_logado

    janela = tk.Tk()
    janela.geometry("1100x600")
    janela.configure(bg="#f5f5f5")

    # Função para atualizar data e hora no título
    def atualizar_data_hora():
        agora = datetime.datetime.now()
        data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
        janela.title(f"Sistema de Estoque                                                                                                                      {data_hora_formatada}")
        janela.after(1000, atualizar_data_hora)  

    atualizar_data_hora()  

    # ======== Topbar ========
    topbar = tk.Frame(janela, bg="#2c3e50", height=50)
    topbar.pack(side="top", fill="x")

    def criar_tela_inicio():
        from views.home_view import criar_tela_inicial
        janela.destroy()
        criar_tela_inicial()

    def sair():
        if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
            janela.destroy()

    botoes = {
        "🏠 Início": lambda: criar_tela_inicio(),
        "📦 Estoque": lambda: exibir_tela_pesquisa(janela),
        "🧑‍💼 Funcionários": lambda: exibir_tela_funcionarios(janela),
        "📤 Saídas": lambda: abrir_tela_saidas(janela),
        "❔ Sobre": lambda: abrir_sobre(janela),
        "🚪 Sair": sair
    }

    for texto, comando in botoes.items():
        btn = tk.Button(
            topbar,
            text=texto,
            fg="white",
            bg="#34495e",
            activebackground="#1abc9c",
            relief="flat",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10,
            command=comando
        )
        btn.pack(side="left", padx=5, pady=5)

    # ======== Área principal ========
    area_principal = tk.Frame(janela, bg="#ecf0f1")
    area_principal.pack(expand=True, fill="both")

    # ======== Rodapé ========
    rodape = tk.Frame(janela, bg="#bdc3c7", height=30)
    rodape.pack(side="bottom", fill="x")

    def obter_cotacao_dolar():
        try:
            response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
            if response.status_code == 200:
                dados = response.json()
                cotacao = dados["USDBRL"]["bid"]
                return f"💵 Dólar: R$ {float(cotacao):.2f}"
            else:
                return "Erro ao obter cotação."
        except Exception as e:
            return f"Erro: {e}"

    cotacao_dolar = obter_cotacao_dolar()
    nome_usuario = usuario_logado.nome

    label_usuario = tk.Label(
        rodape,
        text=f" Bem-vindo(a), {nome_usuario}",
        font=("Arial", 10),
        bg="#bdc3c7",
        anchor="w"
    )
    label_usuario.pack(side="left", padx=10)

    label_cotacao = tk.Label(
        rodape,
        text=cotacao_dolar,
        font=("Arial", 10),
        bg="#bdc3c7",
        anchor="e"
    )
    label_cotacao.pack(side="right", padx=10)

    estoque_baixo = verificar_estoque_baixo()

    label_estoque = tk.Label(
        area_principal,
        text=estoque_baixo,
        font=("Arial", 22, "bold"),
        bg="#ecf0f1",
        fg="#e74c3c",
        pady=30
    )
    label_estoque.pack(expand=True)

    janela.mainloop()

# 🔧 Execução temporária
# criar_tela_inicial()
