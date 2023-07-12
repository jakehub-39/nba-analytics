import os
from table_finder import get_table_ids
from scrape_data import scrape_and_save_bbref_data

# Define the URL of the basketball-reference.com page
url = "https://www.basketball-reference.com/players/p/paulch01.html"

# Call the function to get the list of table IDs
table_ids = get_table_ids(url)

# Specify the base filename, bucket name, and destination path
base_filename = "cp"
bucket_name = "nba-ref"
destination_path = "chris_paul"

# Iterate over the table IDs
for table_id in table_ids:
    # Generate a unique filename for each table
    filename = f"{base_filename}_{table_id}.csv"

    # Construct the full URL for the specific table
    table_url = f"{url}#{table_id}"

    # Call the function to scrape and save the table data
    scrape_and_save_bbref_data(table_url, filename, bucket_name, destination_path)

    print(f"Table '{table_id}' saved as '{filename}'")

# Remove the temporary CSV files
for table_id in table_ids:
    filename = f"{base_filename}_{table_id}.csv"
    os.remove(filename)

print("Temporary CSV files removed")
