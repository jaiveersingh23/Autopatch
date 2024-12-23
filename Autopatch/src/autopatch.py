import argparse
from vulnerability_scanner import scan_code
from patch_generator import generate_patch

def main():
    parser = argparse.ArgumentParser(description="AutoPatch: AI-Based Code Vulnerability Patcher")
    parser.add_argument("file", type=str, help="Path to the source code file to scan")
    args = parser.parse_args()

    code_file = args.file

    print(f"Scanning file: {code_file}")
    vulnerabilities = scan_code(code_file)

    if not vulnerabilities:
        print("No vulnerabilities found!")
    else:
        print("\nVulnerabilities detected:")
        for vuln in vulnerabilities:
            print(f"- {vuln['type']} at line {vuln['line']}: {vuln['description']}")
        
        print("\nGenerating patches...")
        patched_code = generate_patch(code_file, vulnerabilities)
        patched_file = code_file.replace(".py", "_patched.py")
        
        with open(patched_file, "w") as f:
            f.write(patched_code)
        
        print(f"Patched file created: {patched_file}")

if __name__ == "__main__":
    main()
