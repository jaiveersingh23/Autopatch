# AutoPatch

AutoPatch is an AI-driven tool that scans Python source code for common vulnerabilities like SQL Injection and XSS and generates patched versions automatically.

## Features
- Detects common vulnerabilities in Python code.
- Automatically generates patched code.
- Lightweight and easy to use.

## Installation

1. Clone the repository:
2. git clone <URL> cd AutoPatch

2. Install dependencies:

pip install -r requirements.txt

## Usage

Scan a file for vulnerabilities:

python src/autopatch.py <file_path>

Example:

python src/autopatch.py test_files/test_vulnerable_code.py

## Directory Structure

- `src/`: Source code files.
- `tests/`: Unit tests.
- `data/`: Vulnerability patterns.

## License
This project is licensed under the MIT License.


---
