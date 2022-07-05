from flask import Flask
from flask_restful import Api
from app.resources.receita.cnpj.client import ClientCNPJ
from app.resources.receita.cpf.client import ClientCPF

app = Flask(__name__)
api = Api(app)

api.add_resource(ClientCNPJ, '/consulta/cnpj/<string:cnpj>')
api.add_resource(ClientCPF, '/consulta/cpf/<string:cpf>/<string:nascimento>')


if __name__ == '__main__':
    app.run(debug=True)
    a=1