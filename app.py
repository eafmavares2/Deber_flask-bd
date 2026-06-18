from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="Diasdelasemana",
        user="postgres",
        password="12345"
    )

# Ruta principal
@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Base de Datos Dias de la Semana",
        "rutas_disponibles": [
            "/lunes",
            "/martes",
            "/miercoles",
            "/jueves"
        ]
    })

# Ruta Lunes
@app.route("/lunes")
def lunes():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM lunes")
    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    actividades = []

    for fila in datos:
        actividades.append({
            "id": fila[0],
            "actividad": fila[1]
        })

    return jsonify(actividades)

# Ruta Martes
@app.route("/martes")
def martes():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM martes")
    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    actividades = []

    for fila in datos:
        actividades.append({
            "id": fila[0],
            "actividad": fila[1]
        })

    return jsonify(actividades)

# Ruta Miércoles
@app.route("/miercoles")
def miercoles():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM miercoles")
    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    actividades = []

    for fila in datos:
        actividades.append({
            "id": fila[0],
            "actividad": fila[1]
        })

    return jsonify(actividades)

# Ruta Jueves
@app.route("/jueves")
def jueves():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM jueves")
    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    actividades = []

    for fila in datos:
        actividades.append({
            "id": fila[0],
            "actividad": fila[1],
            "observacion": fila[2]
        })

    return jsonify(actividades)

if __name__ == "__main__":
    app.run(debug=True)