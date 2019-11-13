from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

blog_blueprint = Blueprint("blog_api", __name__)

# Route to create a new post
@blog_blueprint.route("/new", methods=["POST"])
@jwt_required
def new_blog():
    user = get_jwt_identity()
    return {
        "who_you_are": user,
        "message": "Blog post created"
    }