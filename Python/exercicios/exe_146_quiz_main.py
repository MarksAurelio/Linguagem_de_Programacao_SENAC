""" Desenvolver um aplicativo de quiz interativo utilizando Python com interface
gráfica (Tkinter) e integração com banco de dados MySQL, aplicando os conceitos
de programação orientada a objetos e manipulação de bancos de dados.
Descrição:
Você deverá criar um sistema de quiz com:
1. Interface gráfica amigável
2. Armazenamento de pontuações
3. Duas perguntas com múltipla escolha (mínimo)
4. Ranking dos melhores jogadores (Desafio)
Requisitos Técnicos:
1. Estrutura do projeto:
o main.py (inicialização)
o quiz_interface.py (classe QuizApp com interface)
o quiz_database.py (operações com MySQL)
2. Funcionalidades obrigatórias:
o Cadastro do nome do jogador
o Cálculo de pontuação
o Armazenamento no banco de dados
o Lista dos participantes com a pontuação
3. Banco de dados MySQL:
o Tabela participantes com:
 id (auto incremento)
 nome (string)
 pontuação (int)
 data_registro (timestamp) """
import tkinter as tk
from exe_146_quiz_interface import QuizApp
from exe_146_quiz_database import QuizDatabase

if __name__ == "__main__":
    db = QuizDatabase(host="localhost", user="root", password="senac", port=3307, database="cadastro_4")
    db.criar_tabela()

    root = tk.Tk()
    app = QuizApp(root, db)
    root.mainloop()

    db.close()
