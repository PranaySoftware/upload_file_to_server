import boto3
import configparser
import os,inspect
import argparse
import logging


class Local2S3(object):
	def __init__(self):
		self.config = configparser.ConfigParser()
		if not os.path.exists('config.ini'):
			raise FileNotFoundError

		self.config.read('config.ini')
		self.aws_access_key = self.config.get('Default', 'ACCESS_KEY')
		self.aws_secret_key = self.config.get('Default', 'SECRET_KEY')
		self.region_name = self.config.get('Default', 'REGION_NAME')
		self.bucket = self.config.get('Default','BUCKET')


		# Create a custom logger
		self.logger = logging.getLogger(__name__)

		# Create handlers
		c_handler = logging.StreamHandler()
		f_handler = logging.FileHandler('./local2s3.log')
		c_handler.setLevel(logging.WARNING)
		f_handler.setLevel(logging.WARNING)

		# Create formatters and add it to handlers
		f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		f_handler.setFormatter(f_format)

		# Add handlers to the logger
		self.logger.addHandler(f_handler)

		# super(Local2S3, self).__init__()
		# self.arg = arg


	def upload_file(self,file="",path=""):
		self.logger.warning('init successful')
		s3 = boto3.client(
			service_name='s3', 
			region_name=self.region_name,
		    aws_access_key_id=self.aws_access_key,
		    aws_secret_access_key=self.aws_secret_key
		    )

		try:
			data = open(path, 'rb')
			s3.upload_file(path, self.bucket, file)
			return True
		except Exception as e:
			self.logger.warning(str(e))
			return False


def parse_args():
    parser = argparse.ArgumentParser(description="Input path to upload file into Google drive")
    parser.add_argument("--file", action="store", dest="File Name",
                        type=str, required=True, help="file")
    parser.add_argument("--path", action="store", dest="File Path",
                        type=str, required=True, help="path")
    return parser.parse_args()

if __name__ == "__main__":
    ARGS = parse_args()
    Local2S3.upload_file()