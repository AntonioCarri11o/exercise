import json

try:
    from connection import get_connection, handle_success, handle_response
except ImportError:
    from .connection import get_connection, handle_success, handle_response


def lambda_handler(event):

    try:
        body = json.loads(event['body'])
    except (TypeError, KeyError, json.JSONDecodeError):
        return handle_response(400, "No se ha enviado el cuerpo", None)

    marca = body.get('marca')
    modelo = body.get('modelo')
    autonomia = body.get('autonomia')
    camara = body.get('camara')

    if not marca or not modelo or not autonomia or not camara:
        return handle_response(400, 'Faltan parámetros', None)

    response = insert_vehicle(marca, modelo, autonomia, camara)
    return response


def insert_vehicle(marca, modelo, autonomia, camara):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """INSERT INTO vehicle (marca, modelo, autonomia, camara) VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (marca, modelo, autonomia, camara))

            connection.commit()
    except Exception as e:
        return handle_response(500, 'Error al insertar', e)
    finally:
        connection.close()
    return handle_response(200, 'Vehículo guardado correctamente', None)
