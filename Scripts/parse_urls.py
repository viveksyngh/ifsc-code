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


def parse_links_from_HTML(file_content):
    """Function parses all anchor tags from HTML file,
        Generates dictionary of all bank name and it IFSC code url list 
        and writes to file.
    """
    
    # Parsing html files to get list of all anchor tags  
    soup = BeautifulSoup(file_content, 'html.parser')
    table_content = soup.find('table', class_='tablebg')
    anchor_links = table_content.find_all('a')

    bank_links = {}
    for anchor_link in anchor_links:
        bank_links[str(anchor_link.text)] = anchor_link.get('href')
    return bank_links


def parse_urls():
    content = get_html_content()
    return parse_links_from_HTML(content)  


if __name__ == '__main__':
    parse_urls()
