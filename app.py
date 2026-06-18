from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
app.json.ensure_ascii = False 

# METODO PARA CONECTAR A LA BASE DE DATOS
def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="DIAS",
        user="postgres",
        password="12345" 
    )

# RUTA PRINCIPAL (INICIO)
@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenidos aqui observaran las actividades por dia."
    })

# RUTA DE LUNES
@app.route("/lunes")
def ruta_lunes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM lunes")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    
    lista = [{"id": f[0], "actividad": f[1]} for f in datos]
    return jsonify(lista)

# RUTA DE MARTES
@app.route("/martes")
def ruta_martes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM martes")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    
    lista = [{"id": f[0], "actividad": f[1]} for f in datos]
    return jsonify(lista)

# RUTA DE MIERCOLES
@app.route("/miercoles")
def ruta_miercoles():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM miercoles")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    
    lista = [{"id": f[0], "actividad": f[1]} for f in datos]
    return jsonify(lista)

# RUTA DE JUEVES
@app.route("/jueves")
def ruta_jueves():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM jueves")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    
#Aui esta ruta incluye el campo 'observacion' requerido para este día
    lista = [{"id": f[0], "actividad": f[1], "observacion": f[2]} for f in datos]
    return jsonify(lista)


# PUNTO DE ARRANQUE DE LA APLICACIÓN
if __name__ == "__main__":
    app.run(debug=True)
    
    
    