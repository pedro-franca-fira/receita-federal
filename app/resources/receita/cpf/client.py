import json
from urllib import response
from flask_restful import Resource
from requests import HTTPError
import requests

from app.config import URL_BASE_CPF

class ClientCPF(Resource):
    def get(self, cpf, nascimento):
        queryString = {
            'token': '6F3F02E5-438E-41AA-812E-14C2DD2BC18B',
            'cpf': cpf,
            'data-nascimento': nascimento,
            'plugin': 'CPF' 
            }
        try:
            response = requests.get(URL_BASE_CPF, params=queryString)
            response = response.text
            response_load = json.loads(response)
            return response_load
        except HTTPError as httperr:
            return {'message': httperr}

    def upload(self):
        pass