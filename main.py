from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()
mongodb_env = os.environ.get('MONGO')
client = MongoClient(mongodb_env)
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
            "rua" :  data["rua"],
            "bairro" :  data["bairro"],
            "cidade" :  data["cidade"],
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
        usuario = colecao.find({"endereco.rua":data["rua"]})
        lista_usuario = list(usuario)
        json_data = dumps(lista_usuario, indent = 21)
        return jsonify(lista_usuario), 200
    except Exception as e:
        return jsonify({"ERROR": str(e)}), 400
    
@app.route('/Procurar_filhos', methods=["Get"])
def procurar_filhos():
    data = request.get_json()
    
    try:
        usuario = colecao.find({"filhos":data["filhos"]})
        lista_usuario = list(usuario)
        json_data = dumps(lista_usuario, indent = 21)
        return jsonify(json_data), 200
    except Exception as e:
        return jsonify({"ERROR": str(e)}), 400



if __name__ == "__main__":
    app.run(debug=True)