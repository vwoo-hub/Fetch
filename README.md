# Fetch assessment
A command line utility that retrieves longitude and latitude coordinates, and other location information based on user input.

* Prereqs:
  * Clone this repository:
    * `git clone https://github.com/vwoo-hub/Fetch.git`
  * Create python env in the project root directory:
    * `python3 -m venv venv`
    * `source venv/bin/activate`
  * Install dependencies
    * Run the following command in the root directory of the project:
      * ` pip install -r requirements.txt`


* Running the util:
  * Make sure you have an active API key, which you'll sub in as <API_KEY> below
  * In the project root directory, run any of the following commands:
    * `python geoloc_util.py --locations "San Francisco","CA","US" --api_key <API_KEY>`
    * `python geoloc_util.py --locations "94404" --api_key <API_KEY>`
  * You can also mix and match locations and/or zip codes together in a single command:
    * `python geoloc_util.py --locations "San Francisco","CA","US" "95014" "90007" "Miami","FL","US" --api_key <API_KEY>`


* Running the tests:
  * In the project root directory, run the following command:
    * `python -m pytest tests/geoloc_tests.py`