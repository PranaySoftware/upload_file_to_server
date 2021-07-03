from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os,inspect
import argparse
import logging

class Local2Gdrive(object):
    def __init__(self):
        if not os.path.exists('client_secrets.json'):
            raise FileNotFoundError

        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

        # Create a custom logger
        self.logger = logging.getLogger(__name__)

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('./local2gdrive.log')
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.WARNING)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

    def upload_file(self,file="",path=""):
        if not os.path.exists(path):
            raise FileNotFoundError
        try:
            self.logger.info("Init successfull")
            file1 = self.drive.CreateFile({'title': file})  # Create GoogleDriveFile instance with title 'Hello.txt'.
            file1.SetContentFile(path) # Set content of the file from given string.
            file1.Upload()
            self.logger.info("%s uploaded successfull"%file)
            return True
        except Exception as e:
            self.logger.error(str(e))
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
    Local2Gdrive.upload_file()



            