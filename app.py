from flask import Flask, jsonify
from assistente import AssistenteMaratona

app = Flask(__name__)

assistente = AssistenteMaratona()

@app.route("/series")
def listar_series():
    minha_lista = ["Breaking Bad", "Round 6", "SerieQueNaoExiste"]
    resultados = [assistente.buscar_serie(serie) for serie in minha_lista]

    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
