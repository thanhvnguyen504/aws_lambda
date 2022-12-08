#!/usr/bin/env python
# coding: utf-8

# In[14]:


import time
import boto3
client = boto3.client('s3')


# In[22]:


#s3_client.list_buckets()
function_name = 'my_function'


# In[23]:


lambda_client = boto3.client('lambda')


# In[24]:


import json
event = {'invoke_name': 'thanhs_desktop'}


# In[25]:


start = time.perf_counter()
response = lambda_client.invoke(
                FunctionName='function_name',
                Payload=json.dumps(event)
                )
end = time.perf_counter()
cold_start_time = end - start
print(f'Cold start time: {cold_start_time} seconds')


# In[26]:


start = time.perf_counter()
response = lambda_client.invoke(
                FunctionName='function_name',
                Payload=json.dumps(event)
                )
end = time.perf_counter()
warm_start_time = end - start
print(f'Warm start time: {warm_start_time} seconds')


# In[27]:


response['Payload'].read()


# In[ ]:




