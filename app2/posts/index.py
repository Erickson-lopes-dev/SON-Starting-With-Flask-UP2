from flask import Blueprint, render_template, request, url_for, redirect

from app2.config import db
from app2.models.post import Post

posts = Blueprint('posts', __name__)


@posts.route('/new', methods=['GET'])
def new():
    return render_template('posts/new.html')


@posts.route('/new', methods=['POST'])
def create():
    post = Post(request.form['title'], request.form['body'])

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('posts.new'))
