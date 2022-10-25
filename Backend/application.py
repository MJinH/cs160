from flask import Flask
from flask import render_template, request, redirect, make_response, jsonify
from flask_cors import CORS, cross_origin
# from flask_cors import CORS, cross_origin

import db
import views

app = Flask(__name__)

CORS(app)
mysql = db.init(app)
views.init(app, mysql)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)