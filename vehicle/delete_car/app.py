try:
    from connection import get_connection, handle_response
except ImportError:
    from .connection import get_connection, handle_response


def lambda_handler(event, context):
    id = 0
    if 'queryStringParameters' in event and event['queryStringParameters'] is not None:
        id = event['queryStringParameters'].get('id')

    response = delete_vehicle(id)
    return response


def delete_vehicle(id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """DELETE FROM vehicle WHERE id = %s"""
            cursor.execute(query, id)
            connection.commit()
    except Exception as e:
        return handle_response(500, 'Ha habido un error al elimnar', e)
    finally:
        connection.close()
    return handle_response(200, 'El vehiculo ha sido eliminado correctamente')