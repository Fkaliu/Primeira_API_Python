# API - É um ligar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. Endpoints -
#   - localhost/livros (GET) #consulta
#   - localhost/livros (POST) #criar
#   - localhost/livros/id (GET)
#   - localhost/livros/id (PUT)
#   - localhost/livros/id (delete)
# 4. Quais recursos - Livros
from flask import Flask, jsonify, request
app = Flask(__name__)
livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis - 1',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Os Aneis do Poder',
        'autor': 'Lucas Luco'
    },
    {
        'id': 3,
        'titulo': 'O Lobo guarana',
        'autor': 'Indio Juca'
    }
]
#consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
#consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
#excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
app.run(port=5000, host='localhost', debug=True)
