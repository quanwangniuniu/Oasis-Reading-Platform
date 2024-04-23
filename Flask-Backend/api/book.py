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

app = current_app

PAGESIZE = 12

# 获取全部图书
class GetAllBooks(Resource):
    def get(self):
        sql = 'select * from book;'
        return executeSQL(sql)


#　分页获取书籍
class GetBookByPage(Resource):
    def get(self, page):
        offset = (page - 1) * PAGESIZE
        # 执行分页查询语句
        sql = f"SELECT * FROM `book` LIMIT %s OFFSET %s"
        return executeSQL(sql, [PAGESIZE, offset])

# 获取总页数
class GetTotalPage(Resource):
    def get(self):
        sql = "SELECT COUNT(*) FROM `book`"
        total = executeSQL(sql, None)
        return math.ceil(total[0]['COUNT(*)'] / PAGESIZE)


# 根据书籍id获取书籍详细信息
class BookById(Resource):
    def get(self, id):
        sql = f"SELECT * FROM book WHERE id = %s"
        res = executeSQL(sql, id)[0]
        print(res)
        return res

    def delete(self, id):
        sql = "DELETE FROM book WHERE id = %s"
        executeSQL(sql, id)
        return 'test'


# 获取书籍title
class GetBookByTitle(Resource):
    @jwt_required()
    def get(self):
        title = request.args.get('title')
        sql = f"SELECT * FROM book WHERE title like '%{title}%'"
        return executeSQL(sql, None)


# 增加书籍封面
class AddBookCover(Resource):
    def post(self):
        # 接收前端发送的图片
        img = request.files.get('file')
        # 生成图片名
        millis = int(round(time.time() * 1000))
        ext = os.path.splitext(img.filename)[-1]
        filename = str(millis) + ext
        print(millis)
        # 获取保存路径
        save_path = os.path.join(app.config['COVER_UPLOAD_FOLDER'], filename)
        # 保存图片
        img.save(save_path)
        return {'url': app.config['BASEURL'] + '/covers/' + filename, 'id': millis}


# 获取书籍封面
class GetBookCover(Resource):
    def get(self, filename):
        return send_from_directory(app.config['COVER_UPLOAD_FOLDER'], filename)

# 获取书籍封面
class GetBookFile(Resource):
    def get(self, filename):
        return send_from_directory(app.config['BOOK_UPLOAD_FOLDER'], filename)


#　增加书籍
class AddBook(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('bookItem', type=str)
        args = parser.parse_args()
        bookItem = json.loads(args['bookItem'])
        keys = ['id', 'title', 'author', 'publisher', 'ISBN', 'description', 'publish_year', 'page', 'binding', 'price',
                'series', 'rate_avg', 'rate_total', 'rate_cnt', 'url']
        values = [bookItem.get(key, 0) for key in keys]
        print(values)
        sql = f"INSERT INTO `book` ({','.join(keys)}) VALUES ({','.join(['%s'] * len(values))})"
        executeSQL(sql, values)
        return {'msg': 'success', 'data': '', 'code': 200}


#　更新书籍
class UpdateBook(Resource):
    def post(selfs):
        parser = reqparse.RequestParser()
        parser.add_argument('bookItem', type=str)
        args = parser.parse_args()
        bookItem = json.loads(args['bookItem'])
        print(bookItem)
        sql = """
            UPDATE book
            SET title=%s, author=%s, publisher=%s, ISBN=%s, description=%s, publish_year=%s, page=%s, binding=%s,
                price=%s, series=%s, rate_avg=%s, rate_total=%s, rate_cnt=%s, url=%s
            WHERE id=%s
        """
        executeSQL(sql, (
            bookItem['title'], bookItem['author'], bookItem['publisher'], bookItem['ISBN'], bookItem['description'],
            bookItem['publish_year'], bookItem['page'], bookItem['binding'], bookItem['price'], bookItem['series'], bookItem['rate_avg'],
            bookItem['rate_total'], bookItem['rate_cnt'],
            bookItem['url'], bookItem['id']
        ))

        return {'msg': 'success', 'data': '', 'code': 200}


api.add_resource(GetAllBooks, '/books')
api.add_resource(BookById, '/books/<string:id>')
api.add_resource(GetBookByTitle, '/getBookByTitle')
api.add_resource(AddBookCover, '/uploadCover')
api.add_resource(GetBookCover, '/covers/<string:filename>')
api.add_resource(GetBookFile, '/bookfile/<string:filename>')
api.add_resource(AddBook, '/addBook')
api.add_resource(UpdateBook, '/updateBook')
api.add_resource(GetBookByPage, '/books/page/<int:page>')
api.add_resource(GetTotalPage, '/books/pages')
