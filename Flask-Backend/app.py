from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['COVER_UPLOAD_FOLDER'] = "./images/covers"
app.config['AVATAR_UPLOAD_FOLDER'] = "./images/avatars"
app.config['BOOK_UPLOAD_FOLDER'] = "./books"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)
app.config['BASEURL'] = 'http://127.0.0.1:5000'

# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
CORS(app, resources=r'/*', supports_credentials=True)

jwt = JWTManager(app)
api = Api(app)

from api import book, user, comment, favourite, common

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)