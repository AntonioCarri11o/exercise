import pymysql
import json
def lambda_handler(event, __):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "This es get_data new lambda!"})
    }