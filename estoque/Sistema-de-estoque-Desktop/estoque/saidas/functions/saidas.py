from tkinter import messagebox
from db.conexao import conectar
from auth.login import usuario_logado



def enviar_saidas(entradas):
    conn = None
    cursor = None
    try:
        id_produto = entradas["id_produto"].get()
        nome_produto = entradas["Nome do Produto"].get().strip().upper()
        categoria = entradas["Categoria"].get().strip().upper()
        estoque = entradas["Estoque"].get().strip()
        quantidade = entradas["Quantidade de saida"].get().strip()
        motivo = entradas["Motivo"].get().strip().upper()
        responsavel = usuario_logado.nome.upper()

        if not quantidade or not motivo :
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
            return

        quantidade = int(quantidade)

        conn = conectar()
        cursor = conn.cursor()

        # Consulta o estoque atual
        cursor.execute("SELECT estoque FROM estoque WHERE id = %s", (id_produto,))
        resultado = cursor.fetchone()

        if not resultado:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        estoque_atual = int(resultado[0])

        if quantidade > estoque_atual:
            messagebox.showwarning("Atenção", "Quantidade de saída maior que o estoque atual.")
            return

        novo_estoque = estoque_atual - quantidade

        # Atualiza estoque
        cursor.execute("UPDATE estoque SET estoque = %s WHERE id = %s", (novo_estoque, id_produto))

        # Insere saída
        cursor.execute("""
            INSERT INTO saidas (nome_produto, categoria, quantidade, motivo, responsavel, data_saida)
            VALUES (%s, %s, %s, %s, %s, CURRENT_DATE)
        """, (nome_produto, categoria, quantidade, motivo, responsavel))

        conn.commit()
        messagebox.showinfo("Sucesso", "Saída registrada com sucesso!")

        for campo in entradas.values():
            campo.delete(0, "end")

    except ValueError:
        messagebox.showerror("Erro", "Verifique os campos numéricos. Use apenas números inteiros.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
