import os
import pandas as pd

input_folder = "input_files"
output_file = "merged_output.xlsx"

all_data = []

# Create input folder if it does not exist
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"Created folder: {input_folder}")
    print("Please put your CSV files into this folder and run the script again.")
    exit()

# Read all CSV files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)

        df = pd.read_csv(file_path)
        df["source_file"] = file_name

        all_data.append(df)

# Merge and export
if all_data:
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df.to_excel(output_file, index=False)

    print(f"Successfully merged {len(all_data)} CSV files.")
    print(f"Output saved as: {output_file}")
else:
    print("No CSV files found in the input_files folder.")