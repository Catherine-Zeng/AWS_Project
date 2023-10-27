from http import client
import time
import json
import random
import boto3

client =boto3.client("kinesis",region_name="us-east-1")

STREAM_NAME = "DataProcessingKinesis"

try:
    while True:
        time.sleep(1)
        id = random.randint(1,10000000)
        first_names= ('John','Mary','Emma')
        last_names = ('William','Kate','Lucas')
        full_name = random.choice(first_names)+""+random.choice(last_names)
        age = random.randint(1,100)
        

        data = {
            "Id": id,
            "Name":full_name,
            "Age": age
        }
        encode_data = bytes(json.dumps(data).encode("utf-8"))
        print(f"Sending:{data}")
        response = client.put_record(
            StreamName=STREAM_NAME,
            Data=encode_data,
            PartitionKey='A'  
        )
except KeyboardInterrupt:
    print("Finishing due to keyboard interrupt")
