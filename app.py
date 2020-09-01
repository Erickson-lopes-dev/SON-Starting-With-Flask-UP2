from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/<name>/<int:id>/', methods=['GET', 'POST'])
def main(name, id):
    print(request.data)
    return f'hello {name}, com o id {id}', 200


@app.route('/request/', methods=['POST'])
def request_data():
    print(request.method)
    print(request.headers.get('User-Agent'))
    # print(request.headers)
    print(request.path)
    print(request.data)
    print(request.args.get('person'))
    return jsonify({'message': 'recebido'})

# app.add_url_rule('/', 'hello', main)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
