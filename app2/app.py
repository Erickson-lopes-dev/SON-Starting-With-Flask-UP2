import os
from app2.config import app
from app2.posts.index import posts

app.register_blueprint(posts)
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
