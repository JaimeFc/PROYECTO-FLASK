from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1 style='color:blue;'>¡Bienvenido a mi aplicación Flask!"
    return render_template('index.html', title='Inicio')

@app.route('/usuarios/<nombre>')
def ususarios(nombre):
    return f"<h2 style='color:blue;'>¡Hola, {nombre} gracias por visitar mi aplicación!"

@app.route('/about/')
def about():
    return render_template('about.html', title='Acerca de')

@app.route('/contacto/')
def about():
    return render_template('contacto.html', title='Contacto')

#if __name__ == '__main__':
#    app.run(debug=True)