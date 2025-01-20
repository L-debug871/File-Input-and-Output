print("***** Program Trace Utility *****")

filename = input("Enter the name of the program file: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    has_trace_statements = lines[0].strip() == '"""DEBUG"""'
    modified_lines = []

    for i, line in enumerate(lines):
        # If the first line is a debug statement, skip it
        if has_trace_statements and line.strip() == '"""DEBUG"""':
            continue

        # Add the line to modified lines
        modified_lines.append(line)

        # Check if the line defines a function
        if line.startswith("def"):
            func_name = line.split("(")[0][4:].strip()
            debug_statement = f'    """DEBUG""";print(\'{func_name}\')\n'
            
            # Ensure we don't add the debug statement if it's already present
            if len(modified_lines) > 1 and modified_lines[-2].strip() != debug_statement.strip():
                modified_lines.append(debug_statement)

    if has_trace_statements:
        print("Program contains trace statements")
    else:
        print("Inserting...Done")

    with open(filename, "w") as file:
        file.writelines(modified_lines)
except FileNotFoundError:
    print(f"File '{filename}' does not exist.")
