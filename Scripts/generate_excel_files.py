import json
import os

import requests

from constants import *
from utils import *


def download_file(url, file_name, out_dir):
	"""Downloads file content from url and writes to a file."""
	url = url.replace("http", "https")
	r = requests.get(url)
	content = r.content
	XLS_DIR = out_dir + "/XLS/"

	if not os.path.exists(XLS_DIR):
		os.mkdir(XLS_DIR)
	file_path =  XLS_DIR + file_name + ".xls"
	write_content(content, file_path)


def download_excel_files(bank_urls, out_dir, verbose):
	"""Downloads excel files containing ifsc codes for each banks and writes 
	to a file. 
	"""
	for bank, url in bank_urls.items():
		if verbose:
			print bank, url
		download_file(url, bank, out_dir)


if __name__ == '__main__':
	download_excel_files()

