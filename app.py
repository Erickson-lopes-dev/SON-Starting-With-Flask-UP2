from flask import Flask, jsonify, request, url_for, redirect, make_response

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
    print(request.form['person'])
    return jsonify({'message': f'Nome recebido {request.form["person"]}'})


@app.route('/redirected', methods=['GET'])
def redirected():
    data = {
        'message': 'Redirect',
        'username': 'Erickson',
        'stacks': ['python', 'django', 'flask']
    }
    return jsonify(user=data)


@app.route('/response/', methods=['POST'])
def response_data():
    # return redirect(url_for('redirected'))
    resp = make_response(jsonify(data=request.form), 201)
    resp.headers['Couse-Powered-by'] = 'School of net Erickson'
    return resp
# app.add_url_rule('/', 'hello', main)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
