import tkinter as tk
from tkinter import messagebox
from prototipo_funcoes import criar_tabela_alunos, cadastrar_aluno, listar_alunos, buscar_aluno, atualizar_aluno, excluir_aluno_db

class App:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Cadastro de Alunos')
        self.janela.geometry('800x650')

        self.entrada_curso = tk.StringVar()
        self.lista_de_alunos_db = []

        self.criar_widgets()
        criar_tabela_alunos()
        self.atualizar_lista_alunos()

    def criar_widgets(self):
        # Campos de Cadastro
        tk.Label(self.janela, text='Nome Completo:').pack(pady=5)
        self.entrada_nome = tk.Entry(self.janela, width=40)
        self.entrada_nome.pack(pady=5)

        tk.Label(self.janela, text='Idade:').pack(pady=5)
        self.entrada_idade = tk.Entry(self.janela, width=10)
        self.entrada_idade.pack(pady=5)

        tk.Label(self.janela, text='Curso:').pack(pady=5)
        cursos = ['Engenharia de Software', 'Ciência da Computação', 'Programação de Sistemas', 'Sistemas de Informação']
        self.entrada_curso.set('Selecione um curso')
        opcoes_curso = tk.OptionMenu(self.janela, self.entrada_curso, *cursos)
        opcoes_curso.config(width=37)
        opcoes_curso.pack(pady=5)

        tk.Button(self.janela, text='Cadastrar Aluno(a)', command=self.cadastrar_aluno).pack(pady=10)

        # Campo de Busca
        tk.Label(self.janela, text='Buscar Aluno por Nome:').pack(pady=5)
        self.entrada_busca = tk.Entry(self.janela, width=40)
        self.entrada_busca.pack(pady=5)
        tk.Button(self.janela, text='Buscar', command=self.buscar_aluno).pack(pady=5)

        # Lista de Alunos
        tk.Label(self.janela, text='Alunos Cadastrados:').pack(pady=10)
        self.lista_alunos_listbox = tk.Listbox(self.janela, height=10, width=100)
        self.lista_alunos_listbox.pack(pady=5)

        # Botões de Ação
        tk.Button(self.janela, text='Editar Aluno(a) Selecionado(a)', command=self.carregar_para_edicao).pack(pady=5)
        tk.Button(self.janela, text='Excluir Aluno(a) Selecionado(a)', command=self.excluir_aluno).pack(pady=5)

        self.resultado = tk.Label(self.janela, text='', fg='green')
        self.resultado.pack(pady=5)

    def cadastrar_aluno(self):
        nome = self.entrada_nome.get()
        idade = self.entrada_idade.get()
        curso = self.entrada_curso.get()

        if not nome or not idade or curso == 'Selecione um curso':
            self.resultado.config(text='Há um ou mais campos sem preencher.', fg='red')
            return

        if cadastrar_aluno(nome, idade, curso):
            self.resultado.config(text='Aluno(a) cadastrado(a) com sucesso!', fg='green')
            self.atualizar_lista_alunos()
            self.entrada_nome.delete(0, tk.END)
            self.entrada_idade.delete(0, tk.END)
            self.entrada_curso.set('Selecione um curso')
        else:
            self.resultado.config(text='Erro ao cadastrar aluno.', fg='red')

    def atualizar_lista_alunos(self):
        self.lista_alunos_listbox.delete(0, tk.END)
        alunos = listar_alunos()
        self.lista_de_alunos_db = alunos
        for aluno in alunos:
            aluno_info_str = f'Matrícula: {aluno["matricula"]}, Nome: {aluno["nome"]}, Idade: {aluno["idade"]}, Curso: {aluno["curso"]}'
            self.lista_alunos_listbox.insert(tk.END, aluno_info_str)

    def buscar_aluno(self):
        termo_busca = self.entrada_busca.get()
        alunos_encontrados = buscar_aluno(termo_busca)
        self.lista_alunos_listbox.delete(0, tk.END)
        for aluno in alunos_encontrados:
            aluno_info_str = f'Matrícula: {aluno["matricula"]}, Nome: {aluno["nome"]}, Idade: {aluno["idade"]}, Curso: {aluno["curso"]}'
            self.lista_alunos_listbox.insert(tk.END, aluno_info_str)

    def carregar_para_edicao(self):
        selecionado_indices = self.lista_alunos_listbox.curselection()
        if not selecionado_indices:
            messagebox.showinfo('Seleção', 'Selecione um aluno para editar.')
            return

        indice_selecionado = selecionado_indices[0]
        aluno_selecionado = self.lista_de_alunos_db[indice_selecionado]

        janela_edicao = tk.Toplevel(self.janela)
        janela_edicao.title('Editar Informações do Aluno')

        tk.Label(janela_edicao, text='Matrícula:').pack(pady=5)
        label_matricula_edicao = tk.Label(janela_edicao, text=aluno_selecionado['matricula'])
        label_matricula_edicao.pack(pady=5)

        tk.Label(janela_edicao, text='Nome Completo:').pack(pady=5)
        entrada_nome_edicao = tk.Entry(janela_edicao, width=40)
        entrada_nome_edicao.insert(0, aluno_selecionado['nome'])
        entrada_nome_edicao.pack(padx=10, pady=5)

        tk.Label(janela_edicao, text='Idade:').pack(pady=5)
        entrada_idade_edicao = tk.Entry(janela_edicao, width=10)
        entrada_idade_edicao.insert(0, aluno_selecionado['idade'])
        entrada_idade_edicao.pack(pady=5)

        tk.Label(janela_edicao, text='Curso:').pack(pady=5)
        entrada_curso_edicao_var = tk.StringVar(janela_edicao)
        cursos = ['Engenharia de Software', 'Ciência da Computação', 'Programação de Sistemas', 'Sistemas de Informação']
        entrada_curso_edicao_var.set(aluno_selecionado['curso'])
        opcoes_curso_edicao = tk.OptionMenu(janela_edicao, entrada_curso_edicao_var, *cursos)
        opcoes_curso_edicao.config(width=37)
        opcoes_curso_edicao.pack(pady=5)

        def salvar_edicao():
            novo_nome = entrada_nome_edicao.get()
            nova_idade = entrada_idade_edicao.get()
            novo_curso = entrada_curso_edicao_var.get()
            matricula_aluno = aluno_selecionado['matricula']

            if not novo_nome or not nova_idade or not novo_curso == 'Selecione um curso':
                messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')
                return

            if atualizar_aluno(matricula_aluno, novo_nome, nova_idade, novo_curso):
                self.atualizar_lista_alunos()
                janela_edicao.destroy()
                self.resultado.config(text='Informações do aluno(a) atualizadas com sucesso!', fg='green')
            else:
                self.resultado.config(text='Erro ao atualizar aluno.', fg='red')

        tk.Button(janela_edicao, text='Salvar Alterações', command=salvar_edicao).pack(pady=10)

    def excluir_aluno(self):
        selecionado_indices = self.lista_alunos_listbox.curselection()
        if not selecionado_indices:
            messagebox.showinfo('Seleção', 'Selecione um aluno para excluir.')
            return

        indice_selecionado = selecionado_indices[0]
        aluno_excluir = self.lista_de_alunos_db[indice_selecionado]

        confirmacao = messagebox.askyesno('Confirmação', f'Tem certeza que deseja excluir o cadastro de {aluno_excluir["nome"]} (Matrícula: {aluno_excluir["matricula"]})?')
        if confirmacao:
            if excluir_aluno_db(aluno_excluir['matricula']):
                self.atualizar_lista_alunos()
                self.resultado.config(text=f'Cadastro de {aluno_excluir["nome"]} excluído com sucesso!', fg='green')
            else:
                self.resultado.config(text='Erro ao excluir aluno.', fg='red')

if __name__ == "__main__":
    janela = tk.Tk()
    app = App(janela)
    janela.mainloop()
    