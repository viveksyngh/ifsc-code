import os
import json

from constants import TEMP_DIR


def write_content(content, file_path):
    """Writes content to a file, on a given file path."""
    if not os.path.exists(TEMP_DIR):
        os.mkdir(TEMP_DIR)
    html_file = open(file_path, 'w')
    html_file.write(content)
    html_file.close()


def dump_to_file(data, file_path):
    """Dump data to file as JSON"""
    file = open(file_path, 'w')
    json.dump(data, file, indent=4)
    file.close()


def load_from_a_file(file_path):
    """Loads json content from a file and returns  it."""
    file = open(file_path, 'r')
    try:
        data = json.load(file)
    except ValueError, e:
        data = {}
    return data
