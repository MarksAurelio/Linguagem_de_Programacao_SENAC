import tkinter as tk
from tkinter import messagebox
from exe_146_quiz_database import QuizDatabase

class QuizApp:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Quiz Interativo")
        self.db = db
        self.nome_jogador = tk.StringVar()
        self.pontuacao = 0
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "pergunta": "Em que ano estamos?",
                "opcoes": ["2024", "2020", "2023", "2025"],
                "resposta": "2025"
            },
            {
                "pergunta": "Quais das cores apresentadas não faz parte da bandeira brasileira?",
                "opcoes": ["Amarelo", "Verde", "Prata", "Azul"],
                "resposta": "Prata"
            }
        ]

        self.criar_tela_cadastro()

    def criar_tela_cadastro(self):
        self.frame_cadastro = tk.Frame(self.root)
        self.frame_cadastro.pack(pady=20)

        tk.Label(self.frame_cadastro, text="Digite seu nome:").pack(pady=5)
        self.entry_nome = tk.Entry(self.frame_cadastro, textvariable=self.nome_jogador)
        self.entry_nome.pack(pady=5)

        tk.Button(self.frame_cadastro, text="Começar o Quiz", command=self.iniciar_quiz).pack(pady=10)

    def iniciar_quiz(self):
        nome = self.nome_jogador.get()
        if nome:
            self.frame_cadastro.destroy()
            self.nome = nome
            self.mostrar_pergunta()
        else:
            messagebox.showerror("Erro", "Por favor, digite seu nome.")

    def mostrar_pergunta(self):
        if self.pergunta_atual < len(self.perguntas):
            self.frame_pergunta = tk.Frame(self.root)
            self.frame_pergunta.pack(padx=20, pady=20)

            pergunta_data = self.perguntas[self.pergunta_atual]
            tk.Label(self.frame_pergunta, text=pergunta_data["pergunta"], wraplength=400, justify="left").pack(pady=10)

            self.botoes_opcoes = []
            for i, opcao in enumerate(pergunta_data["opcoes"]):
                botao = tk.Button(self.frame_pergunta, text=opcao, width=30, command=lambda o=opcao: self.verificar_resposta(o))
                botao.pack(pady=5)
                self.botoes_opcoes.append(botao)

        else:
            self.finalizar_quiz()

    def verificar_resposta(self, resposta_selecionada):
        pergunta_data = self.perguntas[self.pergunta_atual]
        if resposta_selecionada == pergunta_data["resposta"]:
            self.pontuacao += 1
            messagebox.showinfo("Correto", "Resposta correta!")
        else:
            messagebox.showerror("Incorreto", f"Resposta incorreta. A resposta era: {pergunta_data['resposta']}")

        self.frame_pergunta.destroy()
        self.pergunta_atual += 1
        self.mostrar_pergunta()

    def finalizar_quiz(self):
        messagebox.showinfo("Fim do Quiz", f"Quiz finalizado, {self.nome}! Sua pontuação foi: {self.pontuacao}/{len(self.perguntas)}")
        self.db.inserir_participante(self.nome, self.pontuacao)
        self.mostrar_ranking()

    def mostrar_ranking(self):
        ranking = self.db.obter_ranking()
        if ranking:
            self.frame_ranking = tk.Toplevel(self.root)
            self.frame_ranking.title("Ranking dos Melhores Jogadores")

            tk.Label(self.frame_ranking, text="Ranking dos Participantes", font=("Arial", 16, "bold")).pack(pady=10)

            for i, (nome, pontuacao) in enumerate(ranking):
                tk.Label(self.frame_ranking, text=f"{i+1}. {nome}: {pontuacao}").pack(pady=2)
        else:
            messagebox.showinfo("Ranking", "Ainda não há participantes no ranking.")

        reiniciar = messagebox.askyesno("Reiniciar", "Deseja jogar novamente?")
        if reiniciar:
            self.pontuacao = 0
            self.pergunta_atual = 0
            self.criar_tela_cadastro()
        else:
            self.root.destroy()

if __name__ == "__main__":
    db = QuizDatabase(host="localhost", user="root", password="senac", port=3307, database="cadastro_4")
    root = tk.Tk()
    app = QuizApp(root, db)
    root.mainloop()
    db.close()
