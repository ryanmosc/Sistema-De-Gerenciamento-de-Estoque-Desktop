import tkinter as tk
from tkinter import ttk
from saidas.functions.saidas import enviar_saidas

def exibir_formulario_saidas(janela_pai, dados_produto):
    
    janela_atualizar = tk.Toplevel(janela_pai)
    janela_atualizar.title("Saidas")
    janela_atualizar.geometry("400x400")

    tk.Label(janela_atualizar, text=" Saidas", font=("Arial", 14, "bold")).pack(pady=10)
    form_frame = tk.Frame(janela_atualizar)
    form_frame.pack(pady=10)

    entradas = {}
    motivo = ["VENDA", "USO INTERNO", "OUTRO"]
    
    campos = [
        "Nome do Produto",
        "Categoria",
        "Estoque",
        "Quantidade de saida",
        "Motivo"
        
    ]

    for idx, campo in enumerate(campos):
        tk.Label(form_frame, text=campo).grid(row=idx, column=0, sticky="e", pady=5, padx=5)

        if campo == "Motivo":
            combobox = ttk.Combobox(form_frame, values=motivo, state="readonly")
            combobox.grid(row=idx, column=1, pady=5, padx=5)
            entradas[campo] = combobox
        else:
            entrada = tk.Entry(form_frame)
            entrada.grid(row=idx, column=1, pady=5, padx=5)
            entradas[campo] = entrada

    entradas["id_produto"] = tk.Entry(form_frame)
    if dados_produto:
        entradas["id_produto"].insert(0,dados_produto[0])
        entradas["Nome do Produto"].insert(0, dados_produto[1])
        entradas["Estoque"].insert(0, dados_produto[2])
        entradas["Categoria"].insert(0, dados_produto[3])
    
    def desabilitar_campos_nao_editaveis():
        entradas["Nome do Produto"].config(state="readonly")
        entradas["Estoque"].config(state="readonly")
        entradas["Categoria"].config(state="readonly")

    desabilitar_campos_nao_editaveis()
     

    tk.Button(
    janela_atualizar, 
    text="Inserir", 
    command=lambda: enviar_saidas(entradas)
    ).pack(pady=15)

    tk.Button(janela_atualizar, text="Fechar", command=janela_atualizar.destroy).pack(pady=5)