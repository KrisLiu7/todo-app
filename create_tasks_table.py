import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Table name
table_name = 'Tasks'

try:
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'task_id',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'task_id',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'  # No need to define capacity units
    )

    print(f"Creating table '{table_name}'...")

    # Wait for table to be active
    dynamodb_resource = boto3.resource('dynamodb')
    table = dynamodb_resource.Table(table_name)
    table.wait_until_exists()

    print(f"✅ Table '{table_name}' created successfully!")

except dynamodb.exceptions.ResourceInUseException:
    print(f"⚠️ Table '{table_name}' already exists.")