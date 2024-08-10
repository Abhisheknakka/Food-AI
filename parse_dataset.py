import pandas as pd

# Define the chunk size
chunksize = 10000  # Adjust this based on your memory capacity

# Initialize an empty list to store the filtered data
filtered_chunks = []

# Iterate through the dataset in chunks
for chunk in pd.read_csv('D:/Food Product Project/food_dataset.csv', sep='\t', usecols=['product_name', 'ingredients_text', 'countries_en'], chunksize=chunksize):
    # Filter rows where 'countries_en' is 'United States' and 'ingredients_text' is not empty
    filtered_chunk = chunk[(chunk['countries_en'] == 'United States') & (chunk['ingredients_text'].notna())]
    filtered_chunks.append(filtered_chunk)

# Concatenate all the filtered chunks into a single DataFrame
filtered_df = pd.concat(filtered_chunks, ignore_index=True)

# Now you can work with the filtered_df DataFrame
filtered_df.to_csv("D:/Food Product Project/food_dataset_updated.csv",index=False)
print(filtered_df.head())
