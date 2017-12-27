#coding:utf8
from . import admin,api
from flask import render_template,redirect,url_for,jsonify,request,abort
from app.admin.forms import LoginForm
import json
# from flask.ext import restful
from flask_restful import reqparse, abort, Api, Resource
from app import db

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class HelloWorld(Resource):
    def get(self,getid):
        return {'hello': getid}


api.add_resource(HelloWorld, '/getid/<string:getid>')

class Posttest(Resource):

    def post(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('user', type=str , required=True, help='user cannot be converted')
        # parser.add_argument('User-Agent', type=str, location='headers') //header参数
        # parser.add_argument('name', type=int, location='form') // 表单
        # parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files') //From file uploads
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        getstr = args["user"]
        passw = args["password"]
        return {"whatyourpost":getstr,"pwd":passw}

api.add_resource(Posttest,"/userlogin")






















@admin.route("/",methods=["GET","POST"])
def index():

    if not request.json or not "title" in request.json:
        abort(404)

    print(request.json["title"])
    return jsonify({"ni":"dsadsadasdasd"})
    # return render_template("admin/index.html")

@admin.route("/login/<int:task_id>",methods=["GET","POST"])
def login(task_id):
    form = LoginForm
    asd = [1,2,3,4,5,6,7,8,9,0]
    asd.append(task_id)
    return jsonify({"asd":asd})
    # return json.dumps(asd)
    # return render_template("admin/login.html", form = form)

@admin.route("/logout/",methods=["POST"])
def logout(resource):

    # if not request.json or not "title" in request.json:
    #     abort(404)

    # print(request.json["title"])
    return jsonify({"ni":"dsadsadasdasd"})
    # return redirect(url_for("admin.login"))

@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")

@admin.route("/tag/add/")
def tag_add():
    return render_template("admin/tag_add.html")

@admin.route("/tag/list/")
def tag_list():
    return render_template("admin/tag_list.html")

@admin.route("/movie/add/")
def movie_add():
    return render_template("admin/movie_add.html")

@admin.route("/movie/list/")
def movie_list():
    return render_template("admin/movie_list.html")

@admin.route("/preview/add/")
def preview_add():
    return render_template("admin/preview_add.html")

@admin.route("/preview/list/")
def preview_list():
    return render_template("admin/preview_list.html")

@admin.route("/user/list/")
def user_list():
    return render_template("admin/user_list.html")

@admin.route("/user/view/")
def user_view():
    return render_template("admin/user_view.html")

@admin.route("/comment/list/")
def comment_list():
    return render_template("admin/comment_list.html")

@admin.route("/moviecol/list/")
def moviecol_list():
    return render_template("admin/moviecol_list.html")

@admin.route("/oplog/list/")
def oplog_list():
    return render_template("admin/oplog_list.html")

@admin.route("/adminloginlog/list/")
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")

@admin.route("/userloginlog/list/")
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")

@admin.route("/role/add/")
def role_add():
    return render_template("admin/role_add.html")

@admin.route("/role/list/")
def role_list():
    return render_template("admin/role_list.html")

@admin.route("/auth/add/")
def auth_add():
    return render_template("admin/auth_add.html")

@admin.route("/auth/list/")
def auth_list():
    return render_template("admin/auth_list.html")

@admin.route("/admin/add/")
def admin_add():
    return render_template("admin/admin_add.html")

@admin.route("/admin/list/")
def admin_list():
    return render_template("admin/admin_list.html")