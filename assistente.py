import os
import requests
from dotenv import load_dotenv

load_dotenv()

class AssistenteMaratona:
    def __init__(self):
        self.api_key = os.getenv("OMDB_API_KEY")
        self.url_base = "http://www.omdbapi.com/"

    def buscar_serie(self, titulo):
        try:

            parametros = {"t": titulo, "apikey": self.api_key}
            resposta = requests.get(self.url_base, params=parametros)
            dados = resposta.json()
            
            if dados.get("Response") == "False":
                return {"titulo": titulo, "erro": "Série não encontrada"}
            
            return {
                "titulo": dados.get("Title", "N/A"),
                "ano": dados.get("Year", "N/A"),
                "nota": dados.get("imdbRating", "N/A")
            }

        except Exception:
            return {"titulo": titulo, "erro": "Erro ao buscar dados na API"}
