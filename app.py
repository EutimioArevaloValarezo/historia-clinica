from flask import Flask
from flask_toastr import Toastr
import os

app = Flask(__name__)
toastr = Toastr(app)

from routes import routes

if __name__ == '__main__':
    toastr.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)