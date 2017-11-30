"""
Date:-28-Nov-17
created by:- paritosh yadav
description:- This funcation get JSON data store in AWS dynamodb database.
"""

import os
import json
import boto3
from rotation_round import decimalencoder

dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['rotationRoundTable'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'week_id': event['pathParameters']['week_id']
        }
    )
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
