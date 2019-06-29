from flask import Flask, request, Response
import jsonpickle
from finder import *

# Initialize the Flask application
app = Flask(__name__)

# curl localhost:5000/api/test

# route http posts to this method
@app.route('/api/runewords', methods=['GET'])
def test():
    print request.headers
    runes = str(request.args.get('runes')).split(',')
    print runes
    runewords = findRunewords(runes)
    # build a response dict to send back to client
    response = {'runewords': runewords}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
