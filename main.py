import uuid

from flask import Flask, url_for, redirect, request, render_template, make_response, session, abort

session_id = str(uuid.uuid4())

app = Flask(__name__)
app.secret_key = session_id


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


@app.route('/sessions')
def sessions():
    if 'username' in session:
        username = session['username']
        return f"Logged in as {username}<br> <b><a href = '/logout'>click here to log out</a></b>"

    return "You are not logged in <br><a href = '/logins'></b>click here to log in</b></a>"


@app.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('sessions'))
    return '''<form action = "" method = "post">
      <p><h3>Enter userID</h3></p>
      <p><input type = "text" name = "username"/></p>
      <p<<input type = "submit" value = "Login"/></p>
   </form>
   '''


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('sessions'))


if __name__ == '__main__':
    app.run(debug=False)
