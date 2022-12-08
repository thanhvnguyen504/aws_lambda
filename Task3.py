import time
import boto3

# Set up the Lambda client
lambda_client = boto3.client('lambda')

# Define the function name
function_name = 'my_function'

# Set the number of invocations to make
num_invocations = 10

# Measure the execution time for each choice
for choice in [1, 2, 3]:
    start = time.perf_counter()
    for i in range(num_invocations):
        try:
            response = lambda_client.invoke(FunctionName=function_name, InvocationType='Event')
            # Check the response status code to make sure the function was successfully invoked
            if response['StatusCode'] != 202:
                raise Exception('Function invocation failed')
            time.sleep(1)  # Sleep for 1 second after each function invocation
        except Exception as e:
            print(f'Error: {e}')
            break
    end = time.perf_counter()
    execution_time = end - start
    print(f'Choice {choice}: {execution_time} seconds')
