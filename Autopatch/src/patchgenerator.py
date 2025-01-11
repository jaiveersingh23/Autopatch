def generate_patch(file_path, vulnerabilities):
    with open(file_path, "r") as f:
        code_lines = f.readlines()

    for vuln in vulnerabilities:
        line_index = vuln["line"] - 1  # Convert to 0-indexed line
        if vuln["type"] == "SQL Injection":
            # Apply patch for SQL Injection (e.g., add escaping function)
            code_lines[line_index] = code_lines[line_index].replace("execute(", "execute(escape(")
        elif vuln["type"] == "XSS":
            # Apply patch for XSS (e.g., add escaping function)
            code_lines[line_index] = code_lines[line_index].replace("output(", "output(escape(")

    return "".join(code_lines)
