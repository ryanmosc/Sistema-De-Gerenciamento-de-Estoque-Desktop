#Importando as bibliotecas
import tkinter as tk
from views.login_view import exibir_tela_login

#Criando a primeira tela do site
if __name__ == "__main__":
    app = tk.Tk()
    app.title("Login")
    app.geometry("600x400")
    exibir_tela_login(app)
    app.mainloop()
