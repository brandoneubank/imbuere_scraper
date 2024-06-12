# imbuere_scraper_package/imbuere_scraper/scraper.py
import os
from urllib.request import urlopen
from urllib.parse import quote_plus
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_and_save_url(api_key, target_url, json_elements=None):
    # URL encode the target URL
    encoded_url = quote_plus(target_url)

    # Construct the API request URL
    request_url = f'https://api.crawlbase.com/scraper?token={api_key}&url={encoded_url}'

    try:
        # Open the URL and read the response
        handler = urlopen(request_url)
        response = handler.read()

        # Try to decode the response as JSON
        try:
            response_json = json.loads(response)
            
            if json_elements:
                # Extract only the specified JSON elements
                extracted_data = {key: response_json.get(key) for key in json_elements}
                readable_response = json.dumps(extracted_data, indent=4)
            else:
                readable_response = json.dumps(response_json, indent=4)
                
            file_extension = 'json'
        except json.JSONDecodeError:
            # If not JSON, assume it's HTML
            readable_response = response.decode('utf-8')
            file_extension = 'html'

        # Save the response to a file
        filename = f'response.{file_extension}'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(readable_response)
            logging.info(f"Response has been saved to {filename}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch and save URL content using Crawlbase API.')
    parser.add_argument('url', help='The target URL to fetch content from.')
    parser.add_argument('--api-key', required=True, help='Your Crawlbase API key.')
    parser.add_argument('--json-elements', nargs='*', help='Specific JSON elements to return.')

    args = parser.parse_args()

    fetch_and_save_url(args.api_key, args.url, args.json_elements)

if __name__ == '__main__':
    main()
