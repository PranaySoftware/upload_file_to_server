# Initial setup 
## Google Driver API setup

1) Turn on Google Drive API [here] (if you have any troubles, check [Python Quickstart guide]).
1) Get your .json client secret config file in [Google API Projects page] and put it in working directory (don't forget to save it as *client-secret.json*)
1) In *upload_to_drive.py* and *download_from_drive.py* file scripts change global variables FULL_PATH and DIR_NAME to your's full folder path and folder's name, which you want to upload/download/synchronize, respectively.
1) First time you run *upload_to_drive.py* or *download_from_drive.py*, it will open browser/new tab, and you will need to authenticate the script (or if it doesn't redirect you, copy the link and do authentification manually).
1) Run *drive_sync.py* script, if you want to apply changes made on local storage to specific Google Drive folder, and run *download_from_drive.py* if you want to apply changes from that Google Drive folder to your local storage.
1) (Optional) put script that you need to cron or any other task planner that you use.
1) Enjoy how simple it is!

### Requirements and Dependencies

To run this amazing project, you will need:

- Python 3 or higher installed
- Google API Python library. To install it simply run
```
   pip install --upgrade google-api-python-client
```
(or see this [installation page] for more information)

- Google Account
- Internet connection

## AWS Setup
## Prerequisites

This program requires Python3 with these libraries:

- Boto 3: install with `pip install boto3`.


## AWS Credentials

For s3upload to be able to connect to your AWS account, you need to add your AWS credentials. It is a simple process.

1. Go to [AWS IAM Console](https://console.aws.amazon.com/iam/home). 

2. Create a new user or use an existing user. 

3. Generate a new set of keys for the user.

4. Update the file named `config.ini` in the directory `src/` with 
```
[default]
ACCESS_KEY=Your Access Key
SECRET_KEY=Your Secret Key
REGION_NAME= Your s3 region

BUCKET = Your Bucket Name
```

All of these items are extremely important because if you won't have at least one of then, nothing will work :('

## How to Use
- Copy the `src\` folder to your diretory then 
```
from file_upload import upload_file
upload_file(directory_path)

```
- Also can run directly `file_upload.py` with --path as command line argument
```
python file_upload.py --path directory_path

```
- Also can use as package. In order to do that follow below instruction:
```
python -m pip install --upgrade build
python3 -m build

```
- This will create a `dist\` folder which will contain `.whl` and `.tar.gz` file.
```
pip install {{.whl}}
from src import file_upload
file_upload.upload_file(directory_path)

```