from tkinter import messagebox
from db.conexao import conectar

def buscar_produtos_saidas(tipo_pesquisa, entrada_nome, categoria_box, entrada_responsavel, tabela):
    try:
        conn = conectar()
        cursor = conn.cursor()

        consulta_base = """
            SELECT id, nome_produto, quantidade, motivo, responsavel, data_saida 
            FROM saidas
        """

        filtros = []
        valores = []

        tipo = tipo_pesquisa.get()
        nome = entrada_nome.get().strip().upper()
        motivo = categoria_box.get().strip().upper()
        responsavel = entrada_responsavel.get().strip()

        if tipo == "Tudo":
            if motivo != "NULO":
                filtros.append("motivo = %s")
                valores.append(motivo)

        elif tipo == "Por nome":
            if nome:
                filtros.append("nome_produto ILIKE %s")
                valores.append(f"%{nome}%")

        elif tipo == "Por categoria":
            if motivo != "NULO":
                filtros.append("motivo = %s")
                valores.append(motivo)

        elif tipo == "Por responsável":
            if responsavel:
                filtros.append("responsavel ILIKE %s")
                valores.append(f"%{responsavel}%")

        elif tipo == "Nome + Categoria":
            if nome:
                filtros.append("nome_produto ILIKE %s")
                valores.append(f"%{nome}%")
            if motivo != "NULO":
                filtros.append("motivo = %s")
                valores.append(motivo)

        # Monta a query final
        if filtros:
            consulta_base += " WHERE " + " AND ".join(filtros)

        consulta_base += " ORDER BY data_saida DESC"

        cursor.execute(consulta_base, tuple(valores))
        resultados = cursor.fetchall()

        # Limpa a tabela
        for item in tabela.get_children():
            tabela.delete(item)

        # Adiciona os novos resultados
        for linha in resultados:
            tabela.insert("", "end", values=linha)

        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro na busca de saídas: {e}")
