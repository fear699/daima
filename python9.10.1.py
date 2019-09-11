#!usr/bin/env python
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base

# 建立连接与数据库的连接
engine = create_engine('mysql+pymysql://zhang:123@localhost:3306/python1905')

Base = declarative_base(bind=engine)  # 创建模型的基础类
Session = sessionmaker(bind=engine)   # 创建会话类


class User(Base):
    '''类本身对应数据库里的表结构'''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True)
    birthday = Column(Date, default=datetime.date(1990, 1, 1))
    city = Column(String(10), default='上海')


Base.metadata.create_all(checkfirst=True)# 创建表结构
session = Session()

#print(1)

# 定义的每一个对象，对应数据库里的一行数据
bob = User(name='bob', birthday=datetime.date(1990, 3, 21), city='上海')
tom = User(name='tom', birthday=datetime.date(1995, 9, 12))
lucy = User(name='lucy', birthday=datetime.date(1998, 5, 14), city='北京')
jam = User(name='jam', birthday=datetime.date(1994, 3, 9), city='深圳')
alex = User(name='alex', birthday=datetime.date(1992, 3, 17), city='北京')
eva = User(name='eva', birthday=datetime.date(1987, 7, 28), city='深圳')
rob = User(name='rob', birthday=datetime.date(1974, 2, 5), city='上海')
ella = User(name='ella', birthday=datetime.date(1999, 5, 26), city='北京')
#print(2)
#u_query = session.query(User)
#u = u_query.filter_by(id=4).one()
# 定义与数据库的会话

session.add_all([jam])
session.commit()

#session.delete(u)
#session.commit()
#u.city='武汉'

#session.commit()
