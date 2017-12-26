#coding:utf8
from flask import Blueprint
from flask_restful import Api, Resource, url_for


admin = Blueprint("admin",__name__)
api = Api(admin)

import app.admin.views