import json

def lambda_handler(event, context):
    """
    Placeholder for ETL function.
    """
    print("ETL Lambda triggered. Doing nothing.")
    return {
        'statusCode': 200,
        'body': json.dumps('ETL placeholder')
    }