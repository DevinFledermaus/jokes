from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Chuck Norris Joke: </strong>" + response['value']


@app.route('/ting', methods=["GET"])
def get_chuck_norris_response():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Chuck Norris Joke: </strong><br>{}".format(response)


@app.route('/categories', methods=["GET"])
def get_chuck_norris_categories():
    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()

    return "<strong>Chuck Norris Joke Categories: </strong><br>{}".format(response)


if __name__ == "__main__":
    app.debug = True
    app.run()
