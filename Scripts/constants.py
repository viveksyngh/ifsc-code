TEMP_DIR = "../Temp"
DATA_DIR = "../Data"
RBI_URL = "https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009"
HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
          }

FIELD_NAMES = ['BANK', 'IFSC', 'MICR', 'BRANCH', 'ADDRESS', 'CONTACT', 'CITY', 'DISTRICT', 'STATE']
JSON_DIR = DATA_DIR + '/JSON/'
XLS_DIR = DATA_DIR + '/XLS/'
ABBR_URL_LIST = DATA_DIR + '/abbr_url_list.json'
MASTER_IFSC_LIST_FILE = DATA_DIR + "/IFSC_LIST.json"
BANK_LIST_HTML_FILE = TEMP_DIR + "/bank_list.html"
BANK_NAME_FILE_URL_JOSN = DATA_DIR + "/ifsc_code_url.json"
ABBR_BANK_NAME_FILE_URL = DATA_DIR + "/abbr_url_list.json"
BANK_NAME_JSON_FILE = DATA_DIR + '/banknames.json'


