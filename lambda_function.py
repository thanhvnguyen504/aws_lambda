import json
import socket

def lambda_handler(event, context):
    # TODO implement
    event_str = json.dumps(event)
    
    # get ip address
    hostName = socket.gethostname()
    hostIP = socket.gethostbyname(hostName)
    
    print(hostIP)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Host IP: ' + hostIP + ' from ' + event_str)
    }
