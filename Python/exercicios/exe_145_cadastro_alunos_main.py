""" Criar uma aplicação simples que permite:

Cadastrar alunos (nome e idade)Visualizar todos os alunos cadastrados
Usar para a interface
Usar para armazenar os dados
Separar o código em
db.py → funções de banco de dados
ui.py → interface gráfica
main.py → ponto de entrada

def mostrar_alunos():
alunos = db.listar_alunos()
texto = "\n".join([f"{a[1]} ({a[2]} anos)" for a in alunos])
messagebox.showinfo("Alunos", texto) """
import exe_145_cadastro_alunos_db
import exe_145_cadastro_alunos_ui

if __name__ == "__main__":
    exe_145_cadastro_alunos_db.criar_tabela()
    exe_145_cadastro_alunos_ui.iniciar_interface()
  