import json
import os

import requests

from constants import *
from utils import *


def download_file(url, file_name):
	"""Downloads file content from url and writes to a file."""
	url = url.replace("http", "https")
	r = requests.get(url)
	content = r.content
	
	if not os.path.exists(XLS_DIR):
		os.mkdir(XLS_DIR)
	file_path =  XLS_DIR + file_name + ".xls"
	write_content(content, file_path)


def download_excel_files():
	"""Downloads excel files containing ifsc codes for each banks and writes 
	to a file. 
	"""
	
	bank_urls = load_from_a_file(ABBR_URL_LIST)
	for bank, url in bank_urls.items():
		print bank, url
		download_file(url, bank)


if __name__ == '__main__':
	download_excel_files()

