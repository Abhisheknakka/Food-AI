import pandas as pd
import json

# Define the input and output file paths
csv_file_path = 'D:/Food Product Project/split_file_11.csv'
json_file_path = 'D:/Food Product Project/request_chunk_11.jsonl'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Open the JSON file for writing
with open(json_file_path, 'w') as json_file:
    # Iterate over each row in the DataFrame
    for idx, row in df.iterrows():
        ingredients = row['ingredients']
        prompt = f"""Imagine you are a highly trained nutritionist with a great knowledge of food ingredients and their effects. Mention the positive and negative things about the following ingredients with a focus on preservatives and ingredients causing negative health effects. Ingredients: {ingredients}. Answer to the point in 5 to 6 lines in the following format `Positive: Positive things\nNegative: Negative things`."""
        json_object = {
            "custom_id": f"request-{idx+1}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-3.5-turbo-0125",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        }
        # Write the JSON object to the file, one per line
        json_file.write(json.dumps(json_object) + '\n')

print(f"JSON file generated at {json_file_path}")
