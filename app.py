from flask import Flask

from models import db
from services import bcrypt
from controllers import jwt, auth_blueprint, blog_blueprint

app = Flask(__name__)

# Setting our configuration file
app.config.from_object("config.Development")

# TODO: Connect our flask app to postgres
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Add blueprints here
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(blog_blueprint, url_prefix="/blog")

if __name__ == "__main__":
    app.run()