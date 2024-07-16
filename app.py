from flask import Flask
import os

app = Flask(__name__)

from routes import routes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)