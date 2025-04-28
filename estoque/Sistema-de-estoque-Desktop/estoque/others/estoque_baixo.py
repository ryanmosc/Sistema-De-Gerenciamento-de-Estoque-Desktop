from tkinter import messagebox
from db.conexao import conectar

def verificar_estoque_baixo():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT nome_produto, estoque FROM estoque WHERE estoque <= 5")
        produtos = cursor.fetchall()

        if produtos:
            mensagem = "Produtos com estoque baixo:\n\n"
            for nome, estoque in produtos:
                mensagem += f" {nome}: {estoque} unidades\n"

            messagebox.showwarning("Estoque Baixo", mensagem)
        else:
            messagebox.showinfo("Estoque Ok", "Nenhum produto com estoque baixo encontrado.")

        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao verificar estoque: {e}")
