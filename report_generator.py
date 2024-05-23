import os
from file_search import scan_folder

# Function to generate an HTML report from the results
def generate_html_report(results, folder_path):
    results_sorted = sorted(results, key=lambda x: x[2], reverse=True)  # Sort the results by count in descending order
    report_lines = [
        "<html>",
        "<head><title>Log File Report</title></head>",
        "<body>",
        "<table border='1'>",
        "<tr><th>File Name</th><th>String</th><th>Count</th></tr>"
    ]
    
    for file_name, string, count in results_sorted:  # Iterate over each sorted result
        file_path = os.path.join(folder_path, file_name)  # Create the full path to the file
        report_lines.append(
            f"<tr><td><a href='file:///{file_path}'>{file_name}</a></td>"
            f"<td>{string}</td><td>{count}</td></tr>"
        )
    
    report_lines.extend(["</table>", "</body>", "</html>"])  # Add the closing tags for the HTML document
    
    with open("report.html", "w", encoding='utf-8') as report_file:  # Write the report to an HTML file
        report_file.write("\n".join(report_lines))
