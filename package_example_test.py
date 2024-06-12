# package_example_test.py
from imbuere_scraper import fetch_url

# Replace with your actual API key and target URL
API_KEY = 'mY5KrlQnQYw-dhzAh5ATAw'
TARGET_URL = 'https://www.blueally.com/solutions-overview/'



# Optional: Specify the JSON elements you want to extract (using dot notation for nested keys)
JSON_ELEMENTS = ['body.title', 'body.content']

# Fetch the URL content, extracting specified JSON elements
response_data = fetch_url(API_KEY, TARGET_URL, JSON_ELEMENTS)

# Print the response data
print(response_data)
