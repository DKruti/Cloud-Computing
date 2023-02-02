# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request


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

    if zipcode is None:
        return f"Zip code for {city} is not found"
    return zipcode


@app.route('/')
def hello_world():
    return 'hello test'


if __name__ == '__main__':
    app.run()


