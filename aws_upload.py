import boto3
session = boto3.Session(
aws_access_key_id='<Your access key>',
aws_secret_access_key='<Your secret Key>')
s3 = session.resource('s3')
import threading
from os import listdir
from typing import List

#TODO: Constans to be filled by developer
AWS_BUCKET_NAME = "" 
AWS_DESTINATION_FOLDER_NAME = ""
LOCAL_SOURCE_FOLDER_NAME = ""
NUMBER_THREADS = 4 #Change this to your convinience
FILES_FOR_SINGLE_THREAD = 1000 # Change this


bucket = s3.Bucket(AWS_BUCKET_NAME)
s3_list = [str(data.key).split("/")[1].strip() if str(data.key).split("/")[0].strip() == AWS_DESTINATION_FOLDER_NAME else "" for data in bucket.objects.all()]
print(f"Got s3 list with length of {len(s3_list)}")

def start_uploading(file_names: List):
    for i in file_names:
        if i in s3_list:
            try:
                temp = open(f"{LOCAL_SOURCE_FOLDER_NAME}/{i}", "rb")
                object_ = s3.Object(AWS_BUCKET_NAME, f"{AWS_DESTINATION_FOLDER_NAME}/{i}")
                object_.put(Body = temp)
                temp.close()
            except Exception as e:
                print(e, i)
        else:
            print(f"{i} not in the storage")
    print("Finished Uploading")

threads = []
for i in range(0, NUMBER_THREADS):
    try:
        files_list = listdir(LOCAL_SOURCE_FOLDER_NAME)[i*FILES_FOR_SINGLE_THREAD:(i*FILES_FOR_SINGLE_THREAD + FILES_FOR_SINGLE_THREAD + 1)]
    except Exception as e:
        files_list = listdir(LOCAL_SOURCE_FOLDER_NAME)[i*FILES_FOR_SINGLE_THREAD:]
        print("Index Error")
    threads.append(threading.Thread(target = start_uploading, args = (files_list,)))
for i in threads: i.start()