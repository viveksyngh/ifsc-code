import json

import xlrd

from utils import *
from constants import *


def generate_json_files():
	if not os.path.exists(JSON_DIR): # If Json directory not exists
		os.mkdir(JSON_DIR) # Make directory
	
	bank_urls = load_from_a_file(BANK_NAME_FILE_URL_JOSN)
	master_ifsc_list = []
	
	for key in bank_urls.keys():
		json_file_path = JSON_DIR + key + ".json"
		try:
			wb = xlrd.open_workbook(XLS_DIR + key + '.xls')
			print key
			work_sheet = wb.sheet_by_index(0)
			rows = work_sheet.nrows
			ifsc_list = []
			
			for row in range(1, rows):
				item = {}
				# Generating dictionary with key value pair
				for col, key in enumerate(FIELD_NAMES): 
					value = work_sheet.cell_value(rowx=row, colx=col)
					if type(value) == float:
						value = str(value).split('.')[0]
					item[key] = value
				
				ifsc_list.append(item)
				master_ifsc_list.append(item)
			
			# Generating ifsc code list bank wise
			dump_to_file(ifsc_list, json_file_path)
		except Exception, e:
			print "Unable to open file for " + key
		
	# Generating master ifsc code list for all banks
	dump_to_file(master_ifsc_list, MASTER_IFSC_LIST_FILE)


if __name__ == '__main__':
	generate_json_files()