import json

def lambda_handler(event, context):
    print('---------------------------')
    print('----- In the lambda handler -----')
    try:
        for record in event['Records']:
            if record['eventName'] == 'MODIFY':
                print('----- A record has been modified in the table! -----')
                handle_modify_record(record)
            else: 
                print('----- Existing record not modified -----')


    except Exception as e:
        print(e)
        print('---------------------------')
        return "Error occured!"
                
def handle_modify_record(record):
    print('----- Handling the record modification -----')
         
    newImage = record['dynamodb']['NewImage']
               
    employeeID = newImage['EmployeeID']['S']
    employmentStatus = newImage['activeEmployee']['BOOL']
    employeeNumber = newImage['phoneNumber']['N']
    
    if employmentStatus is False:
        print('----- Calling fucntion to make outbound dial---')


                
                
                

            
    
    
