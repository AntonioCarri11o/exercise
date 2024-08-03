try:
    from connection import get_connection, handle_success
except ImportError:
    from .connection import get_connection, handle_success


def lambda_handler(event, context):
    connection = get_connection()
    vehicles = []

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, marca, modelo, autonomia, camara FROM vehicle")
            result = cursor.fetchall()

            for row in result:
                vehicle = {
                    'id': row[0],
                    'marca': row[1],
                    'modelo': row[2],
                    'autonomia': row[3],
                    'camara': row[4],
                }
                vehicles.append(vehicle)
    finally:
        connection.close()
    return handle_success(200, 'Vehicles', vehicles)
