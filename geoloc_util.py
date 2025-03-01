import argparse
import json
import requests

def get_coordinates_by_location(location, api_key, limit = 1):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={limit}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if data:
        result = {
            "location": location,
            "latitude": data[0]["lat"],
            "longitude": data[0]["lon"],
            "city": data[0]["name"],
            "state": data[0]["state"],
            "country": data[0]["country"],
            "localization": data[0]["local_names"]
        }
    # empty data, location invalid or not found
    else:
        result = {
            "location": location,
            "error": "Invalid location"
        }
    result = json.dumps(result, ensure_ascii=False,  indent=4)
    return result


# func that gets coords by zip (area code)
def get_coordinates_by_zip_code(zip_code, api_key):
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    # data is valid containing lat and lon keys
    if "lat" in data and "lon" in data:
        result = {
            "zip code": zip_code,
            "latitude": data["lat"],
            "longitude": data["lon"],
            "city": data["name"],
            "country": data["country"]
        }
    # data containing invalid zip code
    else:
        result = {
            "zip code": zip_code,
            "error": "Invalid zip code"
        }
    result = json.dumps(result, indent=4)
    return result

def main():
    parser = argparse.ArgumentParser(description='Geo-locator util')
    parser.add_argument('--locations', nargs='+', help='list of locations in {<city>,<state>,<country code>} or {<zip code>} format', required=True)
    parser.add_argument('--api_key', help='API key for openweathermap.org', required=True)
    args = parser.parse_args()

    for location in args.locations:
        if not location.isdigit():
            print(get_coordinates_by_location(location, args.api_key))
        else:
            print(get_coordinates_by_zip_code(location, args.api_key))

if __name__ == "__main__":
    main()

