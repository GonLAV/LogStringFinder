# LogStringFinder
Python script that gets 2 arguments from the user: array of strings to search and path to folder

## How to Use

1. Clone the repository:
   git clone https://github.com/username/LogStringFinder.git

Navigate to the project directory:
CMD:cd LogStringFinder

Run the script:
python script.py

Pre-condition:
PYTHON INSTALLED
Create Path : /path/App/logs 
in folder logs create 2 Files
A.log text inside:  
Error: Something went wrong
Fatal: System failure
Error: Another Fatal and another fatal
                                       
b.txt 
Error: stop now
Error my friend

Script Example:

Enter the strings to search for, separated by commas: error, Fatal

Enter the path to the folder containing the log files: /path/App/logs

File Name                     String                       Count
A.log                          error                        2
A.log                          Fatal                         3
 B.txt                         error                         1
