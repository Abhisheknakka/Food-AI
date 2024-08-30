import pandas as pd

# Define the input file path
csv_file_path = 'D:/Food Product Project/food_dataset_updated.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

# Define the number of rows for the first and subsequent files
first_file_rows = 100
subsequent_file_rows = 24120

# Split the DataFrame into the first part with 100 rows
df_first = df.iloc[:first_file_rows]

# Save the first file
df_first.to_csv('split_file_1.csv', index=False)

# Split the remaining DataFrame into chunks of 24,000 rows each
for i in range(10):
    start_idx = first_file_rows + i * subsequent_file_rows
    end_idx = start_idx + subsequent_file_rows
    df_chunk = df.iloc[start_idx:end_idx]
    file_name = f'split_file_{i + 2}.csv'
    df_chunk.to_csv(file_name, index=False)

print("CSV files have been generated.")
