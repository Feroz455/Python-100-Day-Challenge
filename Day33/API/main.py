import requests

try:
    # Send a GET request to the URL
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response into a dictionary
        longitude = float(data["iss_position"]["longitude"])
        latitude = float(data["iss_position"]["latitude"])
        
        # Create a tuple with longitude and latitude
        coordinates = (longitude, latitude)
        
        # Print the coordinates as a tuple
        print(f"Coordinates: {coordinates}")
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
