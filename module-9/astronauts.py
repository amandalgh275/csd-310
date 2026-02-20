import requests
import json

# Function to pretty print JSON data with indentation for better readability
# This matches the tutorial's jprint function
def jprint(obj):
    # Convert Python object to formatted JSON string with sorted keys and 4-space indent
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Make a GET request to the Open Notify API to get current astronauts in space
response = requests.get("http://api.open-notify.org/astros.json")

# Print the HTTP status code to verify the request was successful (200 = success)
print(f"Status code: {response.status_code}")

# Convert the JSON response to a Python dictionary
data = response.json()

# Display the formatted astronaut data
print("\nFormatted data:")
jprint(data)

# Optional: Add more specific output to show individual astronauts
print(f"\nTotal people in space: {data['number']}")
print("Astronauts:")
for person in data['people']:
    print(f"  - {person['name']} aboard the {person['craft']}")