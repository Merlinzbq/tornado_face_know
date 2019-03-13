from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from utils.conn import Base


def create_db():
    # 映射模型对应的表
    Base.metadata.create_all()


def drop_db():
    # 删除模型映射的表
    Base.metadata.drop_all()


class User(Base):
    # 主键自增的int类型的id主键
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10), unique=True, nullable=False)
    realname = Column(String(10), unique=True, nullable=False)
    # img = Column(String(10), unique=True, nullable=False)
    create_time = Column(DateTime, default=datetime.now)

    __tablename__ = 'user'

    # def __repr__(self):



