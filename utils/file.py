import json


def get_json_value(file_path, key):
    """
    Read a JSON file and get the value associated with the provided key.

    Parameters:
    - file_path (str): Path to the JSON file from the root directory.
    - key (str): Key to retrieve the value.

    Returns:
    - If the key is found, returns the associated value.
    - If the key is not found or if there are any errors, returns None.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get(key, None)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# # Example usage:
# file_path = "path/to/your/file.json"  # Replace with the actual path
# key_to_retrieve = "your_key"           # Replace with the actual key
#
# value = get_json_value(file_path, key_to_retrieve)
# if value is not None:
#     print(f"The value for key '{key_to_retrieve}' is: {value}")
# else:
#     print(f"Key '{key_to_retrieve}' not found or error reading the file.")
#
