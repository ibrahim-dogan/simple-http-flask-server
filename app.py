# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/myservice', methods=['GET'])
def query_example():
    word = request.args.get('word')
    return word[::-1]


@app.route('/calculate', methods=['GET'])
def calculate():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a + b)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
