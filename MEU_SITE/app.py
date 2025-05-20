# Importa a classe Flask e a função render_template da biblioteca flask
# Flask: framework principal usado para criar o app web
# render_template: usada para carregar arquivos HTML que estão na pasta "templates"
from flask import Flask, render_template

# Cria uma instância do app Flask
# __name__ informa ao Flask onde o app está sendo executado
app = Flask(__name__)

# Define a rota principal do site ('/') — ou seja, a página inicial
@app.route('/')
def index():
    # Quando alguém acessar a rota '/', o Flask vai renderizar o arquivo "index.html"
    return render_template("index.html")

# Este bloco garante que o app só será executado se este arquivo for rodado diretamente
# (e não importado por outro script)
if __name__ == "__main__":
    # Inicia o servidor Flask no modo debug (útil para ver erros no navegador e recarregar automaticamente)
    app.run(debug=True)



