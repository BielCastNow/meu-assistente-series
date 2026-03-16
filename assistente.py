import os
import requests
from dotenv import load_dotenv

load_dotenv()

class AssistenteMaratonas:
    def __init__(self):
        self.api_key = os.getenv('OMDb_API_KEY')
        self.base_url = 'http://www.omdbapi.com/'

    def buscar_serie(self, nome_serie):
        try:
            params = {
                't': nome_serie, 
                'apikey': self.api_key, 
                'type': 'series'
            }
            response = requests.get(self.base_url, params=params)
            dados = response.json()

            if dados.get("Response") == "False":
                return {"erro": f"Serie '{nome_serie}' não encontrada!"}

            return {
                "titulo": dados.get("Title"), 
                "ano": dados.get("Year"),
                "sinopse": dados.get("Plot"), 
                "nota": dados.get("imdbRating")
            }
        except Exception as e:
            return {"erro": f"Erro na busca: {str(e)}"}

    def buscar_lista(self, lista):
        return [self.buscar_serie(serie) for serie in lista]