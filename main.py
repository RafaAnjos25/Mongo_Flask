from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps



client = MongoClient('mongodb+srv://rafaelaugusto0112:MaDbI0E1Nw5Difx4@clusterbancodedados.t9q8hma.mongodb.net/')
db = client.get_database("ClusterBancoDeDados")
colecao = db.get_collection('yshtola')

app = Flask(__name__)


@app.route('/cadastrar', methods=["Post"])
def registrar():
    data = request.get_json()

    try:
        novo_usuario = {
            "nome" : data["nome"],
            "telefone" : data["telefone"],
            "endereco" :  data["endereco"],
            "filhos" : data["filhos"]
        } 
        colecao.insert_one(novo_usuario)
        return jsonify({"Message" : "Usuario cadastrado com sucesso"}), 200
    except Exception as e:
        return jsonify({"ERROR": str(e)}), 400
    
@app.route('/Procurar_Nome', methods=["Get"])
def procurar_nome():
    data = request.get_json()
    
    try:
        usuario = colecao.find({"nome":data["nome"]})
        lista_usuario = list(usuario)
        json_data = dumps(lista_usuario, indent = 21)
        return jsonify(json_data), 200
    except Exception as e:
        return jsonify({"ERROR": str(e)}), 400

@app.route('/Procurar_rua', methods=["Get"])
def procurar_rua():
    data = request.get_json()
    
    try:
        usuario = colecao.find({"endereco" : {"rua":data["rua"]}})
        lista_usuario = list(usuario)
        json_data = dumps(lista_usuario, indent = 21)
        return jsonify(json_data), 200
    except Exception as e:
        return jsonify({"ERROR": str(e)}), 400



if __name__ == "__main__":
    app.run(debug=True)