from models.user import User

def create_user(email, password, f_name, l_name):
    # 1) Check if email exists in the DB
    # 2) Hash the password
    # 3) Create the User object
    new_user = User(email, password, f_name, l_name)
    # 4) Save to the database
    return new_user.save()

def delete_user(id):
    # Grab user from DB
    # Delete the user
    pass

def update_user(id, data):
    # Grab the user from DB
    # Update the user's fields with data
    # Commit the changes to the DB
    pass

def get_user(id):
    # Grab user from the DB
    # Return that user to the controller
    pass
