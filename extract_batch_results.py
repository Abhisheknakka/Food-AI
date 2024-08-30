import json
import csv

# Define the result file and the output CSV file
result_file_name = 'D:/Food Product Project/batch_11_2_output.jsonl'
output_csv_file = 'D:/Food Product Project/batch_11_2_results.csv'

# Open the output CSV file for writing
with open(output_csv_file, 'w', newline='', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header
    csv_writer.writerow(['analysis'])
    
    # Open the result file and process each line
    with open(result_file_name, 'r') as file:
        for line in file:
            # Parsing the JSON string into a dict
            output = json.loads(line.strip())
            # Extract the GPT response
            gpt_response = output["response"]["body"]["choices"][0]["message"]["content"]
            # Write the GPT response as a new row in the CSV
            csv_writer.writerow([gpt_response])

print(f"CSV file generated at {output_csv_file}")
