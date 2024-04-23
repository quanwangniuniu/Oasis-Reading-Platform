import datetime
import time
import json

from flask import request, current_app, send_from_directory
from flask_restful import Resource, reqparse

from api.sql import executeSQL
from app import api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)

from api.snowflake import SnowflakeIDGenerator

app = current_app

PAGESIZE = 10


class AddFavourite(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('favouriteObj', type=str)
        args = parser.parse_args()
        favouriteObj = json.loads(args['favouriteObj'])

        favouriteObj['id'] = SnowflakeIDGenerator(1, 1).next_id()
        favouriteObj['user_id'] = int(get_jwt_identity())
        favouriteObj['created_time'] = int(round(time.time() * 1000))
        print(favouriteObj)

        if favouriteObj['type'] == 1:
            # 想读
            keys = ['id', 'user_id','book_id', 'created_time']
            values = [favouriteObj.get(key) for key in keys]
            sql = f"INSERT INTO `want` ({','.join(keys)}) VALUES ({','.join(['%s'] * len(values))})"
            executeSQL(sql, values)
            return {'msg': 'success', 'code': 200, 'data': ''}

        elif favouriteObj['type'] == 2:
            # 收藏
            keys = ['id', 'user_id', 'book_id', 'created_time', 'folder']
            values = [favouriteObj.get(key) for key in keys]
            sql = f"INSERT INTO `favourite` ({','.join(keys)}) VALUES ({','.join(['%s'] * len(values))})"
            executeSQL(sql, values)
            return {'msg': 'success', 'code': 200, 'data': ''}


class DeleteFavourite(Resource):
    @jwt_required()
    def delete(self, book_id, type):
        user_id = get_jwt_identity()
        table = 'want' if type == 1 else 'favourite'
        sql = f"delete from {table} where user_id = %s and book_id = %s"
        print(sql)
        executeSQL(sql, [user_id, book_id])
        return {'msg': 'success', 'code': 200, 'data': ''}


class GetAllFolder(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        sql = "select * from folder where user_id = %s"
        res = executeSQL(sql, [user_id])
        res = [{k: str(v) if isinstance(v, (int, float)) else v for k, v in d.items()} for d in res]
        print(res)
        return {'msg': 'success', 'code': 200, 'data': res}


class AddFolder(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        # 获取参数，收藏夹的名字
        parser.add_argument('folder_name', type=str)
        args = parser.parse_args()
        folder_name = args['folder_name']
        # 获取用户id
        user_id = get_jwt_identity()
        # 生成收藏夹的id
        folder_id = SnowflakeIDGenerator(1, 1).next_id()
        sql = "insert into folder values(%s, %s, %s)"
        executeSQL(sql, [folder_id, user_id, folder_name])
        return {'msg': 'success', 'code': 200, 'data': ''}


class GetFavouritesByFolder(Resource):
    @jwt_required()
    def get(get):
        # 获取用户id
        user_id = get_jwt_identity()
        # 先查询该用户所有收藏夹的id
        sql = "select id, folder_name from folder where user_id = %s"
        folders = executeSQL(sql, user_id)
        res = []
        for folder in folders:
            cur_sql = "SELECT book.* FROM favourite " \
                      "JOIN book ON favourite.book_id = book.id " \
                      "WHERE favourite.folder = %s " \
                      "order by favourite.created_time desc LIMIT 6 offset 0"
            books = executeSQL(cur_sql, folder['id'])
            folderObj = {'id': folder['id'], 'name': folder['folder_name'], 'books': books}
            res.append(folderObj)
        print(res)
        return {'msg': 'success', 'code': 200, 'data': res}


api.add_resource(AddFavourite, '/favourite/add')
api.add_resource(DeleteFavourite, '/favourite/delete/<int:book_id>/<int:type>')
api.add_resource(GetAllFolder, '/favourite/folder/')
api.add_resource(AddFolder, '/favourite/folder/add')
api.add_resource(GetFavouritesByFolder, '/favourite/abstract')
