#coding:utf8
from flask import Flask
from flask import Blueprint,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,url_for

import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True 
app.config["SECRET_KEY"] = "fca3a1f7d808434f892e45f8bd70e86d"
# app.debug = True

db = SQLAlchemy(app)


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"),404