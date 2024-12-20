import json

def load_data(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        dict: The data loaded from the JSON file.

    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def load_sample_data():
    return load_data('../data/sample_itinerary.json')
