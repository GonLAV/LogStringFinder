import os
from file_search import scan_folder

# Function that returns the value at index 2 of a tuple
def get_third_element(t):
    return t[2]

# Function to generate an HTML report from the results
def generate_html_report(results, folder_path):
    # Sort the results by the count (third element of the tuple) in descending order
    results_sorted = sorted(results, key=get_third_element, reverse=True)
    
    # Initialize the lines of the HTML report
    report_lines = [
        "<html>",
        "<head><title>Log File Report</title></head>",
        "<body>",
        "<table border='1'>",
        "<tr><th>File Name</th><th>String</th><th>Count</th></tr>"
    ]
    
    # Iterate over each sorted result
    for file_name, string, count in results_sorted:
        # Create the full path to the file
        file_path = os.path.join(folder_path, file_name)
        # Add a row to the report for each result
        report_lines.append(
            f"<tr><td><a href='file:///{file_path}'>{file_name}</a></td>"
            f"<td>{string}</td><td>{count}</td></tr>"
        )
    
    # Add the closing tags for the HTML document
    report_lines.extend(["</table>", "</body>", "</html>"])
    
    # Write the report to an HTML file
    with open("report.html", "w", encoding='utf-8') as report_file:
        report_file.write("\n".join(report_lines))
