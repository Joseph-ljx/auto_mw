import pandas as pd
import json

csv_file_path = 'CTA_backbone.csv'
df = pd.read_csv(csv_file_path)

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', indent=4)

# Write JSON to a file
json_file_path = 'CTA_backbone.json'  # Replace with your output file path
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Data has been successfully written to {json_file_path}")