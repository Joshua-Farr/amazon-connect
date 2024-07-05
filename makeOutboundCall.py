import json

def lambda_handler(event, context):
    
    customerName = event['name'];
    customerPhoneNumber = event['number'];
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!' +' '+ customerName +' '+ customerPhoneNumber)
    }
