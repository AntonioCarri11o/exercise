import json
import pymysql

headers_cors = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
}

def get_connection():
    try:
        connection = pymysql.connect(
            host='exercise.cxukkquegvcb.us-east-1.rds.amazonaws.com',
            user='root',
            password='superroot',
            database='vehicles'
        )
    except Exception as e:
        raise e
    return connection

def handle_response(statusCode, message, error):
    return {
        'statusCode': statusCode,
        'headers': headers_cors,
        'body': json.dumps({
            'statusCode': statusCode,
            'message': message,
            'error': error
        })
    }
