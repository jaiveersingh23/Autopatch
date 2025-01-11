import argparse
from vulnerability_scanner import scan_code
from patch_generator import generate_patch

def main():
    parser = argparse.ArgumentParser(description="AutoPatch: AI-Based Code Vulnerability Patcher")
    parser.add_argument("file", type=str, help="Path to the source code file to scan")
    args = parser.parse_args()

    code_file = args.file

    print(f"Scanning file: {code_file}")
    try:
        vulnerabilities = scan_code(code_file)
    except Exception as e:
        print(f"Error scanning file: {e}")
        return

    if not vulnerabilities:
        print("No vulnerabilities found!")
    else:
        print("\nVulnerabilities detected:")
        for vuln in vulnerabilities:
            print(f"- {vuln['type']} at line {vuln['line']}: {vuln['description']}")
        
        print("\nGenerating patches...")
        try:
            patched_code = generate_patch(code_file, vulnerabilities)
        except Exception as e:
            print(f"Error generating patch: {e}")
            return

        patched_file = code_file.replace(".py", "_patched.py")
        
        try:
            with open(patched_file, "w") as f:
                f.write(patched_code)
            print(f"Patched file created: {patched_file}")
        except Exception as e:
            print(f"Error writing patched file: {e}")

if __name__ == "__main__":
    main()
