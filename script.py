import os

def count_string_occurrences_in_file(file_path, search_strings):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}

    results = {}
    for search_string in search_strings:
        count = content.count(search_string)
        if count > 0:
            results[search_string] = count
    return results

def scan_folder_for_strings(folder_path, search_strings):
    results = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            occurrences = count_string_occurrences_in_file(file_path, search_strings)
            for string, count in occurrences.items():
                results.append((file_name, string, count))
    return results

def main():
    search_strings = input("Enter the strings to search for, separated by commas: ").split(',')
    folder_path = input("Enter the path to the folder containing the log files: ")

    search_strings = [s.strip() for s in search_strings]
    results = scan_folder_for_strings(folder_path, search_strings)
    
    if results:
        print(f"{'File Name':<30}{'String':<30}{'Count'}")
        for file_name, string, count in results:
            print(f"{file_name:<30}{string:<30}{count}")
    else:
        print("No occurrences found.")

if __name__ == "__main__":
    main()

