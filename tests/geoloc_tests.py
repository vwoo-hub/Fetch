import json
import os

import pytest
import geoloc_util

API_KEY = 'c2d57e7ccb9a4ee8915556a125507662'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


with open(os.path.join(DATA_DIR, "test_data.json"), "r") as test_file:
    test_data = json.load(test_file)

with open(os.path.join(DATA_DIR, "expected_data.json"), "r") as expected_file:
    expected_data = json.load(expected_file)

@pytest.mark.parametrize("location", test_data["valid_locations"])
def test_get_coordinates_by_valid_location(location):
    api_key = API_KEY
    result = geoloc_util.get_coordinates_by_location(location, api_key)
    result = json.loads(result)
    expected = expected_data[location]

    assert result['latitude'] == expected['latitude']
    assert result['longitude'] == expected['longitude']
    assert result['city'] == expected['city']
    assert result['state'] == expected['state']
    assert result['country'] == expected['country']

@pytest.mark.parametrize("location", ['San Francisco,CA,US', 'Phoenix,AZ,US', 'Las Vegas,NV,US'])
def test_get_coordinates_by_location_with_multiple_locations(location):
    api_key = API_KEY
    result = geoloc_util.get_coordinates_by_location(location, api_key)
    result = json.loads(result)
    expected = expected_data.get(location, {})

    assert result['latitude'] == expected.get('latitude')
    assert result['longitude'] == expected.get('longitude')
    assert result['city'] == expected.get('city')
    assert result['state'] == expected.get('state')
    assert result['country'] == expected.get('country')

@pytest.mark.parametrize("location", test_data["invalid_locations"])
def test_error_coordinates_by_invalid_location(location):
    api_key = API_KEY
    result = geoloc_util.get_coordinates_by_location(location, api_key)
    result = json.loads(result)
    expected = expected_data["invalid_locations"].get(location)
    assert result['error'] == expected['error']

@pytest.mark.parametrize("zip_code", test_data["valid_zip_codes"])
def test_get_coordinates_by_valid_zip_code(zip_code):
    api_key = API_KEY
    result = geoloc_util.get_coordinates_by_zip_code(zip_code, api_key)
    result = json.loads(result)
    expected = expected_data[zip_code]

    assert result['zip code'] == expected['zip code']
    assert result['latitude'] == expected['latitude']
    assert result['longitude'] == expected['longitude']
    assert result['city'] == expected['city']
    assert result['country'] == expected['country']

def test_get_coordinates_by_multiple_zip_codes():
    zip_code = ['90011', '90650', '91331']
    api_key = API_KEY
    result = geoloc_util.get_coordinates_by_zip_code(zip_code, api_key)
    result = json.loads(result)

@pytest.mark.parametrize("zip_code", test_data["invalid_zip_codes"])
def test_error_message_by_invalid_zip_code(zip_code):
    api_key = API_KEY
    result = geoloc_util.get_coordinates_by_location(zip_code, api_key)
    result = json.loads(result)
    expected = expected_data['invalid_zip_codes'].get(zip_code)

    assert result.get('location') == expected.get('zip_code')
    assert result.get('error') == expected.get('error')