#python code that calls invocation type events to find the the 
#cold start time and warm start time of a AWS lambda function

import time
import boto3

# Set up the Lambda client
lambda_client = boto3.client('lambda')

# Define the function name
function_name = 'my_function'

# Measure the cold start time
start = time.perf_counter()
response = lambda_client.invoke(FunctionName='function_name')
end = time.perf_counter()
cold_start_time = end - start
print(f'Cold start time: {cold_start_time} seconds')

# Measure the warm start time
start = time.perf_counter()
response = lambda_client.invoke(FunctionName='function_name')
end = time.perf_counter()
warm_start_time = end - start
print(f'Warm start time: {warm_start_time} seconds')