from flask import Flask, request, jsonify
from mongodbtask import client_connect, data_fetch

app = Flask(__name__)


@app.route('/mongodbtask', methods=['GET', 'POST'])
def showData():

    """
    :return: mongo db data
    This function fetching the data by postman
    """
    if (request.method == 'POST'):
        user = request.json['myuser']
        password = request.json['mypassword']

    # Authentication the user

    if user == 'nesibe' and password == 'mypeople':
        client_connect()
        data = data_fetch()
        return jsonify(str(data))


if __name__ == '__main__':
    app.run(port=6000)
