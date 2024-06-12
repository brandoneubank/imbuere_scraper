# imbuere_scraper_package/imbuere_scraper/scraper.py
import os
from urllib.request import urlopen
from urllib.parse import quote_plus
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_nested_value(d, keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d

def fetch_url(api_key, target_url, json_elements=None):
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
                extracted_data = {}
                for elem in json_elements:
                    keys = elem.split('.')
                    extracted_data[elem] = get_nested_value(response_json, keys)
                readable_response = json.dumps(extracted_data, indent=4)
            else:
                readable_response = json.dumps(response_json, indent=4)
                
            return readable_response
        except json.JSONDecodeError:
            # If not JSON, assume it's HTML
            return response.decode('utf-8')

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch URL content using Crawlbase API.')
    parser.add_argument('url', help='The target URL to fetch content from.')
    parser.add_argument('--api-key', required=True, help='Your Crawlbase API key.')
    parser.add_argument('--json-elements', nargs='*', help='Specific JSON elements to return (use dot notation for nested keys).')

    args = parser.parse_args()

    result = fetch_url(args.api_key, args.url, args.json_elements)
    if result:
        print(result)

if __name__ == '__main__':
    main()
