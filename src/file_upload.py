import os,sys,inspect
from pathlib import Path
from local2s3 import Local2S3
from local2gdrive import Local2Gdrive
import argparse
import logging

media_file_format = [".mp3", ".mp4", ".mpeg4", ".WMV", ".3gp", ".webm"]
image_file_format = [".jpg", ".png", ".SVG", ".Webp"]
doc_file_format = [".doc", ".docx", ".CSV", ".pdf"]

def upload_file(path):
    if not os.path.isdir(path):
        raise NotADirectoryError
    gdriveobj = Local2Gdrive()
    s3obj = Local2S3()
    for root, dirs, files in os.walk(Path(path)):
        for file in files:
            split_tup = os.path.splitext(file)
            if split_tup[1] in media_file_format or split_tup[1] in image_file_format:
                s3obj.upload_file(file,os.path.join(root,file))
            if split_tup[1] in doc_file_format:
                gdriveobj.upload_file(file,os.path.join(root,file))

def parse_args():
    parser = argparse.ArgumentParser(description="Input path to upload file into Google drive")
    parser.add_argument("--path", action="store", dest="path",
                        type=str, required=True, help="Folder path")
    return parser.parse_args()

if __name__ == "__main__":
    ARGS = parse_args()
    upload_file(**vars(ARGS))




