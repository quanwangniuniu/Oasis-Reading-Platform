import datetime
import time
import json

from flask import request, current_app, send_from_directory
from flask_restful import Resource, reqparse

from api.sql import executeSQL
from app import api
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)

from api.snowflake import SnowflakeIDGenerator

app = current_app


# 　检查用户是否已经想读、收藏、评论
class OperationCheck(Resource):
    @jwt_required()
    def get(self):
        # 获取书籍id和用户id
        book_id = request.args.get('book_id')
        user_id = get_jwt_identity()
        # 查询是否已经想读
        sql = "select count(*) from comment where user_id = %s and book_id = %s"
        isCommented = executeSQL(sql, [user_id, book_id])[0]['count(*)']

        # 查询是否已经收藏
        sql = "select count(*) from want where user_id = %s and book_id = %s "
        isWanted = executeSQL(sql, [user_id, book_id])[0]['count(*)']

        # 查询是否已经评论
        sql = "select count(*) from favourite where user_id = %s and book_id = %s"
        isFavourited = executeSQL(sql, [user_id, book_id])[0]['count(*)']

        # 封装查询结果
        res = {
            'isCommented': True if isCommented > 0 else False,
            'isWanted': True if isWanted > 0 else False,
            'isFavourited': True if isFavourited > 0 else False
        }
        print(res)

        return {'msg': 'success', 'code': 200, 'data': res}

api.add_resource(OperationCheck, '/operation/check')
