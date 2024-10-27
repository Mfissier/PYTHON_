from utils.files.pyos import *
from utils.print.print_color import *
from utils.print.print_error import *
import re
from transformers import AutoTokenizer
import json

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
    return output_path
#



def tokenize_json_file(input_path, model_name, mod_dev = False):
    """
    Tokenizes the text content of a normalized JSON file for optimized processing.
    
    Args:
        input_path (str): Path to the normalized JSON file.
        output_path (str): Path to save the tokenized output.
        model_name (str): Name of the model's tokenizer to use (default: 'gpt2').
    
    Returns:
        dict: Dictionary with tokenized data.
    """
    # Load the tokenizer
    if not model_name :
    #
        if mod_dev :
            print_red("Choice model please !")
        return None
    #
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.pad_token = tokenizer.eos_token
    except ValueError:
    #
        if mod_dev :
            print_red(f"Error: The model '{model_name}' could not be found.")
        return None
    #
    
    if (find_file(input_path) == None):
    #
        if mod_dev == True :
            print_red("Not find " + input_path + " in tokenize_json_file()")
        return None
    #
    input_path = find_file(input_path)
    # Read the JSON file content
    try:
    #
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    #
    except FileNotFoundError:
    #
        if mod_dev :
            print_red(f"Error: The file '{input_path}' was not found.")
        return None
    #
    except json.JSONDecodeError:
    #
        if mod_dev :
            print_red(f"Error: The file '{input_path}' is not a valid JSON file.")
        return None
    #
    except IOError:
    #
        if mod_dev :
            print_red(f"Error: Could not read the file '{input_path}'.")
        return None
    #
    # Recursive function to tokenize each text field in the JSON
    def tokenize_data(data):
    #
        if isinstance(data, dict):
            return {key: tokenize_data(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [tokenize_data(item) for item in data]
        elif isinstance(data, str):
        #        
            try:
                return tokenizer.encode(data, truncation=True, padding='max_length', max_length=512)
            except IndexError:
                return None
        #
        else:
            return data
    #
    tokenized_data = tokenize_data(data)
    output_path = find_folder("raw_data")
    if output_path == None :
    #
        if mod_dev :
            print_red(f"Folder raw_data not found")
        return None
    #
    output_path += "/" + get_filename_without_extension(input_path) + "_raw.json" 
    try:
    # 
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(tokenized_data, file, ensure_ascii=False, indent=4)
    # 
    except IOError:
    # 
        if mod_dev :
            print_red(f"Error: Could not write to the output file '{output_path}'.")
        return None
    # 
    print_yellow(f"The Tokenization is ok for {output_path} !")
    return tokenized_data
