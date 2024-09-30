from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

# Criar uma rota = se comunicar com o cliente | Receber e devolver informações
@app.route("/") # Definir a rota
# O que vai ser executado?
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Esta página definitivamente contém informações :)"

# Só para desenvolvimento local, executado de forma manual
if __name__ == "__main__":
    app.run(debug=True) # O debug habilita logs para nos ajudar
