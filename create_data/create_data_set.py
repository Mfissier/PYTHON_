from utils.files.pyos import *
from utils.print.print_color import *
from utils.print.print_error import *
import json
import re

# Helper function to normalize text strings
def normalize_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters, keeping only alphanumeric and spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Recursive function to normalize all text fields in the JSON structure
def normalize_data(data):
    if isinstance(data, dict):
        return {key: normalize_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [normalize_data(item) for item in data]
    elif isinstance(data, str):
        return normalize_text(data)
    else:
        return data

def normalize_json(file_path, mod_dev = False):
#
    """
        This function reads a JSON file, normalizes the text by removing special characters, 
        and writes the normalized content to a new file (or replaces the original).
        # [Returns] normalized content as a Python dictionary
        # [Modifies] Writes a new normalized JSON file if an output path is specified.
        Args:
            file_path (str): Path to the input JSON file.        
        Example:
            normalize_json("input.json")  # Returns normalized data
    """
    if mod_dev == True :
        print_blue("In normalize_json() :")
    if (find_file(file_path) == None):
    #
        if mod_dev == True :
            print_red("Not find" + file_path + "in normalize_json()")
        return None
    #
    file_path = find_file(file_path)
    output_path = "processed_data"
    if (find_folder(output_path) == None):
    #
        if mod_dev == True :
            print_yellow("Not find [" + output_path + "] in normalize_json(), rename this")
    #
    output_path = find_folder("processed_data")
    output_path += "/" + get_filename_without_extension(file_path) + "_normalize.json" 
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    normalized_data = normalize_data(data)
    if output_path:
    #
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(normalized_data, file, ensure_ascii=False, indent=4)
    #
    if mod_dev == True :
        print_yellow(output_path + "is create !")
    return normalized_data
#
