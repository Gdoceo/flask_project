
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p>Hello, World!</p><br><a href="/about">About</a>'

@app.route('/about')
def about():
    return '<p>This is a Flask web app running in a Linux VM.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


