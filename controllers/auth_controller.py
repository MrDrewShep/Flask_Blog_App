from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from services import bcrypt
from services.user_service import create_user
from models.user import User

auth_blueprint = Blueprint('auth_api', __name__)

# login route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    # To log a user in and return an authentication token
    # Body: { username, password }
    # Return: { auth_token }
    body = request.json
    to_check = User.query.filter_by(email=body["email"]).first()
    
    if bcrypt.check_password_hash(to_check.password, body["password"]):
        # Create JWT token and return it
        access_token = create_access_token(identity=to_check.id)
        message = {
            "message": "Hey, you logged in.",
            "token": access_token
        }
    else:
        message = {
            "message": "Incorrect password."
        }
    
    return message

# logout route
@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    # de-authenticate the token
    return 'logout route hit'

# register route
@auth_blueprint.route('/register', methods=['POST'])
def register():
    # Create a user
    # Body: { email, password, first_name, last_name }
    # Return: { message }

    body = request.json
    message = create_user(
        body['email'],
        bcrypt.generate_password_hash(body['password']).decode('utf-8'),
        body['f_name'],
        body['l_name'])

    return {
        "message": message
    }
