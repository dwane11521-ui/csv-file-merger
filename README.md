# CSV File Merger

A simple Python tool for merging multiple CSV files into one Excel file.

This script reads all CSV files from an input folder, combines them into a single table, and exports the result as an Excel file.

## Features

- Read multiple CSV files
- Merge all files into one table
- Add a `source_file` column to track where each row came from
- Export the merged result to Excel
- Simple and beginner-friendly Python script

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Use

1. Run the script once:

```bash
python main.py
```

2. The script will create a folder called:

```text
input_files
```

3. Put your CSV files into the `input_files` folder.

4. Run the script again:

```bash
python main.py
```

5. The merged file will be saved as:

```text
merged_output.xlsx
```

## Example

Input folder:

```text
input_files/
```

Example files:

```text
customers_1.csv
customers_2.csv
orders.csv
```

Output file:

```text
merged_output.xlsx
```

## What This Project Demonstrates

This project shows basic skills in:

- Python automation
- CSV data processing
- Excel export
- Pandas
- File handling
- GitHub project workflow

## Notes

This tool does not modify the original CSV files.  
It creates a new merged Excel file.
