from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 注意不要写成now()
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('question'))


class Places(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    path = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)


class Hotel(db.Model):
    __tablename__ = 'hotel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    path = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)






class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    question = db.relationship('Question', backref=db.backref('answers', order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('answers'))



class HotelBook(db.Model):
    __tablename__ = 'hotelbook'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    num = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    Fr = db.Column(db.Text, nullable=False)
    To = db.Column(db.Text, nullable=False)

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hotel = db.relationship('Hotel', backref=db.backref('hotelbooks', order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('hotelbooks'))


class PlaceBook(db.Model):
    __tablename__ = 'placebook'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    num = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    Fr = db.Column(db.Text, nullable=False)
    To = db.Column(db.Text, nullable=False)


    Date = db.Column(db.String(50), nullable=False)

    place_id = db.Column(db.Integer, db.ForeignKey('places.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    place = db.relationship('Places', backref=db.backref('placebooks', order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('placebooks'))




class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    admin = db.relationship('Admin', backref=db.backref('messages', order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('messages'))



class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('admin.id'))

    message = db.relationship('Message', backref=db.backref('replys', order_by=id.desc()))
    author = db.relationship('Admin', backref=db.backref('replys'))


class Apex(db.Model):
    __tablename__ = 'apex'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    path = db.Column(db.Text, nullable=False)
    post = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    author_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    author = db.relationship('Admin', backref=db.backref('apexs'))
