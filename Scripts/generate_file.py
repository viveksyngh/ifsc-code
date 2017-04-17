import sys
from parse_urls import parse_urls
from generate_excel_files import download_excel_files
from generate_json_files import generate_json_files


if __name__ == '__main__':
    args = sys.argv
    file_type = args[1]
    parse_urls()
    download_excel_files()
    if file_type == 'JSON':
        generate_json_files()

