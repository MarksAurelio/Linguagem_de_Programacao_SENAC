import mysql.connector
def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            port=3307,
            password="senac",
            database="cadastro_2" 
        )
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id int AUTO_INCREMENT PRIMARY key, 
            username varchar (50) not null,
            senha varchar (50) not null
            )
        """)
    conn.commit()
    conn.close()

def inserir_usuario(username, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, senha) VALUES (%s,%s)", (username, senha))
    conn.commit()
    conn.close()
    