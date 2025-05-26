from flask import Flask, url_for, redirect, request, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route('/admin')
def admin():
    return 'Hello Admin'


@app.route('/hello/<name>')
def helloname(name):
    if name.lower() == 'arpit':
        return redirect(url_for('admin'))
    else:
        return render_template('hello.html', name=name)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/student')
def student():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

        resp = make_response(render_template('readcookie.html', user=user))
        resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return f'<h1>welcome {name} </h1>'

if __name__ == '__main__':
    app.run(debug=False)
