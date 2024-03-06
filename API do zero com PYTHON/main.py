from Flask import Flask, request, jsonify

#Criar uma instância do flask
app = Flask(__name__)

#Database
livros = {
    {'id': 1, 'titulo': 'Python 1'},
    {'id': 2, 'titulo': 'Python 2'}
}

#Rota para listar todos os livros (GET)
@app.route('/livros', methods=['GET'])
def get_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    return jsonify({'livro:': livro[0]})

#Rota para adicionar um novo livro (POST)
@app.route('/livros', methods=['POST'])
def add_livro(livro_id):
    novo_livro = request.json
    livros.append(novo_livro)
    return jsonify({'messagem': 'Livro adicionado com sucesso'}), 201

#Rota para atualizar livro que já existe pelo id (PUT)
@app.route('/livros/<int:livro_id>', methods=['PUT'])
def update_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    livro[0]['titulo'] = request.json.get('titulo', livro[0]['titulo'])
    livro[0]['autor'] = request.json.get('autor', livro[0]['autor'])
    return jsonify({'messagem': 'Livro atualizado com sucesso'})

#Rota para excluir o livro pelo id (DELETE)
@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def delete_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    livros.remove(livro[0])
    return jsonify({'messagem': 'Livro removido com sucesso'})


if __name__ == '__name__':
    app.run(debug=True)