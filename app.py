from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/guardar_datos", methods=["POST"])
def guardar_datos():
    campo1 = request.form["campo1"]
    campo2 = request.form["campo2"]

    # Conexión a la base de datos SQLite
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()

    # Insertar datos en la base de datos
    cursor.execute('INSERT INTO datos (campo1, campo2) VALUES (?, ?)', (campo1, campo2))
    conn.commit()

    conn.close()

    return render_template("exito.html")

if __name__ == "__main__":
    app.run(debug=True)
