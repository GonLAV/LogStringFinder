import os

# Function to count the occurrences of each search string in a given file
def count_strings_in_file(file_path, search_strings):
    # Open the file for reading with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Return a dictionary with the count of each search string found in the file
    return {s: content.count(s) for s in search_strings if content.count(s) > 0}

# Function to scan a folder and count the occurrences of search strings in all files
def scan_folder(folder_path, search_strings):
    results = []  # Create a list to store the results
    for root, _, files in os.walk(folder_path):  # Iterate over all directories and files in the base folder
        for file_name in files:  # Iterate over each file in the folder
            file_path = os.path.join(root, file_name)  # Create the full path to the file
            counts = count_strings_in_file(file_path, search_strings)  # Count the occurrences of the search strings in the file
            for s, count in counts.items():  # Iterate over each search string and its count in the results
                results.append((file_name, s, count))  # Add the file name, search string, and count to the results list
    return results  # Return the list of results
