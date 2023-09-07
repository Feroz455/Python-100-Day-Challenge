import requests

# Function to get the user's location based on IP address
def get_location():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching location data: {e}")
        return None

# Get the user's location data
location_data = get_location()

# Check if location data was successfully retrieved
if location_data:
    city = location_data['city']
    region = location_data['region']
    country = location_data['country']
    print(f"Location: {city}, {region}, {country}")

    # Replace 'YOUR_LocationApiKey' with your actual OpenCage API key
    LocationApiKey = '56230049223842e1aed81193d541a933'

    # Define the city name for which you want to get coordinates
    city_name = location_data["city"]  # Replace with your desired city name

    # Construct the API request URL for OpenCage Geocoding
    url = f'https://api.opencagedata.com/geocode/v1/json?q={city_name}&key={LocationApiKey}'

    try:
        # Send a GET request to the OpenCage Geocoding API
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response into a dictionary
            
            # Extract latitude and longitude from the response
            first_result = data['results'][0]  # Get the first result
            lat = first_result['geometry']['lat']
            lon = first_result['geometry']['lng']
            
            # Print the coordinates
            print(f'Latitude: {lat}, Longitude: {lon}')

            # Replace '0b3d8e2a82bd791db1f3529be52f4274' with your actual API key
            api_key = "0b3d8e2a82bd791db1f3529be52f4274"

            # Construct the URL with the API key and coordinates
            url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}"
            print(url)

            # Make a GET request to the API
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                data = response.json()  # Parse the JSON response into a dictionary
                # Now you can work with the weather data
                print(data)
            else:
                # Print an error message if the request was not successful
                print(f"Error: {response.status_code}")
        else:
            # Print an error message if the OpenCage Geocoding request was not successful
            print(f'Error: Unable to retrieve coordinates (HTTP Status Code: {response.status_code})')
    except Exception as e:
        print(f'An error occurred while fetching coordinates: {str(e)}')
