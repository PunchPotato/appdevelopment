import requests

# Replace these with your actual API credentials
api_id = "ca2310a8"
api_key = "e105fb826a5867dd4102a90223738264	"

# Base URL for the Nutritionix API
base_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

# Example input text
input_text = "apple"

# Construct headers with API credentials
headers = {
    "x-app-id": api_id,
    "x-app-key": api_key
}

# Construct request parameters
params = {
    "query": input_text
}

# Make the API request
response = requests.post(base_url, headers=headers, params=params)

# Process the response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)