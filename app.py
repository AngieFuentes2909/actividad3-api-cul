from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def obtener_conexion():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="2002",
        db="contabilidad",
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
    conexion.close()
    return jsonify(clientes)


@app.route('/clientes', methods=['POST'])
def crear_cliente():
    nuevo_cliente = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nuevo_cliente['nombre'], nuevo_cliente['email'], nuevo_cliente['telefono']))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Cliente creado'}), 201


@app.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    cliente_actualizado = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "UPDATE clientes SET nombre=%s, email=%s, telefono=%s WHERE id=%s"
        cursor.execute(sql, (cliente_actualizado['nombre'], cliente_actualizado['email'], cliente_actualizado['telefono'], id))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Cliente actualizado'})


@app.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "DELETE FROM clientes WHERE id=%s"
        cursor.execute(sql, (id,))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Cliente eliminado'})



@app.route('/facturas', methods=['GET'])
def obtener_facturas():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM facturas")
        facturas = cursor.fetchall()
    conexion.close()
    return jsonify(facturas)


@app.route('/facturas', methods=['POST'])
def crear_factura():
    nueva_factura = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO facturas (cliente_id, monto, fecha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nueva_factura['cliente_id'], nueva_factura['monto'], nueva_factura['fecha']))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Factura creada'}), 201


@app.route('/facturas/<int:id>', methods=['PUT'])
def actualizar_factura(id):
    factura_actualizada = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "UPDATE facturas SET cliente_id=%s, monto=%s, fecha=%s WHERE id=%s"
        cursor.execute(sql, (factura_actualizada['cliente_id'], factura_actualizada['monto'], factura_actualizada['fecha'], id))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Factura actualizada'})


@app.route('/facturas/<int:id>', methods=['DELETE'])
def eliminar_factura(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "DELETE FROM facturas WHERE id=%s"
        cursor.execute(sql, (id,))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Factura eliminada'})


if __name__ == '__main__':
    app.run(debug=True)
