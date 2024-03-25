# Log Parsing Project

## Overview

The Log Parsing project involves parsing and processing data streams in real-time using Python. The script reads from standard input (stdin), handles data in a specific format, and computes metrics based on the input data.

## Project Details

- **Topic:** Log Parsing
- **Algorithm:** Python
- **Weight:** 1
- **Start Date:** Mar 25, 2024 6:00 AM
- **End Date:** Mar 29, 2024 6:00 AM
- **Checker Release:** Mar 26, 2024 6:00 AM
- **Auto Review:** Will be launched at the deadline

## Concepts Needed

- File I/O in Python
- Signal Handling in Python
- Data Processing
- Regular Expressions
- Dictionaries in Python
- Exception Handling

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- Files should end with a new line
- First line of all files should be exactly `#!/usr/bin/python3`
- Mandatory README.md file at the root of the project folder
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable
- File lengths will be tested using `wc`

## Tasks

### 0. Log Parsing (mandatory)

Write a script that reads stdin line by line and computes metrics:
- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- After every 10 lines and/or a keyboard interruption (CTRL + C), print statistics from the beginning:
  - Total file size: `File size: <total size>`
  - Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
    - If a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order

### Example

```bash
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
```

```bash
alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Additional Notes

- Follow the provided example for input generation and expected output.
- Ensure the script handles keyboard interruptions gracefully.`
