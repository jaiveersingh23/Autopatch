# AutoPatch

AutoPatch is an AI-driven tool that scans Python source code for common vulnerabilities like SQL Injection and XSS and automatically generates patched versions to mitigate those vulnerabilities.

## Features
- Detects common vulnerabilities (SQL Injection, XSS) in Python code.
- Automatically generates patched code by applying safe practices (e.g., escaping inputs).
- Lightweight, easy to use, and customizable for future vulnerabilities.

## Installation

### 1. Clone the repository:
```bash
git clone <URL>
cd AutoPatch
```

### 2. Install dependencies:
Make sure you have Python 3.6+ installed. Then, install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

### Scan a file for vulnerabilities:
```bash
python src/autopatch.py <file_path>
```

For example:
```bash
python src/autopatch.py test_files/test_vulnerable_code.py
```

### Output:
The script will output any vulnerabilities detected and create a patched version of the file named `<original_filename>_patched.py`.

### Example:
- Original file: `test_files/test_vulnerable_code.py`
- Patched file: `test_files/test_vulnerable_code_patched.py`

## Directory Structure
- **`src/`**: Source code files, including core functionality for vulnerability scanning and patching.
- **`tests/`**: Unit tests for the scanning and patch generation logic.
- **`data/`**: Vulnerability patterns (signatures) used by the scanner.
- **`test_files/`**: Sample Python files containing vulnerabilities for testing purposes.

## License
This project is licensed under the MIT License.
```

Just replace `<URL>` with the actual URL of your repository. This will give users a complete guide for setting up and using your project.
