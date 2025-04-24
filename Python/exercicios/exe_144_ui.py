import tkinter as tk
from tkinter import messagebox
import exe_144_db
def iniciar_interface():
    def cadastrar_usuario():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario and senha:
            exe_144_db.inserir_usuario(usuario, senha)
            messagebox.showinfo("Sucesso", f"Usuário '{usuario}' cadastrado com sucesso!")
            entrada_usuario.delete(0, tk.END)
            entrada_senha.delete(0, tk.END)
        else:
            messagebox.showwarning('Campos vazios', 'Preencha todos os campos')

    janela = tk.Tk()
    janela.title('Cadastro Simples')
    janela.geometry('200x200')

    tk.Label(janela, text='Usuário:').pack()
    entrada_usuario = tk.Entry(janela)
    entrada_usuario.pack()

    tk.Label(janela, text='Senha:').pack()
    entrada_senha = tk.Entry(janela, show='*')
    entrada_senha.pack()

    tk.Button(janela, text='Cadastrar', command=cadastrar_usuario).pack(pady=10)

    janela.mainloop()
