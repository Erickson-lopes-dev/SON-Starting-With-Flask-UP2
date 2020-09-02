from flask import Blueprint
from app2.models.post import Post

posts = Blueprint('posts', __name__)


@posts.route('/', methods=['GET'])
def main():
    return 'posts routes'
