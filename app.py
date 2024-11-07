

from flask import Flask

# Inicializar a aplicação Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Eldin Gosta de Bacon."

# Rota adicional
@app.route('/sobre')
def sobre():
    return "Esta é uma aplicação simples feita com Flask."

# Executa a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0',
        debug=True)

