import json

def lambda_handler(event, context):
    print('---------------------------')
    try:
        for record in event['record']:
            if record['eventName'] == 'MODIFY':
                handle_modify_record(record)
            else 
                print('----- Existing record not modified -----')
                
def handle_modify_record(record):
    print('----- Handling the record modification -----')
                
                
                
                

            
    
    
