import sqlite3

from flask import Flask, session, url_for, redirect, request, render_template,  make_response, current_app,flash ,g


import random
import os
import hashlib
import json

from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash

from models import User, Question, Answer, Admin, Places, Hotel, HotelBook, PlaceBook, Message, Reply, Apex
from exts import db
import config
from config import Config
import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)


app.config.from_object(config)
db.init_app(app)


#db= SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/search_place/')
def search_place():
    q = request.args.get('q')
    places = Places.query.filter(or_(Places.name.contains(q),Places.content.contains(q)))
    context = {
        'places': places
    }
    return render_template('places.html',**context)

@app.route('/search_hotel/')
def search_hotel():
    q = request.args.get('q')
    hotels = Hotel.query.filter(or_(Hotel.name.contains(q),Hotel.content.contains(q)))
    context = {
        'hotels': hotels
    }
    return render_template('hotel.html',**context)

@app.route('/search/')
def search():
    q = request.args.get('q')
    questions = Question.query.filter(or_(Question.title.contains(q),Question.content.contains(q)))
    context = {
        'questions': questions
    }
    return render_template('indexz.html',**context)

#注册！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！


# @app.route('/regist', methods=['GET', 'POST'])
# ef regist():
#    # Accept the front-end information
#    if request.method == 'POST':
#        NAME = request.form['name']
#        EMAIL = request.form['email']
#        PASSWORD = request.form['password']
#        # Registration conditions are not established
#        if NAME == '' or EMAIL == '' or PASSWORD == '':
            #
#           flash('Content cannot be empty',"warning")
#           return render_template('login&signup.html')
  #       elif user_check.user_exist_email(EMAIL) or user_check.user_check(NAME):
#            flash('The user account has been used, please re register',"danger")
#
#            return render_template('login&signup.html')
#        # Register successfully
  #       elif len(PASSWORD)< 8:
#           flash('Password must be more than eight digits',"danger")

#          return render_template('login&signup.html')
        # Register successfully
#      else:
#          password = hashlib.sha256(PASSWORD.encode('utf-8')).hexdigest()
#           user_regist.post_register(EMAIL, NAME, password)
#           current_app.logger.info("email: " + EMAIL + " Regist")
#          flash('Register was successful!!',"success")


#            return redirect(url_for(endpoint='check'))



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login&signup.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone).first()
        if user and check_password_hash(user.password,password):
            # 如果用户存在，就设置cookie
            session['user_id'] = user.id
            # 如果想在31天都不需要登录，就写上下面这句话
            session.permanent = True
            # 以上设置完成后就认为登陆成功，跳转到index页面
            return redirect(url_for('index'))
        else:
            return u'手机号码或者密码输入错误，请确认后再登录！'






@app.route('/ADMINlogin/', methods=['GET', 'POST'])
def ADMINlogin():
    if request.method == 'GET':
        return render_template('login_admin.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        admin = Admin.query.filter(Admin.telephone == telephone, Admin.password == password).first()
        if admin:
            # 如果用户存在，就设置cookie
            session['admin_id'] = admin.id
            # 如果想在31天都不需要登录，就写上下面这句话
            #session.permanent = True
            # 以上设置完成后就认为登陆成功，跳转到index页面
            return redirect(url_for('indexadmin'))
        else:
            return u'手机号码或者密码输入错误，请确认后再登录！'






@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('login&signup.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password_hash = generate_password_hash(password1)

        # 创建用户
        user = User(telephone=telephone, username=username, password=password_hash)
        # 提交数据库
        db.session.add(user)
        db.session.commit()
        # 注册成功就跳转到登录页面
        return redirect(url_for('login'))

@app.route('/ADMINregist/', methods=['GET', 'POST'])
def ADMINregist():
    if request.method == 'GET':
        return render_template('login_admin.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')


        # 创建用户
        admin = Admin(telephone=telephone, username=username, password=password1)
        # 提交数据库
        db.session.add(admin)
        db.session.commit()
        # 注册成功就跳转到登录页面
        return redirect(url_for('ADMINlogin'))






@app.route('/')
def first():
  return render_template('first.html')

@app.route('/admin')
def admin():
  return render_template('admin.html')

#改动！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

@app.route('/contact')
def contact():
    context = {
        'admins': Admin.query.order_by('id').all(),
        'apexs': Apex.query.order_by('id').all()
    }
    return render_template("contact.html", **context)

@app.route('/deta/<admin_id>/', methods=['GET', 'POST'])
def deta(admin_id):
    admin_model = Admin.query.filter(Admin.id == admin_id).first()
    return render_template('deta.html', admin=admin_model)



@app.route('/question/', methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('indexz'))


@app.route('/reply/<message_id>/', methods=['GET', 'POST'])
def reply(message_id):
    message_model = Message.query.filter(Message.id == message_id).first()
    return render_template('reply.html', message=message_model)

@app.route('/places/', methods=['GET', 'POST'])
def places():
        name = request.form.get('name')
        content = request.form.get('content')
        path = request.form.get('path')
        price = request.form.get('price')
        places = Places(name=name,content=content,path=path,price=price)
        db.session.add(places)
        db.session.commit()
        return redirect(url_for('type'))

@app.route('/hotels/', methods=['GET', 'POST'])
def hotels():
        name = request.form.get('name')
        content = request.form.get('content')
        path = request.form.get('path')
        price = request.form.get('price')
        hotels = Hotel(name=name,content=content,path=path,price=price)
        db.session.add(hotels)
        db.session.commit()
        return redirect(url_for('inbound'))

@app.route('/add_apex/', methods=['GET', 'POST'])
def add_apex():
    content = request.form.get('content')
    path = request.form.get('path')
    post = request.form.get('post')
    reply = Apex(content=content, path=path, post=post)
    admin_id = session.get('admin_id')
    admin = Admin.query.filter(Admin.id == admin_id).first()
    reply.author = admin

    db.session.add(reply)
    db.session.commit()
    return redirect(url_for('apex'))



@app.route('/add_answer/', methods=['POST'])
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    answer = Answer(content=content)
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    answer.author = user

    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))

