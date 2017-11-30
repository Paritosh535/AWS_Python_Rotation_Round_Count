"""
Date:-28-Nov-17
created by:- paritosh yadav
description:- This funcation get JSON data store in AWS dynamodb database.
"""

import json
import time
import logging
import os
from rotation_round import decimalencoder
import boto3

dynamodb = boto3.resource('dynamodb')

def update(event, context):
    data = json.loads(event['body'])
    if data is 'null':
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['rotationRoundTable'])

    # update the todo in the database
    result = table.update_item(
        Key={
            'week_id': event['pathParameters']['week_id']
        },
        ExpressionAttributeNames={
          '#data': 'data',
        },
        ExpressionAttributeValues={
          ':data': data['data'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #data = :data, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
