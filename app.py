from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# LOGIN
@app.route('/')
def inicio():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():

    usuario = request.form['usuario']
    password = request.form['password']

    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND password=?",
        (usuario, password)
    )

    dato = cursor.fetchone()

    conexion.close()

    if dato:
        return redirect('/principal')
    else:
        return "Usuario incorrecto"


# VENTANA PRINCIPAL
@app.route('/principal')
def principal():
    return render_template('principal.html')


# BUSCAR PRODUCTOS
@app.route('/buscar', methods=['GET', 'POST'])
def buscar():

    producto = None

    if request.method == 'POST':

        codigo = request.form['codigo']

        conexion = sqlite3.connect('database.db')
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM productos WHERE codigo=?",
            (codigo,)
        )

        producto = cursor.fetchone()

        conexion.close()

    return render_template(
        'buscar.html',
        producto=producto
    )


# SALIR
@app.route('/logout')
def logout():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)