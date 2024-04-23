import os
import time
import json
import math

from flask import request, current_app, send_from_directory
from flask_restful import Resource, reqparse

from api.sql import executeSQL
from app import api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)

from api.snowflake import SnowflakeIDGenerator

app = current_app


def checkNewPhone(phone):
    sql = "select count(*) from user where phone = %s"
    count = executeSQL(sql, phone)[0]['count(*)']
    return count == 0

def getPhoneByUserId(id):
    sql = "select phone from user where id = %s"
    phone = executeSQL(sql, id)[0]['phone']
    return phone


class AddUser(Resource):
    def post(self):
        # 接收前端传递的参数
        parser = reqparse.RequestParser()
        parser.add_argument('user', type=str)
        args = parser.parse_args()
        user = json.loads(args['user'])

        # 取出手机号
        phone = user['phone']
        # 查询手机号是否已经被注册了
        if not checkNewPhone(phone):
            return {'msg': '该手机号已被注册', 'data': '', 'code': 300}

        # 设置id和默认头像
        user['id'] = SnowflakeIDGenerator(1, 1).next_id()
        user['avatar'] = app.config['BASEURL'] + '/avatars/default.jpg'
        user['type'] = 1
        user['create_day'] = int(round(time.time() * 1000))
        # 生成sql语句
        keys = ['id', 'username', 'password', 'phone', 'type', 'avatar', 'create_day']
        values = [user.get(key) for key in keys]
        sql = f"INSERT INTO `user` ({','.join(keys)}) VALUES ({','.join(['%s'] * len(values))})"
        # 执行sql语句
        executeSQL(sql, values)
        # 为用户生成一个默认收藏夹
        user_id = user['id']
        folder_id = SnowflakeIDGenerator(1, 1).next_id()
        folder_name = '默认收藏夹'
        sql = "insert into folder values(%s, %s, %s)"

        print(app.config['BASEURL'] + '/avatars/default.jpg')
        executeSQL(sql, [folder_id, user_id, folder_name])

        return {'msg': 'success', 'data': '', 'code': 200}


class UserLogin(Resource):
    def post(self):
        # 接收参数, 用户名和密码
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        phone, password = args['phone'], args['password']
        # 先判断手机号是否已经注册
        if checkNewPhone(phone):
            return {'msg': '手机号未注册,先去注册吧！', 'data': '', 'code': 300}

        # 根据用户名从数据库查密码
        sql = "select id, password, type from `user` where phone = %s"
        result = executeSQL(sql, phone)[0]
        id, expected_password, type = result['id'], result['password'], result['type']

        # 验证密码
        if password == expected_password:
            access_token = create_access_token(identity=id)
            if type == 1:
                return {'msg': '登录成功', 'data': {'token': access_token, 'type': 1}, 'code': 200}
            else:
                return {'msg': '登录成功', 'data': {'token': access_token, 'type': 2}, 'code': 200}
        else:
            return {'msg': '密码错误', 'data': '', 'code': 400}

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print(current_user)
        return {'data': {'status': 1}, 'code': 0}


class GetUserAvatarURL(Resource):
    @jwt_required()
    def get(self):
        # 从token中获取用户id
        current_user_id = get_jwt_identity()
        # 根据id查询头像url
        sql = "select avatar from `user` where id = %s"
        path = executeSQL(sql, current_user_id)[0]['avatar']
        return {'data': path}


class GetUserInfo(Resource):
    @jwt_required()
    def get(self):
        # 从token中获取用户id
        id = get_jwt_identity()
        sql = "select id, username, phone, email, create_day, signature, gender, birthday, avatar from `user` where id = %s"
        res = executeSQL(sql, id)[0]
        res['create_day'] = res['create_day']
        res['birthday'] = res['birthday']
        return {'msg': 'success', 'code': 200, 'data': res}


class GetUserAvatar(Resource):
    def get(self, filename):
        return send_from_directory(app.config['AVATAR_UPLOAD_FOLDER'], filename)


class AddUserAvatar(Resource):
    @jwt_required()
    def post(self):
        # 接收前端发送的图片
        img = request.files.get('file')
        # 从token中获取用户id
        id = get_jwt_identity()
        ext = os.path.splitext(img.filename)[-1]
        millis = str(int(round(time.time() * 1000)))
        filename = millis + ext
        # 获取保存路径
        save_path = os.path.join(app.config['AVATAR_UPLOAD_FOLDER'], filename)
        # 保存图片
        img.save(save_path)
        print(save_path)
        print(app.config['BASEURL']+'/avatars/' + filename)
        return {'url': app.config['BASEURL']+'/avatars/' + filename}


class UpdateUser(Resource):
    @jwt_required()
    def post(self):
        id = get_jwt_identity()
        # 接收前端传递的参数
        parser = reqparse.RequestParser()
        parser.add_argument('user', type=str)
        args = parser.parse_args()
        user = json.loads(args['user'])
        print(user)
        # 取出手机号和id
        phone = user['phone']
        id = get_jwt_identity()
        # 先看手机号是否被修改了
        if getPhoneByUserId(id) != phone and not checkNewPhone(phone):
            return {'msg': '手机号已注册！', 'data': '', 'code': 300}


        sql = "UPDATE `user` SET "
        for key, value in user.items():
            if key != "id" and key != "code":
                sql += f"`{key}`='{value}',"
        sql = sql[:-1] + f" WHERE `id`={id};"
        executeSQL(sql, None)
        return {'msg': 'success', 'code': 200, 'data': ''}


api.add_resource(UserLogin, '/login')
api.add_resource(AddUser, '/user/add')
api.add_resource(UpdateUser, '/user/update')
api.add_resource(GetUserAvatar, '/avatars/<string:filename>')
api.add_resource(GetUserAvatarURL, '/avatar')
api.add_resource(GetUserInfo, '/user')
api.add_resource(AddUserAvatar, '/upload/avatar')
