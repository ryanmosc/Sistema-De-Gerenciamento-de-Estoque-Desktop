
# 📦 StockBuddy - Gerenciamento de Estoque para Armazéns

**StockBuddy** é um sistema desktop desenvolvido para facilitar o gerenciamento de estoque de armazéns, oferecendo controle de entradas, saídas, métricas e cadastro de funcionários de forma intuitiva e eficiente.

---

## 🚀 Funcionalidades Principais

- Cadastro e autenticação de usuários (login e registro)
- Controle completo de produtos em estoque
- Controle de saídas de produtos
- Gerenciamento de funcionários
- Geração de métricas de produtos
- Relatórios de estoque baixo
- Interface desktop amigável usando **Tkinter**

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (GUI)
- **PostgreSQL** (Banco de Dados)
- **psycopg2** (Conector Python-PostgreSQL)

---

## 📂 Estrutura de Pastas

```
estoque/
├── auth/           # Controle de login, registro e recuperação de senha
├── db/             # Conexão com banco de dados
├── estoque/        # Controle de estoque (CRUD e views)
├── funcionarios/   # Controle de funcionários
├── home/           # Tela inicial
├── others/         # Relatórios e métricas
├── saidas/         # Controle de saídas
└── views/          # Telas genéricas (login, home, sobre, etc.)
```

---

## ⚙️ Como Instalar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/StockBuddy.git
   cd StockBuddy/estoque
   ```

2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install psycopg2-binary
   ```

4. Configure a conexão do banco de dados em:
   ```
   db/conexao.py
   ```
   (Atualize com seu usuário, senha e nome do banco.)

---

## ▶️ Como Rodar

Execute o arquivo principal:
```bash
python main.py
```
(rodando dentro da pasta `estoque/`)

---

## 📝 Observações

- É necessário ter o **PostgreSQL** instalado e configurado.
- As tabelas devem ser criadas previamente (usuários, produtos, saídas, etc.).
- Projeto ideal para pequenas empresas ou armazéns que precisam de um controle local eficiente.

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Fique à vontade para abrir **Issues** ou enviar **Pull Requests**.

---

## 📢 Autor

Desenvolvido por [Seu Nome].
