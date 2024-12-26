import json

import boto3
from uuid import uuid4
client = boto3.client('dynamodb')


def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    
    if http_method=='POST':
        body=json.loads(event['body'])
        print("in post")
        item = {
                'id': str(uuid4()),
                'task': body['task'],
                'status': body.get('status', 'pending')
            }
        response=client.put_item(  TableName='ToDoTable',       Item={
                'id': {'S': item['id']},
                'task': {'S': item['task']},
                'status': {'S': item['status']}
            })

        return {
        'statusCode': 200,
        'body': json.dumps(response)
        }
    elif http_method=='GET':
        response = client.scan(TableName='ToDoTable', ConsistentRead=True)
        print("Scan Response:", response)  # Debugging log


        return {
        'statusCode': 200,
        'body': json.dumps(response)
        }
    elif http_method=='DELETE':
        task_name=json.loads(event['body']).get('task')
        response = client.scan(
                TableName='ToDoTable',
                FilterExpression='task = :task',
                ExpressionAttributeValues={':task': {'S': task_name}}
        )
        response_body = {"message": "This is a POST response", "body": response}
        item=response.get('Items',[])
        items_to_delete=item[0] 

        response=client.delete_item(
                TableName='ToDoTable',
                Key={'id': {'S': items_to_delete['id']['S']}}
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }