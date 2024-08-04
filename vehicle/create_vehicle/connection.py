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
            host="exercise.cxukkquegvcb.us-east-1.rds.amazonaws.com",
            user="root",
            password="superroot",
            database="vehicles"
        )
    except Exception as e:
        raise e
    return connection


def handle_success(status_code, message):
    return {
        'statusCode': status_code,
        'headers': headers_cors,
        'body': json.dumps({
            'statusCode': status_code,
            'message': message
        })
    }


def handle_response(status_code, message, error):
    return {
        'statusCode': status_code,
        'headers': headers_cors,
        'body': json.dumps({
            'statusCode': status_code,
            'message': message,
            'error': str(error)
        })
    }
