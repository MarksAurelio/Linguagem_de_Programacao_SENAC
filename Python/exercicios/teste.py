from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configurações do MySQL
app.config['MYSQL_HOST'] = 'seu_host_mysql'
app.config['MYSQL_USER'] = 'seu_usuario_mysql'
app.config['MYSQL_PASSWORD'] = 'sua_senha_mysql'
app.config['MYSQL_DB'] = 'seu_banco_de_dados'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # Aqui vc não precisa colocar nenhum dado, pois é o cursor

mysql = MySQL(app)

# Dicionário para armazenar usuários (no banco de dados que tu criar)
users = {}

def criar_usuario(username, password):
    """Cria um novo usuário e armazena a senha hash."""
    if username in users:
        return False, "Nome de usuário já existe."
    hashed_password = generate_password_hash(password)
    users[username] = hashed_password
    return True, "Usuário criado com sucesso."

def verificar_usuario(username, password):
    """Verifica se o usuário existe e a senha está correta."""
    if username in users:
        if check_password_hash(users[username], password):
            return True, "Login bem-sucedido."
        else:
            return False, "Senha incorreta."
    else:
        return False, "Usuário não encontrado."

@app.route('/criar_usuario', methods=['POST'])
def route_criar_usuario():
    """Rota para criar um novo usuário."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Nome de usuário e senha são obrigatórios.'}), 400

    success, message = criar_usuario(username, password)
    return jsonify({'message': message}), 201 if success else 409

@app.route('/login', methods=['POST'])
def login():
    """Rota para autenticar um usuário."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Nome de usuário e senha são obrigatórios.'}), 400

    success, message = verificar_usuario(username, password)
    return jsonify({'message': message}), 200 if success else 401

if __name__ == '__main__':
    # Exemplo de criação de um usuário inicial (apenas para demonstração, depois tu comenta)
    with app.app_context():
        if 'admin' not in users:
            criar_usuario('admin', 'senha123')
        print("Usuário 'admin' criado com a senha 'senha123' (para demonstração).")
    app.run(debug=True)
