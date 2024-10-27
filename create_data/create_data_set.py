from utils.files.pyos import *
from utils.print.print_color import *
from utils.print.print_error import *
import json
import re

def normalize_json(file_path, output_path=None):
    """
        This function reads a JSON file, normalizes the text by removing special characters, 
        and writes the normalized content to a new file (or replaces the original).
        
        # [Returns] normalized content as a Python dictionary
        # [Modifies] Writes a new normalized JSON file if an output path is specified.

        Args:
            file_path (str): Path to the input JSON file.
            output_path (str, optional): Path to the output file for saving the normalized JSON content.
        
        Example:
            1/ normalize_json("input.json")  # Returns normalized data
            2/ normalize_json("input.json", "output.json")  # Returns normalized data and writes to 'output.json'
    """
    print(find_file("test.json"))
    return
    # Load JSON data from the input file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

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
            # Apply normalization for each key-value pair in the dictionary
            return {key: normalize_data(value) for key, value in data.items()}
        elif isinstance(data, list):
            # Apply normalization to each item in the list
            return [normalize_data(item) for item in data]
        elif isinstance(data, str):
            # Normalize string values only
            return normalize_text(data)
        else:
            # Return non-string values (e.g., numbers) unchanged
            return data

    # Normalize the data
    normalized_data = normalize_data(data)

    # Save the normalized data to a new JSON file if output path is specified
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(normalized_data, file, ensure_ascii=False, indent=4)

    return normalized_data