@app.route('/add_reply/', methods=['POST'])
def add_reply():
    content = request.form.get('content')
    message_id = request.form.get('message_id')

    reply = Reply(content=content)
    admin_id = session.get('admin_id')
    admin = Admin.query.filter(Admin.id == admin_id).first()
    reply.author = admin

    message = Message.query.filter(Message.id == message_id).first()
    reply.message = message
    db.session.add(reply)
    db.session.commit()
    return redirect(url_for('message', message_id=message_id))

@app.route('/add_message/', methods=['POST'])
def add_message():
    content = request.form.get('answer_content')
    admin_id = request.form.get('admin_id')

    message = Message(content=content)
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    message.author = user

    admin = Admin.query.filter(Admin.id == admin_id).first()
    message.admin = admin
    db.session.add(message)
    db.session.commit()
    return redirect(url_for('deta', admin_id=admin_id))




@app.route('/add_book/', methods=['POST'])
def add_book():
    name = request.form.get('name')
    hotel_id = request.form.get('hotel_id')

    num = request.form.get('num')
    Fr = request.form.get('Fr')
    To = request.form.get('To')

    hotelbook = HotelBook(name=name,num=num,Fr=Fr,To=To)

    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    hotelbook.author = user


    hotel = Hotel.query.filter(Hotel.id == hotel_id).first()
    hotelbook.hotel = hotel
    db.session.add(hotelbook)
    db.session.commit()
    flash('Booking successfully')

    return redirect(url_for('hotel', hotel_id=hotel_id))



@app.route('/add_bookP/', methods=['POST'])
def add_bookP():
    name = request.form.get('name')
    place_id = request.form.get('place_id')

    num = request.form.get('num')
    Fr = request.form.get('Fr')
    To = request.form.get('To')
    Date = request.form.get('Date')

    placebook = PlaceBook(name=name,num=num,Fr=Fr,To=To, Date=Date)

    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    placebook.author = user


    place = Places.query.filter(Places.id == place_id).first()
    placebook.place = place
    db.session.add(placebook)
    db.session.commit()
    flash('Booking successfully')

    return redirect(url_for('place', place_id=place_id))





@app.route('/check')
def check():
    # Random visitor id
    visitor = random.randint(500, 999)
    return render_template('login&signup.html', visitor=visitor)



@app.route('/index')
def index():
    context = {
        'places': Places.query.order_by('id').all(),
        'hotels': Hotel.query.order_by('id').all()
    }
    return render_template("index.html",**context)

@app.route('/place_single/<place_id>/', methods=['GET', 'POST'])
def place_single(place_id):
    place_model = Places.query.filter(Places.id == place_id).first()
    return render_template('place-single.html', place=place_model)

@app.route('/hotel_single/<hotel_id>/', methods=['GET', 'POST'])
def hotel_single(hotel_id):
    hotel_model = Hotel.query.filter(Hotel.id == hotel_id).first()
    return render_template('hotel-single.html', hotel=hotel_model)

@app.route('/detail/<question_id>/', methods=['GET', 'POST'])
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)

@app.route('/hotelbook/', methods=['GET', 'POST'])
def hotelbook():
    context = {
        'hotelbooks': HotelBook.query.order_by('id').all()
    }
    return render_template("hotelbook.html",**context)


