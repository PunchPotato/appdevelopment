import requests
import os

query = '10 grams of kitkat'
api_key = os.environ.get('MY_API_KEY')  # Replace this with your actual API key
api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
headers = {'X-Api-Key': api_key}

response = requests.get(api_url, headers=headers)

if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)