# Fetch assessment
A command line utility that retrieves longitude and latitude coordinates, and other location information based on user input.

* Prereqs:
  * Install dependencies
    * Run the following command in the root directory of the project:
      * ` pip install -r requirements.txt`


* Running the util:
  * From the root directory of the project, run any of the following commands:
    * `python geoloc_util.py --locations "San Francisco","CA","US" --api_key c2d57e7ccb9a4ee8915556a125507662`
    * `python geoloc_util.py --locations "94404" --api_key c2d57e7ccb9a4ee8915556a125507662`
  * You can also mix and match locations and/or zip codes together in a single command:
    * `python geoloc_util.py --locations "San Francisco","CA","US" "95014" "90007" "Miami","FL","US" --api_key c2d57e7ccb9a4ee8915556a125507662`


* Running the tests:
  * Run the following command in the root directory of the project:
    * `python -m pytest tests/geoloc_tests.py`