@app.route('/indexadmin')
def indexadmin():
    return render_template("indexadmin.html")



@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/place')
def place():
    context = {
        'places': Places.query.order_by('id').all(),

        'placebooks': PlaceBook.query.order_by('id').all()

    }

    return render_template('places.html', **context)


@app.route('/indexz')
def indexz():
    context = {
        'questions': Question.query.order_by('create_time').all()
    }
    return render_template('indexz.html', **context)


@app.route('/Mu')
def Mu():
    return render_template('MU.html')

@app.route('/idle')
def idle():
    return render_template('idle.html')
@app.route('/sound')
def sound():
    return render_template('sound.html')
@app.route('/ipad')
def ipad():
    return render_template('ipad.html')
@app.route('/hotel')
def hotel():
    context = {
        'hotels': Hotel.query.order_by('id').all(),
        'hotelbooks': HotelBook.query.order_by('id').all()
    }
    return render_template('hotel.html', **context)

@app.route('/blog')
def blog():
  return render_template('blog.html')







#admin interface
@app.route('/inbound')
def inbound():
    context = {
        'hotels': Hotel.query.order_by('id').all()
    }
    return render_template("inbound.html", **context)



#员工端blog！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
@app.route('/blog_delete/<int:id>',methods=['POST'])
def blog_delete(id):
    quest = Question.query.get_or_404(id)
    db.session.delete(quest)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('inventory'))

@app.route('/apex_delete/<int:id>',methods=['POST'])
def apex_delete(id):
    quest = Apex.query.get_or_404(id)
    db.session.delete(quest)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('apex'))


@app.route('/reply_delete/<int:id>',methods=['POST'])
def reply_delete(id):
    quest = Reply.query.get_or_404(id)
    db.session.delete(quest)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('re'))


@app.route('/mess_delete/<int:id>',methods=['POST'])
def mess_delete(id):
    quest = Message.query.get_or_404(id)
    db.session.delete(quest)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('message'))




@app.route('/place_delete/<int:id>',methods=['POST'])
def place_delete(id):
    place = Places.query.get_or_404(id)
    db.session.delete(place)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('type'))


@app.route('/hotel_delete/<int:id>',methods=['POST'])
def hotel_delete(id):
    hotel = Hotel.query.get_or_404(id)
    db.session.delete(hotel)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('inbound'))


@app.route('/hotelbook_delete/<int:id>',methods=['POST'])
def hotelbook_delete(id):
    hotelbook = HotelBook.query.get_or_404(id)
    db.session.delete(hotelbook)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('hotelbook'))


@app.route('/placebook_delete/<int:id>',methods=['POST'])
def placebook_delete(id):
    placebook = PlaceBook.query.get_or_404(id)
    db.session.delete(placebook)
    db.session.commit()
    flash('Delete successfully')
    return redirect(url_for('placebook'))


@app.route('/inventory')
def inventory():
    context = {
        'questions': Question.query.order_by('create_time').all()
    }
    return render_template("inventory.html", **context)

@app.route('/message')
def message():
    context = {
        'messages': Message.query.order_by('create_time').all()
    }
    return render_template("message.html", **context)


@app.route('/re')
def re():
    context = {
        'replys': Reply.query.order_by('create_time').all()
    }
    return render_template("re.html", **context)


@app.route('/outBoud')
def outBoud():
    return render_template("outBoud.html")
@app.route('/type')
def type():
    context = {
        'places': Places.query.order_by('id').all()
    }
    return render_template("type.html",**context)

@app.route('/apex')
def apex():
    context = {
        'apexs': Apex.query.order_by('id').all()
    }
    return render_template("apex.html",**context)

@app.route('/placebook')
def placebook():
    context = {
        'placebooks': PlaceBook.query.order_by('id').all()
    }
    return render_template("placebook.html",**context)


@app.route('/updatePwd')
def updatePwd():
    return render_template("updatePwd.html")
@app.route('/user')
def user():
    return render_template("user.html")
@app.route('/warning')
def warning():
    return render_template("warning.html")





@app.route('/blog-single')
def blog_single():
    return render_template("blog-single.html")


@app.route('/map')
def map():
    return render_template("map.html")


if __name__ == '__main__':
    app.debug = True
    app.run()

















from exts import db
from datetime import datetime

# class Question(db.Model):
#    __tablename__ = 'question'
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    title = db.Column(db.String(100), nullable=False)
#    content = db.Column(db.Text, nullable=False)
#    # 注意不要写成now()
#    create_time = db.Column(db.DateTime, default=datetime.now)
#    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#    author = db.relationship('User', backref=db.backref('question'))

with app.app_context():
    db.create_all()


