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

# 新增评论
class AddComment(Resource):
    @jwt_required()
    def post(self):
        # 提取评论参数
        parser = reqparse.RequestParser()
        parser.add_argument('rateObj', type=str)
        args = parser.parse_args()
        rateObj = json.loads(args['rateObj'])
        #　设置默认值
        rateObj['id'] = SnowflakeIDGenerator(1, 1).next_id()
        rateObj['book_id'] = int(rateObj['book_id'])
        rateObj['rate'] = rateObj['rate'] * 2
        rateObj['user_id'] = int(get_jwt_identity())
        rateObj['created_time'] = int(round(time.time() * 1000))
        # 将评价对象插入数据库
        keys = ['id', 'user_id', 'book_id', 'rate', 'comment', 'created_time']
        values = [rateObj.get(key) for key in keys]
        sql = f"INSERT INTO `comment` ({','.join(keys)}) VALUES ({','.join(['%s'] * len(values))})"
        executeSQL(sql, values)
        return {'msg': 'success', 'code': 200, 'data': ''}


class DeleteComment(Resource):
    @jwt_required()
    def delete(self, book_id):
        # 获取用户id
        user_id = get_jwt_identity()
        sql = "delete from `comment` where user_id = %s and book_id = %s"
        executeSQL(sql, [user_id, book_id])
        return {'msg': 'success', 'code': 200, 'data': ''}


class IsRated(Resource):
    @jwt_required()
    def get(self):
        # 获取书籍id和用户id
        book_id = request.args.get('book_id')
        user_id = get_jwt_identity()
        # 执行sql
        sql = "select count(*) from comment where user_id = %s and book_id = %s"
        res = executeSQL(sql, [user_id, book_id])[0]['count(*)']
        print(res)
        return {'msg': 'success', 'code': 200, 'data': True if res > 0 else False}


# 根据id获取所有评论
class GetAllCommentById(Resource):
    def get(self, id):
        sql = "select * from comment where book_id = %s"
        res = executeSQL(sql, id)
        return {'msg': 'success', 'code': 200, 'data': res}


# 获取指定书籍的所有评论
class GetAllCommentByIdAndPage(Resource):
    def get(self, id, page):
        offset = (page - 1) * PAGESIZE
        sql = "SELECT comment.id, comment.user_id, comment.book_id, comment.rate, comment.comment, comment.created_time, user.username, user.avatar " \
              "FROM comment " \
              "INNER JOIN user ON comment.user_id = user.id " \
              "WHERE comment.book_id = %s " \
              "order by comment.created_time desc " \
              "LIMIT %s OFFSET %s"
        res = executeSQL(sql, [id, PAGESIZE, offset])
        return {'msg': 'success', 'code': 200, 'data': res}


# 获取指定用户的评论
class GetCommentByUserIdAndPage(Resource):
    @jwt_required()
    def get(self, page):
        user_id = get_jwt_identity()
        pagesize = 3
        offset = (page - 1) * pagesize
        sql = "SELECT comment.id, comment.book_id, comment.rate, comment.created_time, comment.comment, book.title, book.url " \
              "FROM comment, book, user " \
              "where user.id = comment.user_id and comment.book_id = book.id and user.id = %s " \
              "order by comment.created_time desc " \
              "LIMIT %s OFFSET %s"
        res = executeSQL(sql, [user_id, pagesize, offset])
        return {'msg': 'success', 'code': 200, 'data': res}


api.add_resource(AddComment, '/comment/add')
api.add_resource(DeleteComment, '/comment/delete/<int:book_id>')
api.add_resource(IsRated, '/comment/check')
api.add_resource(GetAllCommentById, '/comment/<string:id>')
api.add_resource(GetAllCommentByIdAndPage, '/comment/<int:id>/<int:page>')
api.add_resource(GetCommentByUserIdAndPage, '/comment/user/<int:page>')
