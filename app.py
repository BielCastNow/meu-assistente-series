from flask import Flask, jsonify
from maratonas import AssistenteMaratonas  # Importando sua classe

app = Flask(__name__)
assistente = AssistenteMaratonas()

@app.route('/')
def maratonar():
    series = ["Stranger Things", "Naruto", "Round 6"]
    resultado = assistente.buscar_lista(series)
    return jsonify(resultado)

@app.route('/teste')
def teste():
    return "O servidor está vivo!"

if __name__ == '__main__':
    app.run(debug=True)