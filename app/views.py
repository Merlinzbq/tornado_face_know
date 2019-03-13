
import tornado.web

from app.models import create_db, User
from utils.conn import session
from utils.faceid import face_register, face_valid


class InitDbHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        create_db()
        self.write('同步数据成功')


class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        self.render('login_new.html')

    def post(self, *args, **kwargs):
        face = self.get_argument('face')
        img = face.split(',')[-1]
        if face_valid(img):
            self.render('index.html')
            return
        self.write('登录失败')


class RegisterHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('register_new.html')

    def post(self, *args, **kwargs):
        # 获取账号
        username = self.get_argument('username')
        realname = self.get_argument('realname')
        face = self.get_argument('face')
        # img = base64.b64decode(face.split(',')[-1])
        img = face.split(',')[-1]
        # 注册基本信息
        user = User()
        user.username = username
        user.realname = realname
        session.add(user)
        session.commit()
        # 人脸注册
        res = face_register(img, user.id)
        if res:
            self.redirect('/login/')
            return

        # 如果注册不成功，则删除用户信息
        session.delete(user)
        session.commit()
        self.write('注册失败')






