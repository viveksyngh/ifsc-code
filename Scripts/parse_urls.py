import os
import json

from bs4 import BeautifulSoup
import urllib2

from constants import *
from utils import *


def get_html_content():
    """Downloads RBI html page, which conatins URL to IFSC code 
        excels by bank names.
    """
    
    request = urllib2.Request(RBI_URL, headers=HEADERS)
    page = urllib2.urlopen(request)
    html_content = page.read()
    return html_content


def parse_links_from_HTML():
    """Function parses all anchor tags from HTML file,
        Generates dictionary of all bank name and it IFSC code url list 
        and writes to file.
    """

    file_content = open(BANK_LIST_HTML_FILE, 'r').read()

    # Parsing html files to get list of all anchor tags  
    soup = BeautifulSoup(file_content)
    table_content = soup.find('table', class_='tablebg')
    anchor_links = table_content.find_all('a')
    
    abbr_map = load_from_a_file(BANK_NAME_JSON_FILE)
    
    bank_links, urls_list = {}, {}
    for anchor_link in anchor_links:
        bank_links[str(anchor_link.text)] = anchor_link.get('href')
    
    for abbr, bank_name in abbr_map.items():
        urls_list[abbr] = bank_links[bank_name]
    
    dump_to_file(bank_links, BANK_NAME_FILE_URL_JOSN)
    dump_to_file(urls_list, ABBR_BANK_NAME_FILE_URL)


def parse_urls():
    content = get_html_content()
    write_content(content, BANK_LIST_HTML_FILE)
    parse_links_from_HTML()  


if __name__ == '__main__':
    parse_urls()
