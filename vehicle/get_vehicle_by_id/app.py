try:
    from connection import get_connection, handle_response_success
except ImportError:
    from .connection import get_connection, handle_response_success

def lambda_handler(event, context):
    id = 0
    if 'queryStringParameters' in event and event['queryStringParameters'] is not None:
        id = event['queryStringParameters'].get('id')

    connection = get_connection()
    query = f"SELECT id, marca, modelo, autonomia, camara FROM vehicle WHERE id = {id}"
    vehicles = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

            for row in result:
                vehicle = {
                    'id': row[0],
                    'marca': row[1],
                    'modelo': row[2],
                    'autonomia': row[3],
                    'camara': row[4]
                }
                vehicles.append(vehicle)
    finally:
        connection.close()
    return handle_response_success(200, 'Exito', vehicles)