import requests
from urllib.parse import quote

# Example: Fetch Google autocomplete suggestions for a keyword
keyword = "pizza recipes"
url = f'https://api.qequals.com/v1/google-autocomplete?q={quote(keyword)}'  # URL encode keywords

# Note: Rate limiting is 2 requests per minute and 8 requests per day
response = requests.get(url)

if response.status_code == 200:
    print("Autocomplete suggestions:")
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
