import csv
import os
import sys
from datetime import datetime

# --- Configuration ---
# The output directory is now hardcoded to the user's Desktop.
# This finds the Desktop path on any Windows computer.
output_directory = os.path.join(os.path.expanduser('~'), 'Desktop')
# --- End of Configuration ---

# Check if a file path was provided as an argument when the script was run.
# sys.argv is a list of command-line arguments. 
# sys.argv[0] is the script name itself, sys.argv[1] is the first argument.
if len(sys.argv) < 2:
    print("Error: No input file provided.")
    print("Usage: Drag and drop a file onto the .bat file or run from cmd with a file path.")
    # In a batch file context, 'input()' will pause the window.
    input("Press Enter to exit...") 
    sys.exit()

input_filename = sys.argv[1]

# Check if the provided input file actually exists.
if not os.path.exists(input_filename):
    print(f"Error: Input file '{input_filename}' not found.")
    input("Press Enter to exit...")
    sys.exit()

# --- Generate the dynamic output filename ---
# Get the current date and time
now = datetime.now()
# Format the date as YYYY-MM-DD
date_str = now.strftime("%Y-%m-%d")
# Get the time as total seconds since the epoch (ensures a unique number)
time_in_seconds = int(now.timestamp())
# Construct the filename
# Note: We use .csv because it's the best format for Excel.
# If you truly need .txt, just change the extension here.
output_filename = f"parameter-export-{date_str}-{time_in_seconds}.csv"
# Combine the directory and filename to create the full path
full_output_path = os.path.join(output_directory, output_filename)


# The rest of the processing logic remains the same as before
processed_data = []

with open(input_filename, 'r') as f:
    lines = f.readlines()

# Rule for Line 1
if len(lines) > 0:
    processed_data.append(["Line 1 Text", lines[0].strip()])

# Rule for Line 2
if len(lines) > 1:
    parts = lines[1].strip().split(':', 1)
    if len(parts) == 2:
        processed_data.append([parts[0].strip(), parts[1].strip()])

# Rule for Line 3
if len(lines) > 2:
    items = lines[2].strip().split(',')
    for item in items:
        if item.strip():
            parts = item.strip().split(':', 1)
            if len(parts) == 2:
                processed_data.append([parts[0].strip(), parts[1].strip()])

# --- Write the processed data to the new CSV file on the Desktop ---
with open(full_output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Header', 'Value'])
    writer.writerows(processed_data)

print(f"Success! Conversion complete.")
print(f"Output saved to: {full_output_path}")