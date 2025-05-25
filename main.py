from flask import Flask, url_for, redirect, request

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
        return f'Hello {name}'

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = False)