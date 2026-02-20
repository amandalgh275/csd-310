import requests
import json

# Reuse the pretty print function from the tutorial
def jprint(obj):
    """Format and print JSON data with indentation"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Step 6b: Test the connection to API
# Using the Dog API - returns random dog images
api_url = "https://dog.ceo/api/breeds/image/random"
print("Testing connection to Dog API...")
response = requests.get(api_url)
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    print("Connection successful!\n")
    
    # Step 6c: Print the response with NO formatting
    print("=" * 50)
    print("STEP 6c: RESPONSE WITH NO FORMATTING")
    print("=" * 50)
    print(response.json())
    print("\n")
    
    # Step 6d: Print the response WITH formatting (like the tutorial)
    print("=" * 50)
    print("STEP 6d: RESPONSE WITH FORMATTING")
    print("=" * 50)
    jprint(response.json())
    
    # Bonus: Extract and display just the image URL
    data = response.json()
    print(f"\nRandom dog image URL: {data['message']}")
    
else:
    print(f"Connection failed with status code: {response.status_code}")
