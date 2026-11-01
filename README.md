Discord Forensic Scanner

A lightweight Python-based forensic scanning tool designed to inspect selected local application storage directories for token-like patterns.

The project demonstrates basic file system inspection, regular expressions, directory traversal, and error handling using Python.

About the Project

Discord Forensic Scanner is an educational digital forensics project.

It examines selected Local Storage LevelDB directories associated with Discord and Google Chrome and checks whether files contain strings matching predefined token-like patterns.

For privacy and security reasons, the application does not extract, display, save, or transmit token values.

Instead, it reports the number of files containing matching patterns.

Features
Scans selected application storage directories.
Supports .ldb and .log files.
Uses regular expressions for pattern detection.
Checks Discord and Chrome storage locations.
Handles missing directories.
Handles file access errors.
Avoids displaying sensitive authentication data.
Reports matching file counts.
Uses Python's built-in libraries.
Technologies Used
Technology	Purpose
Python 3	Main programming language
os	File system operations
re	Pattern matching
Regular Expressions	Token-like pattern detection
Requirements
Python 3.8 or newer
Windows operating system
Access to the relevant application storage directories

No external Python packages are required.

Installation

Clone the repository:

bash
git clone https://github.com/Wotie1/discord-forensic-scanner.git


Navigate to the project directory:

bash
cd discord-forensic-scanner

Usage

Run the script:

bash
python scanner.py


The program checks the configured application storage directories and reports files containing matching patterns.

How It Works
Reads Windows application data directory paths.
Locates the configured Local Storage LevelDB directories.
Enumerates .ldb and .log files.
Reads accessible files.
Checks file contents against predefined regular expression patterns.
Counts files containing matching patterns.
Displays a summary without exposing sensitive values.
Limitations
Designed primarily for Windows.
Only checks predefined application storage locations.
Only examines .ldb and .log files.
Pattern matches do not prove that a valid authentication token exists.
Does not verify token validity.
Does not identify the account associated with a match.
Results depend on file permissions and application storage availability.
Privacy and Security

This project is designed for educational digital forensics.

It does not collect, export, or display authentication credentials.

All scanning operations are performed locally.

Only inspect application data that belongs to you or that you are explicitly authorized to examine.

Future Improvements

Potential improvements include:

JSON report generation.
File modification timestamp reporting.
Configurable scan directories.
Improved forensic logging.
Additional safe indicator patterns.
A graphical user interface.

These features are proposed improvements and may not be available in the current version.

Contributing

Suggestions, bug reports, and improvements are welcome.

Feel free to open an issue or submit a pull request.

License

This project is intended to be released under the MIT License.

Include a LICENSE file in the repository before publishing under this license.

Author

YOUR NAME

GitHub: https://github.com/Wotie1