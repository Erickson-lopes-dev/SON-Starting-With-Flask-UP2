from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {'Olá mundo': 'message0'}, 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)
