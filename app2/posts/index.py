from flask import Blueprint

posts = Blueprint('posts', __name__)


@posts.route('/', methods=['GET'])
def main():
    return 'posts routes'
