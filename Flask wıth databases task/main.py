from flask import Flask, request, jsonify
from sqlite import conn_sqlite, fetching_data

app = Flask(__name__)

@app.route('/show-sqlite',methods = ['GET', 'POST'] )
def showData():
    """
    :return: sqlite data is returned
    This function is for fetching the data from
    sqlite  already inserted by sqlite file
    """
    if (request.method == 'POST'):
        user = request.json['myuser']
        password = request.json['mypassword']

    # Validating the user and password
    if user =='nesibe' and password =='hello':
        conn_sqlite()
        data = fetching_data()
        return jsonify(str(data))

if __name__ == '__main__':
    app.run(port = 6000)






