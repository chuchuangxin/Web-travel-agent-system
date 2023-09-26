# 用于储存配置信息
# 数据库配置
# Used to store configuration information
# Database configuration

import os
basedi = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    JSON_AS_ASCII = False
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    SECRET_KEY = "chuchuchu"
    SECRET_KEY = os.environ.get('SECRET_KEY')or'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedi,"chuchuchu.db")
    SQLALCHEMY_TRACK_MODIFICATION=False




