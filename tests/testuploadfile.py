import json
import pytest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
srcdir = os.path.join(parentdir,"src")
sys.path.insert(0,srcdir)
from file_upload import upload_file

def test_invalid_file_stream():
	file_name = "invalid_file"
	try:
		upload_file(file_name)
		assert False
	except Exception:
		assert True

def test_valid_file():
	dir_path = os.path.join(parentdir,"files")
	try:
		upload_file(dir_path)
		assert True
	except Exception:
		assert False

