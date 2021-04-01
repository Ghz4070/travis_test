from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world !"


@app.route('/hello/<name>')
def hello_world(name):
    return str('Your slug is : ' + name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
