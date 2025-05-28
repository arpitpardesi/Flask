from flask import Flask, url_for, redirect, request, render_template, make_response, session, abort, flash
import uuid

app = Flask(__name__)
session_id = str(uuid.uuid4())
app.secret_key = session_id


@app.route('/')
def indexf():
    return render_template('indexf.html')


@app.route('/loginf', methods=['GET', 'POST'])
def loginf():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('indexf'))
    return render_template('loginf.html', error=error)


if __name__ == '__main__':
    app.run(debug=False)
