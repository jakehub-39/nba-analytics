import pandas as pd
from google.cloud import storage
from datetime import datetime
import re

def scrape_and_save_bbref_data(url, base_filename, bucket_name, destination_path):
    # Use pandas to read the HTML tables from the page
    tables = pd.read_html(url)

    # Find the desired table by index or other identification
    table = tables[0]  # Adjust the index based on the desired table

    # Extract the headers from the second row
    # headers = table.iloc[1]
    # table = table.iloc[2:]

    # # Reset the column headers using the extracted headers
    # table.columns = headers

    # Generate a timestamp string
    timestamp = datetime.now().strftime("%Y%m%d")

    # Append the timestamp to the base filename
    filename = re.sub(r"\.csv$", f"_{timestamp}.csv", base_filename)

    # Save the table data as a CSV file with headers
    table.to_csv(filename, index=False)

    # Set up Google Cloud Storage client
    client = storage.Client()

    # Define the destination blob path
    blob_name = f"{destination_path}/{filename}"

    # Upload the CSV file to the Google Cloud Storage bucket
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(filename)

    print("CSV file uploaded to Google Cloud Storage successfully.")
