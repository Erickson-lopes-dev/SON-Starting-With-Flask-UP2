from flask import Flask, jsonify, request, url_for, redirect, make_response, render_template

app = Flask(__name__)


@app.route('/<name>/<int:id>/', methods=['GET', 'POST'])
def main_x(name, id):
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

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        return redirect(url_for('result', name=request.form['name']))


@app.route('/result/<name>', methods=['GET'])
def result(name):
    return render_template('index.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


if __name__ == '__main__':
    app.run(debug=True, port=8000)
