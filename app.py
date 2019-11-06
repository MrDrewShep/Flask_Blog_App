from flask import Flask

from controllers import auth_blueprint

app = Flask(__name__)

# TODO: Connect our flask app to postgres

# Add blueprints here
app.register_blueprint(auth_blueprint, url_prefix="/auth")

# Any other routes here
@app.route('/')
def hello():
    return 'HELLO TEST'

if __name__ == "__main__":
    app.run()