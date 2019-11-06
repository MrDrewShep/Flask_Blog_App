from flask import Blueprint, request

auth_blueprint = Blueprint('auth_api', __name__)

# login route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    # To log a user in and return an authentication token
    # Body: { username, password }
    # Return: { auth_token }
    body = request.json
    print(body['email'], body['password'])
    return {
        'auth_token': 'qwertyuio1234567890'
    }

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

    print(body['email'], body['password'], body['f_name'], body['l_name'])

    return {
        'message': 'User successfully created!'
    }
