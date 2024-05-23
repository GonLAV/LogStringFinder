from file_search import scan_folder
from report_generator import generate_html_report

# Main function to interact with the user and generate the report
def main():
    # Get the search strings from the user, separated by commas, and remove any extra whitespace
    search_strings = [s.strip() for s in input("Enter the strings to search for, separated by commas: ").split(',')]
    # Get the path to the folder containing the log files from the user
    folder_path = input("Enter the path to the folder containing the log files: ")

    # Scan the folder for the search strings and get the results
    results = scan_folder(folder_path, search_strings)
    # Generate the HTML report from the results
    generate_html_report(results, folder_path)
    print("Report generated: report.html")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
