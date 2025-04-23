import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

db_host = 'localhost' # informações de host do banco de dados
db_user = 'root' # nome de usuário do banco de dados
db_password = 'senac' # senha do banco de dados
db_port = 3307
db_database= 'app' # nome do banco de dados

def conectar_db():
    # tenta estabelecer uma conexão com o banco de dados mysql.
    try:
        meu_db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, port=db_port, database=db_database)

        return meu_db # retorna o objeto de conexão se a conexão for bem-sucedida.
    except Error as e:
        messagebox.showerror('Erro de Banco de Dados', f'Erro ao conectar ao MySQL: {e}') # exibe uma janela de erro com a mensagem de falha na conexão.
        return None # retorna None se a conexão com o banco de dados falhar.

def criar_tabela_alunos():
    # conecta ao banco de dados e cria a tabela 'alunos' se ela ainda não existir.
    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor() # cria um objeto cursor para executar comandos sql.
        try:
            meu_cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    matricula INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    idade INT NOT NULL,
                    curso VARCHAR(255) NOT NULL
                )
            ''') # define o comando sql para criar a tabela 'alunos' com matrícula auto_increment como chave primária.
            meu_db.commit() # envia as alterações para o banco de dados, criando a tabela se necessário.
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao criar tabela: {e}') # exibe uma janela de erro se a criação da tabela falhar.
        finally:
            meu_cursor.close() # fecha o cursor para liberar recursos.
            meu_db.close() # fecha a conexão com o banco de dados.

def cadastrar_aluno():
    # obtém os dados do aluno dos campos de entrada, valida-os e os insere no banco de dados.
    nome = entrada_nome.get() # obtém o texto inserido no campo de nome.
    idade = entrada_idade.get() # obtém o texto inserido no campo de idade.
    curso = entrada_curso.get() # obtém o curso selecionado no menu de opções.

    if not nome or not idade or curso == 'Selecione um curso':
        resultado.config(text='Há um ou mais campos sem preencher.', fg='red') # configura o texto do rótulo de resultado para indicar campos vazios.
        return # interrompe a função se houver campos vazios.

    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            sql = 'INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)' # define o comando sql para inserir um novo aluno.
            val = (nome, idade, curso) # define os valores a serem inseridos no comando sql.
            meu_cursor.execute(sql, val) # executa o comando sql com os valores fornecidos.
            meu_db.commit() # envia as alterações para o banco de dados, inserindo o novo aluno.
            resultado.config(text='Aluno(a) cadastrado(a) com sucesso!', fg='green') # configura o texto do rótulo de resultado para indicar sucesso.
            atualizar_lista_alunos() # chama a função para atualizar a lista de alunos exibida.
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao cadastrar aluno: {e}') # exibe uma janela de erro se o cadastro falhar.
        finally:
            meu_cursor.close() # fecha o cursor para liberar recursos.
            meu_db.close() # fecha a conexão com o banco de dados.

    entrada_nome.delete(0, tk.END) # limpa o conteúdo do campo de entrada de nome.
    entrada_idade.delete(0, tk.END) # limpa o conteúdo do campo de entrada de idade.
    entrada_curso.set('Selecione um curso') # redefine o menu de opções de curso para o valor padrão.

def atualizar_lista_alunos():
    # limpa a listbox e busca os dados atualizados dos alunos no banco de dados para exibi-los.
    lista_alunos_listbox.delete(0, tk.END) # remove todos os itens da listbox.
    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            meu_cursor.execute('SELECT matricula, nome, idade, curso FROM alunos') # define o comando sql para selecionar todos os alunos.
            alunos = meu_cursor.fetchall() # obtém todos os resultados da consulta sql.
            global lista_de_alunos_db
            lista_de_alunos_db = [] # inicializa uma lista vazia para armazenar os dados dos alunos do banco de dados.
            for matricula, nome, idade, curso in alunos:
                aluno_info = {'matricula': matricula, 'nome': nome, 'idade': idade, 'curso': curso} # cria um dicionário para armazenar as informações de cada aluno.
                lista_de_alunos_db.append(aluno_info) # adiciona o dicionário à lista de alunos.
                aluno_info_str = f'Matrícula: {matricula}, Nome: {nome}, Idade: {idade}, Curso: {curso}' # formata as informações do aluno para exibição na listbox.
                lista_alunos_listbox.insert(tk.END, aluno_info_str) # insere a string formatada na listbox.
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao buscar alunos: {e}') # exibe uma janela de erro se a busca de alunos falhar.
        finally:
            meu_cursor.close() # fecha o cursor para liberar recursos.
            meu_db.close() # fecha a conexão com o banco de dados.

def buscar_aluno():
    # busca alunos no banco de dados cujo nome contenha o termo de busca inserido.
    termo_busca = entrada_busca.get().lower() # obtém o texto de busca do campo de entrada e o converte para minúsculas.

    print(f"Termo de busca: '{termo_busca}'")

    lista_alunos_listbox.delete(0, tk.END) # remove todos os itens da listbox.
    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            sql = 'SELECT matricula, nome, idade, curso FROM alunos WHERE LOWER(nome) LIKE %s' # define o comando sql para buscar alunos pelo nome (insensível a maiúsculas/minúsculas).
            val = (f'%{termo_busca}%',) # define o valor a ser substituído no comando sql (com curingas para busca parcial).
            meu_cursor.execute(sql, val) # executa o comando sql com o termo de busca.
            alunos = meu_cursor.fetchall() # obtém todos os resultados da busca.
            for matricula, nome, idade, curso in alunos:
                aluno_info_str = f'Matrícula: {matricula}, Nome: {nome}, Idade: {idade}, Curso: {curso}' # formata as informações do aluno para exibição.
                lista_alunos_listbox.insert(tk.END, aluno_info_str) # insere a string formatada na listbox.
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao buscar alunos: {e}') # exibe uma janela de erro se a busca falhar.
        finally:
            meu_cursor.close() # fecha o cursor para liberar recursos.
            meu_db.close() # fecha a conexão com o banco de dados.

def carregar_para_edicao():
    # carrega as informações do aluno selecionado na listbox para a janela de edição.
    selecionado_indices = lista_alunos_listbox.curselection() # obtém os índices dos itens selecionados na listbox.
    if not selecionado_indices:
        messagebox.showinfo('Seleção', 'Selecione um aluno para editar.') # exibe uma mensagem se nenhum aluno estiver selecionado.
        return # interrompe a função se nenhum aluno estiver selecionado.

    indice_selecionado = selecionado_indices[0] # obtém o índice do primeiro aluno selecionado.
    aluno_selecionado = lista_de_alunos_db[indice_selecionado] # obtém os dados do aluno selecionado da lista de alunos do banco de dados.

    janela_edicao = tk.Toplevel(janela) # cria uma nova janela de nível superior para a edição.
    janela_edicao.title('Editar Informações do Aluno') # define o título da janela de edição.

    tk.Label(janela_edicao, text='Matrícula:').pack(pady=5) # cria e posiciona um rótulo para exibir a matrícula.
    label_matricula_edicao = tk.Label(janela_edicao, text=aluno_selecionado['matricula']) # cria e posiciona um rótulo para exibir a matrícula do aluno (geralmente não editável).
    label_matricula_edicao.pack(pady=5)

    tk.Label(janela_edicao, text='Nome Completo:').pack(pady=5) # cria e posiciona um rótulo para o campo de nome.
    entrada_nome_edicao = tk.Entry(janela_edicao, width=40) # cria e posiciona um campo de entrada para o nome.
    entrada_nome_edicao.insert(0, aluno_selecionado['nome']) # preenche o campo de entrada com o nome atual do aluno.
    entrada_nome_edicao.pack(padx=10, pady=5)

    tk.Label(janela_edicao, text='Idade:').pack(pady=5) # cria e posiciona um rótulo para o campo de idade.
    entrada_idade_edicao = tk.Entry(janela_edicao, width=10) # cria e posiciona um campo de entrada para a idade.
    entrada_idade_edicao.insert(0, aluno_selecionado['idade']) # preenche o campo de entrada com a idade atual do aluno.
    entrada_idade_edicao.pack(pady=5)

    tk.Label(janela_edicao, text='Curso:').pack(pady=5) # cria e posiciona um rótulo para o menu de opções de curso.
    entrada_curso_edicao_var = tk.StringVar(janela_edicao) # cria uma variável de string para controlar o menu de opções de curso na janela de edição.
    cursos = ['Engenharia de Software', 'Ciência da Computação', 'Programação de Sistemas', 'Sistemas de Informação'] # define a lista de cursos disponíveis.
    entrada_curso_edicao_var.set(aluno_selecionado['curso']) # define o curso atual do aluno como o valor inicial selecionado.
    opcoes_curso_edicao = tk.OptionMenu(janela_edicao, entrada_curso_edicao_var, *cursos) # cria e posiciona o menu de opções para o curso.
    opcoes_curso_edicao.config(width=37)
    opcoes_curso_edicao.pack(pady=5)

    def salvar_edicao():
        # obtém os novos valores dos campos de edição e atualiza o registro do aluno no banco de dados.
        novo_nome = entrada_nome_edicao.get() # obtém o texto do campo de edição de nome.
        nova_idade = entrada_idade_edicao.get() # obtém o texto do campo de edição de idade.
        novo_curso = entrada_curso_edicao_var.get() # obtém o curso selecionado no menu de opções de edição.
        matricula_aluno = aluno_selecionado['matricula'] # obtém a matrícula do aluno que está sendo editado.

        if not novo_nome or not nova_idade or not novo_curso == 'Selecione um curso':
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos.') # exibe uma mensagem de erro se algum campo estiver vazio.
            return # interrompe a função se houver campos vazios.

        meu_db = conectar_db()
        if meu_db:
            meu_cursor = meu_db.cursor()
            try:
                sql = 'UPDATE alunos SET nome=%s, idade=%s, curso=%s WHERE matricula=%s' # define o comando sql para atualizar as informações do aluno com base na matrícula.
                val = (novo_nome, nova_idade, novo_curso, matricula_aluno) # define os novos valores e a condição de atualização.
                meu_cursor.execute(sql, val) # executa o comando sql com os novos valores.
                meu_db.commit() # envia as alterações para o banco de dados, atualizando o registro do aluno.
                atualizar_lista_alunos() # chama a função para atualizar a lista de alunos exibida.
                janela_edicao.destroy() # fecha a janela de edição.
                resultado.config(text='Informações do aluno(a) atualizadas com sucesso!', fg='green') # exibe uma mensagem de sucesso na janela principal.
            except Error as e:
                messagebox.showerror('Erro de Banco de Dados', f'Erro ao atualizar aluno: {e}') # exibe uma janela de erro se a atualização falhar.
            finally:
                meu_cursor.close() # fecha o cursor para liberar recursos.
                meu_db.close() # fecha a conexão com o banco de dados.

    tk.Button(janela_edicao, text='Salvar Alterações', command=salvar_edicao).pack(pady=10) # cria e posiciona um botão para salvar as alterações feitas na janela de edição.

def excluir_aluno():
    # exclui o aluno selecionado da listbox do banco de dados.
    selecionado_indices = lista_alunos_listbox.curselection() # obtém os índices dos itens selecionados na listbox.
    if not selecionado_indices:
        messagebox.showinfo('Seleção', 'Selecione um aluno para excluir.') # exibe uma mensagem se nenhum aluno estiver selecionado.
        return # interrompe a função se nenhum aluno estiver selecionado.

    indice_selecionado = selecionado_indices[0] # obtém o índice do primeiro aluno selecionado.
    aluno_excluir = lista_de_alunos_db[indice_selecionado] # obtém os dados do aluno a ser excluído da lista de alunos do banco de dados.

    confirmacao = messagebox.askyesno('Confirmação', f'Tem certeza que deseja excluir o cadastro de {aluno_excluir["nome"]} (Matrícula: {aluno_excluir["matricula"]})?') # exibe uma caixa de diálogo de confirmação antes da exclusão.
    if confirmacao:
        meu_db = conectar_db()
        if meu_db:
            meu_cursor = meu_db.cursor()
            try:
                sql = 'DELETE FROM alunos WHERE matricula=%s' # define o comando sql para excluir o aluno com base na matrícula.
                val = (aluno_excluir['matricula'],) # define o valor da matrícula do aluno a ser excluído.
                meu_cursor.execute(sql, val) # executa o comando sql com a matrícula fornecida.
                meu_db.commit() # envia as alterações para o banco de dados, excluindo o aluno.
                atualizar_lista_alunos() # chama a função para atualizar a lista de alunos exibida.
                resultado.config(text=f'Cadastro de {aluno_excluir["nome"]} excluído com sucesso!', fg='green') # exibe uma mensagem de sucesso na janela principal.
            except Error as e:
                messagebox.showerror('Erro de Banco de Dados', f'Erro ao excluir aluno: {e}') # exibe uma janela de erro se a exclusão falhar.
            finally:
                meu_cursor.close() # fecha o cursor para liberar recursos.
                meu_db.close() # fecha a conexão com o banco de dados.

lista_de_alunos_db = [] # lista para armazenar os dados dos alunos lidos do banco de dados.

janela = tk.Tk()
janela.title('Cadastro de Alunos')
janela.geometry('800x650') 

entrada_curso = tk.StringVar()

label_nome = tk.Label(janela, text='Nome Completo:')
label_nome.pack(pady=5)
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

label_idade = tk.Label(janela, text='Idade:')
label_idade.pack(pady=5)
entrada_idade = tk.Entry(janela, width=10)
entrada_idade.pack(pady=5)

label_curso = tk.Label(janela, text='Curso:')
label_curso.pack(pady=5)
cursos = ['Engenharia de Software', 'Ciência da Computação', 'Programação de Sistemas', 'Sistemas de Informação']
entrada_curso.set('Selecione um curso')
opcoes_curso = tk.OptionMenu(janela, entrada_curso, *cursos)
opcoes_curso.config(width=37)
opcoes_curso.pack(pady=5)

tk.Button(janela, text='Cadastrar Aluno(a)', command=cadastrar_aluno).pack(pady=10)

label_busca = tk.Label(janela, text='Buscar Aluno por Nome:')
label_busca.pack(pady=5)
entrada_busca = tk.Entry(janela, width=40)
entrada_busca.pack(pady=5)
tk.Button(janela, text='Buscar', command=buscar_aluno).pack(pady=5)

label_lista = tk.Label(janela, text='Alunos Cadastrados:')
label_lista.pack(pady=10)
lista_alunos_listbox = tk.Listbox(janela, height=10, width=100)
lista_alunos_listbox.pack(pady=5)

tk.Button(janela, text='Editar Aluno(a) Selecionado(a)', command=carregar_para_edicao).pack(pady=5)
tk.Button(janela, text='Excluir Aluno(a) Selecionado(a)', command=excluir_aluno).pack(pady=5)

resultado = tk.Label(janela, text='', fg='green')
resultado.pack(pady=5)

criar_tabela_alunos()

atualizar_lista_alunos()

janela.mainloop()
