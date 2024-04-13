import csv
import pandas as pd
import os

def parse_file(file_path):
    """Checks if a file is CSV or Excel, parses it, and returns a dictionary.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary with column names as keys and lists of values as items.

    Raises:
        ValueError: If the file format is not supported.
    """

    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == '.csv':
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Get the header row
            data = {column: [] for column in header}
            for row in reader:
                for col_name, value in zip(header, row):
                    data[col_name].append(value)

    elif file_ext in ('.xls', '.xlsx'):
        df = pd.read_excel(file_path)
        data = df.to_dict('list')

    else:
        raise ValueError(f"Unsupported file format: {file_ext}")

    return data

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    try:
        file_data = parse_file(file_path)
        print(file_data)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}") 
