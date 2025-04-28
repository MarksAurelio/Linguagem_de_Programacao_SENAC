import mysql.connector
from datetime import datetime

class QuizDatabase:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.mydb = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            self.cursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao MySQL: {err}")

    def close(self):
        if self.mydb and self.mydb.is_connected():
            self.cursor.close()
            self.mydb.close()
            print("Conexão com o MySQL encerrada.")

    def criar_tabela(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS participantes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    pontuacao INT NOT NULL,
                    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.mydb.commit()
            print("Tabela 'participantes' criada com sucesso (ou já existia).")
        except mysql.connector.Error as err:
            print(f"Erro ao criar a tabela: {err}")

    def inserir_participante(self, nome, pontuacao):
        try:
            sql = "INSERT INTO participantes (nome, pontuacao) VALUES (%s, %s)"
            val = (nome, pontuacao)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            print(f"Participante '{nome}' inserido com pontuação {pontuacao}.")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir participante: {err}")

    def obter_ranking(self):
        try:
            self.cursor.execute("SELECT nome, pontuacao FROM participantes ORDER BY pontuacao DESC")
            ranking = self.cursor.fetchall()
            return ranking
        except mysql.connector.Error as err:
            print(f"Erro ao obter o ranking: {err}")
            return []

if __name__ == "__main__":
    db = QuizDatabase(host="localhost", user="root", password="senac", port=3307, database="cadastro_4")
    db.criar_tabela()
    ranking = db.obter_ranking()
    if ranking:
        print("\nRanking dos Participantes:")
        for nome, pontuacao in ranking:
            print(f"- {nome}: {pontuacao}")
    db.close()
    