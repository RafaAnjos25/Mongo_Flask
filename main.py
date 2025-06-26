from pymongo import MongoClient
from flask import Flask, request, jsonify


app = Flask(__name__)

client = MongoClient('mongodb+srv://rafaelaugusto0112:MaDbI0E1Nw5Difx4@clusterbancodedados.t9q8hma.mongodb.net/')
db = client.get_database("ClusterBancoDeDados")
colecao = db.get_collection('yshtola')


@app.route('/registrar', methods=["Post"])
def registrar():
    data = request.get_json

    



if __name__ == "__main__":
    app.run(debug=True)