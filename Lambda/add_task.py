import json
import boto3
from datetime import datetime
import traceback

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')  # your actual table name

def lambda_handler(event, context):
    print("Received event:", event)

    try:
        # Parse event['body']
        if isinstance(event['body'], str):
            body = json.loads(event['body'])
        else:
            body = event['body']

        # Required fields
        user_id = body.get("user_id")
        task_id = body.get("task_id") or body.get("title")
        title = body.get("title")

        # Optional fields
        description = body.get("description", "")
        status = body.get("status", "Waiting to start")
        due_date = body.get("due_date")
        created_at = datetime.utcnow().isoformat()

        print("Parsed values:", user_id, task_id, title)

        if not user_id or not task_id or not title:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing required fields"})
            }

        table.put_item(
            Item={
                'user_id': user_id,
                'task_id': task_id,
                'title': title,
                'description': description,
                'status': status,
                'due_date': due_date,
                'created_at': created_at
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Task added successfully"})
        }

    except Exception as e:
        # ✅ Make sure everything here is indented
        traceback_str = traceback.format_exc()
        print("Full traceback:", traceback_str)

        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }
