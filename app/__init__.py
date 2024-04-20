from flask import Flask
from app.functions import generate_quotes

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Fortune Cookie API!"

@app.route('/get_quotes')
def get_quotes():
    return generate_quotes()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')