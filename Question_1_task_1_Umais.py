import os
import csv

# Use one of these options for the path
csv_directory = r"C:\Users\User\OneDrive - Charles Darwin University\HIT137_2023_S2_groupCAS076_Ass1"

# Output text file
output_txt = 'output_csv.txt'

# Function to extract text from all CSV files and store in a .txt file
def extract_text_from_csvs(csv_directory, output_txt):
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        # Iterate over all CSV files in the directory
        for file_name in os.listdir(csv_directory):
            if file_name.endswith('.csv'):
                file_path = os.path.join(csv_directory, file_name)
                # Read CSV file
                try:
                    with open(file_path, 'r', encoding='utf-8') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        # Write each row as text to the output file
                        for row in csv_reader:
                            row_text = ' '.join(row)  # Join the values as a single string
                            txt_file.write(row_text + '\n')  # Write row text to the txt file
                except Exception as e:
                    print(f"Error reading {file_name}: {e}")

# Call the function
extract_text_from_csvs(csv_directory, output_txt)