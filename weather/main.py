# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request


app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def getweather():
    dictionary = {
        "95112": "72F",
        "95050": "80F",
        "94539": "64F",
        "11368": "35F"
    }

    zipcode = request.args.get('zipcode')

    if zipcode is None:
        return " Please provide valid zipcode"

    weather = dictionary.get(zipcode)

    if weather is None:
        return f"Weather for {zipcode} is not found"
    return weather


@app.route('/')
def hello_world():
    return 'hello test'


if __name__ == '__main__':
    app.run()


