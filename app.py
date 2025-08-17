from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color:blue;'>¡Bienvenido a mi aplicación Flask!"

@app.route('/usuarios/<nombre>')
def ususarios(nombre):
    return f"<h2 style='color:blue;'>¡Hola, {nombre} gracias por visitar mi aplicación!"

if __name__ == '__main__':
    app.run(debug=True)