import csv
import os

# --- Configuration ---
# Set the name of your input file
input_filename = "input.txt" 
# Set the name for the clean, organized output file
output_filename = "output.csv" 
# --- End of Configuration ---

# A list to hold all our final rows of data
processed_data = []

# Check if the input file actually exists before we start
if not os.path.exists(input_filename):
    print(f"Error: Input file '{input_filename}' not found.")
    print("Please make sure the file is in the same directory as the script.")
    exit()

# Open and read the input file
with open(input_filename, 'r') as f:
    lines = f.readlines()

# --- Process each line according to its specific rule ---

# Rule for Line 1: Uncategorized text
if len(lines) > 0:
    # We assign a generic header for the first line
    header = "Heading Line 1"
    value = lines[0].strip() # .strip() removes any extra whitespace or newlines
    processed_data.append([header, value])

# Rule for Line 2: Single "Header: Value"
if len(lines) > 1:
    # Split the line only on the first colon to handle colons in the text
    parts = lines[1].strip().split(':', 1)
    if len(parts) == 2:
        header = parts[0].strip()
        value = parts[1].strip()
        processed_data.append([header, value])

# Rule for Line 3: Multiple comma-separated "Header: Value" pairs
if len(lines) > 2:
    # First, split the entire line by commas
    items = lines[2].strip().split(',')
    for item in items:
        # Ignore any empty parts that might result from a trailing comma
        if item.strip():
            # Split each part by the first colon
            parts = item.strip().split(':', 1)
            if len(parts) == 2:
                header = parts[0].strip()
                value = parts[1].strip()
                processed_data.append([header, value])

# --- Write the processed data to a new CSV file ---
with open(output_filename, 'w', newline='') as f:
    writer = csv.writer(f)
    # Write the column titles for our new table
    writer.writerow(['Header', 'Value'])
    # Write all the data rows we collected
    writer.writerows(processed_data)

print(f"Success! Processed '{input_filename}' and saved the results to '{output_filename}'.")