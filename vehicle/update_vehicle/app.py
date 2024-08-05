import json

try:
    from connection import get_connection, handle_response
except ImportError:
    from .connection import get_connection, handle_response


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
    except (TypeError, KeyError, json.JSONDecodeError) as e:
        return handle_response(400, "No se ha enviado el cuerpo, e")

    id = body.get('id')
    marca = body.get('marca')
    modelo = body.get('modelo')
    autonomia = body.get('autonomia')
    camara = body.get('camara')

    if not id or not marca or not modelo or not autonomia or camara is None:
        return handle_response(
            400,
            "Faltan paramentros",
            None
        )
    response = update_vehicle(id, marca, modelo, autonomia, camara)
    return response


def update_vehicle(id, marca, modelo, autonomia, camara):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """SELECT id FROM vehicle WHERE id = %s"""
            cursor.execute(query, id)
            result = cursor.fetchall()
            if len(result) > 0:
                return handle_response(400, 'Id no encontrado', None)
            update_query = """UPDATE vehicle SET marca = %s, modelo = %s, autonomia = %s, camara = %s WHERE id = $s"""
            cursor.execute(update_query, marca, modelo, autonomia, camara, id)
            connection.commit()
    except Exception as e:
        return handle_response(500, 'Ha ocurrido un error en la transaccion!', e)
    finally:
        connection.close()
    return handle_response(200, "Actualizacion exitosa!", None)
