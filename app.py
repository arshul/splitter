from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
if __name__ == "__main__":
    app.run()

import smz.views
