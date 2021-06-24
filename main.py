import math
from datetime import datetime
import json
from flask_mail import Mail
from flask import Flask, render_template, session, redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

local_server = True
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = params["upload_location"]
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params["gmail_user"],
    MAIL_PASSWORD=params["gmail_password"]
)

mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)


class Contact(db.Model):
    Sr_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=True)


class Posts(db.Model):
    Sr_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    subtitle = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)
    imageurl = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=True)


@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]

    if (page == 1):
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif (page == last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', param=params, posts=posts, prev=prev, next=next)


@app.route('/about')
def about():
    return render_template('about.html', param=params)


@app.route('/edit/<string:Sr_no>', methods=["GET", "POST"])
def edit(Sr_no):
    if ('user' in session and session['user'] == params['admin_email']):
        if request.method == "POST":
            title = request.form.get('title')
            subtitle = request.form.get('subtitle')
            slug = request.form.get('slug')
            content = request.form.get('content')
            imageurl = request.form.get('imageurl')
            date = datetime.now()

            if Sr_no == '0':
                post = Posts(title=title, subtitle=subtitle, slug=slug, content=content, imageurl=imageurl, date=date)
                db.session.add(post);
                db.session.commit()
            else:
                post = Posts.query.filter_by(Sr_no=Sr_no).first()
                post.title = title;
                post.subtitle = subtitle;
                post.slug = slug;
                post.content = content;
                post.imageurl = imageurl;
                post.date = date
                db.session.commit()
                return redirect('/edit/' + Sr_no)
        post = Posts.query.filter_by(Sr_no=Sr_no).first()
        return render_template('edit.html', param=params, post=post)


@app.route('/delete/<string:Sr_no>', methods=["GET", "POST"])
def delete(Sr_no):

    #Checking if the user is admin or not
    #Only admin can have access to the dashboard

    if ('user' in session and session['user'] == params['admin_email']):
        post = Posts.query.filter_by(Sr_no=Sr_no).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/dashboard")


@app.route('/uploader', methods=["GET", "POST"])
def uploader():
    if ('user' in session and session['user'] == params['admin_email']):
        if request.method == "POST":
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded Successfully"


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if ('user' in session and session['user'] == params['admin_email']):
        posts = Posts.query.filter_by().all()
        return render_template('dashboard.html', param=params, posts=posts)

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        if (email == params['admin_email'] and password == params['admin_password']):
            session['user'] = email
            posts = Posts.query.filter_by().all()
            return render_template('dashboard.html', param=params, posts=posts)

    else:
        return render_template('login.html', param=params)


@app.route('/post/<string:post_slug>', methods=["GET"])
def post(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', param=params, post=post)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contact(name=name, email=email, phone_number=phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender='email',
                          recipients=[params["gmail_user"]],
                          body=message + "\n" + phone
                          )

    return render_template('contact.html', param=params)


app.run()
