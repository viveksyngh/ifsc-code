import os
import json


def write_content(content, file_path):
    """Writes content to a file, on a given file path."""
    TEMP_DIR = os.path.dirname(file_path)
    if not os.path.exists(TEMP_DIR):
        os.mkdir(TEMP_DIR)
    with open(file_path, 'w') as html_file:
        html_file.write(content)


def dump_to_file(data, file_path):
    """Dump data to file as JSON"""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def load_from_a_file(file_path):
    """Loads json content from a file and returns  it."""
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except ValueError, e:
            data = {}
    return data
