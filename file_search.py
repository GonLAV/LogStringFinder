import os

# This function counts the occurrences of search strings in a given file
def count_strings_in_file(file_path, search_strings):
    # Open the file for reading with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # Read the entire content of the file
    # Return a dictionary with the count of each search string found in the file
    return {s: content.count(s) for s in search_strings if content.count(s) > 0}

# This function scans a folder for occurrences of search strings in all files
def scan_folder(folder_path, search_strings):
    results = []  # Create a list to store the results
    # Walk through all directories and files in the base folder
    for root, _, files in os.walk(folder_path):
        # Iterate over each file in the folder
        for file_name in files:
            # Create the full path to the file
            file_path = os.path.join(root, file_name)
            # Count the occurrences of the search strings in the file
            counts = count_strings_in_file(file_path, search_strings)
            # Iterate over each search string and its count in the results
            for s, count in counts.items():
                # Add the file name, search string, and count to the results list
                results.append((file_name, s, count))
    return results  # Return the list of results
