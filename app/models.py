#coding:utf8
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db
# import pymysql

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/movie"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True 

# db = SQLAlchemy(app)

#会员

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    phone = db.Column(db.String(11),unique=True)
    info = db.Column(db.Text(100))
    face = db.Column(db.String(225),unique=True)
    datetime = db.Column(db.DateTime,index=True,default=datetime.now)
    uuid = db.Column(db.String(225),unique=True)

    userlogs = db.relationship("Userlog",backref="user")
    comments = db.relationship("Comment",backref="user")
    moviecols = db.relationship("Moviecol",backref="user")

    def __repr__(self):
        return "<User %r>" % self.name

#会员登陆日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Userlog %r>" % self.id

#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)
    movies = db.relationship("Movie",backref="tag")

    def __repr__(self):
        return "<Tag %r>" % self.name

#电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),unique=True)
    url = db.Column(db.String(255),unique=True)
    info = db.Column(db.Text(255))
    logo = db.Column(db.String(255),unique=True)
    star = db.Column(db.Integer)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer,db.ForeignKey("tag.id"))
    area = db.Column(db.String(255))
    release_time = db.Column(db.DateTime,index=True,default=datetime.now)
    length = db.Column(db.String(255))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)

    comments = db.relationship("Comment",backref="movie")
    moviecols = db.relationship("Moviecol",backref="movie")

    def __repr__(self):
        return "<Movie %r>" % self.title

#预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),unique=True)
    logo = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Preview %r>" % self.title

#评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text(255))
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)
    movie_id = db.Column(db.Integer,db.ForeignKey("movie.id"))

    def __repr__(self):
        return "<Comment %r>" % self.id

#收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)
    movie_id = db.Column(db.Integer,db.ForeignKey("movie.id"))

    def __repr__(self):
        return "<Moviecol %r>" % self.id

#权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    url = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Auth %r>" % self.name


#角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    auths = db.Column(db.String(600))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)
    admins = db.relationship("Admin",backref="role")

    def __repr__(self):
        return "<Role %r>" % self.name

#管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer,db.ForeignKey("role.id"))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)
    adminlog = db.relationship("Adminlog",backref="admin")
    oplog = db.relationship("Oplog",backref="admin")

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd,pwd)
        

#管理员登陆日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer,primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey("admin.id"))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Adminlog %r>" % self.id

#操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer,primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey("admin.id"))
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(600))
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Oplog %r>" % self.id

# mysql.server start
# mysql -urrot -p

# if __name__ == "__main__":
#     # db.create_all()
#     # role = Role(
#     #     name="超级管理员",
#     #     auths=""
#     # )
#     # db.session.add(role)
#     # db.session.commit()

#     from werkzeug.security import generate_password_hash
#     admin = Admin(

#         name = "imoocmovie1",
#         pwd = generate_password_hash("imoocmovie1"),
#         is_super = 0,
#         role_id = 1
#     )
#     db.session.add(admin)
#     db.session.commit()