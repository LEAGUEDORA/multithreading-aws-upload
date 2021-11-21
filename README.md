# AWS UPLOAD SCRIPT WITH MULTPLE   THREADING IN PYTHON
This is a Python script written to upload your local files to **AWS S3** bucket. 

 - Uses Multithread
 - Many small files uploads
 - Checks **AWS** for existing files and uplods only files which are not there. 
 - Time & Data Saving
---
### Installing
Clone this repository using
```
git clone https://github.com/LEAGUEDORA/multithreading-aws-upload.git
```
And cd into the folder
```bash
cd multithreading-aws-upload
```

### Fields to be changed
You have to change the following fields in your cloned repo
```python
aws_access_key_id='<Your access key>',
aws_secret_access_key='<Your secret Key>'
AWS_BUCKET_NAME =  ""
AWS_DESTINATION_FOLDER_NAME =  ""
LOCAL_SOURCE_FOLDER_NAME =  ""
NUMBER_THREADS =  4  #Change this to your convinience
FILES_FOR_SINGLE_THREAD =  1000  # Change this
```

> These fields are marked under TODO section in the code. Description of each are there in the code

### Execution
After filling the constants, run
```bash
python aws_upload.py
```

After finishing your upload you will see `Finished Uploading` for everything on your console. 
