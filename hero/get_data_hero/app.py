try:
    from connection import get_connection, handle_response, handle_response_success
except ImportError:
    from .connection import get_connection, handle_response, handle_response_success

def lambda_handler(event, context):
    connection = get_connection()
    heroes = []
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, power, origin FROM hero")
            result = cursor.fetchall()

            for row in result:
                hero = {
                    'id': row[0],
                    'name': row[1],
                    'power': row[2],
                    'origin': row[3]
                }
                heroes.append(hero)
    finally:
        connection.close()
    return handle_response_success(200, 'Heroes', heroes)