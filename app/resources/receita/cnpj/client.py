import json
from flask_restful import Resource
from requests import HTTPError
import requests
from app.config import URL_BASE_CNPJ

class ClientCNPJ(Resource):


    def get(self, cnpj):
        try:
            response = requests.get(f'{URL_BASE_CNPJ}{cnpj}')
            response = response.text
            response_load = json.loads(response)
            if response_load['status'] == "ERROR":
                return {'message': 'Upload Error'}, 404
            else:
                return {'message': response_load}, 200
        except HTTPError as httperr:
            return {'message': httperr}, 404
