# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request

import requests
app = Flask(__name__)


@app.route('/zipcode', methods=['GET'])
def getzipcode():
    dictionary = {
        "San Jose": "95112",
        "Santa Clara": "95050",
        "Fremont": "94539",
        "New York": "11368"
    }

    city = request.args.get('city')

    if city is None:
        return " Please provide valid city name"

    zipcode = dictionary.get(city)
    response = ''
    # follwoing 3 line used for indiviual serivce run
    #if zipcode is None:
    #    return f"Zip code for {city} is not found"
    #return zipcode
    
    # following lines are used to call other service based on the output of this service
    try:
        response = requests.get('http://weather-service-container:5001/weather?zipcode='+zipcode)
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the WEATHER service.')
        return zipcode
    return "weather=" + response.text + '\n'


@app.route('/')
def hello_world():
    return 'City to Zipcode'


if __name__ == '__main__':
    app.run()


