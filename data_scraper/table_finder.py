import requests
from bs4 import BeautifulSoup

def get_table_ids(url):
    # Send a GET request to the URL and get the HTML content
    response = requests.get(url)
    html = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Find all table elements on the pagige and extract their IDs
    table_ids = [table.get('id') for table in soup.find_all('table')]

    return table_ids

# Define the URL of the basketball-reference.com page
url = "https://www.basketball-reference.com/players/p/paulch01.html"

# Call the function to get the list of table IDs
table_ids = get_table_ids(url)

# Print the list of table IDs
for table_id in table_ids:
    print(table_id)