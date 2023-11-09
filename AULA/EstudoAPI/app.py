from flask import Flask, jsonify, request
from Cadastro import Cadastro

app = Flask(__name__)
_Cadastrar = Cadastro()

@app.route('/')
def initroute():
    return "Caminho Inicial"

@app.route('/hello', methods=['GET'])
def helloworld():
    return "Hello World"

@app.route('/Cadastrar/usuario/<usuario>', methods=['POST'])
def Cadastro(usuario):
    return _Cadastrar.CriarNovoUsuario(usuario)

@app.errorhandler(404)
def RotaNaoEncontrada(Erro):
    return "Você esta perdido!" +str(Erro)
    

if __name__ == '__main__':
    app.run(debug=True)