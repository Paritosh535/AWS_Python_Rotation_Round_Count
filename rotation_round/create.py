# """
# Date:-28-Nov-17
# created by:- paritosh yadav
# description:- This funcation get JSON data store in AWS dynamodb database.
# """
import json
import logging
import os
import time
import boto3

#assigned resource to dynamodb variable
dynamodb = boto3.resource('dynamodb')

#create function featch data from UI and save to dynamodb database
def create(event, context):
    #convert data to json object
    data = json.loads(event['body'])
    
    if data is 'null':
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        return

    timestamp = int(time.time() * 1000)
    table = dynamodb.Table(os.environ['rotationRoundTable'])
    item = {
        'week_id': data['week_id'],
        'data':data['data'],
        'createdAt': timestamp
    }
    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
