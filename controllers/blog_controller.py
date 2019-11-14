from flask import Blueprint, request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.blog_service import create_blog, fetch_blog, edit_blog, delete_blog, fetch_one_blog

blog_blueprint = Blueprint("blog_api", __name__)

# Route to create a new post
@blog_blueprint.route("/new", methods=["POST"])
@jwt_required
def new_blog():
    user = get_jwt_identity()
    data = request.json
    return create_blog(data, user)

# /all
@blog_blueprint.route('/all', methods=["GET"])
@jwt_required
def all_blog():
    posts = fetch_blog()
    return custom_response(posts, 200)

# /<int:post_id>
@blog_blueprint.route("/<int:post_id>", methods=["GET", "PUT", "DELETE"])
@jwt_required
def single_blog(post_id):
    if request.method == "GET":
        blog = fetch_one_blog(post_id)
        if blog:
            return custom_response(blog, 200)
    elif request.method == "PUT":
        data = request.json
        user = get_jwt_identity()
        blog = fetch_one_blog(post_id)
        if str(user) == blog["user_id"]:
            return custom_response(edit_blog(post_id, data), 200)
    elif request.method == "DELETE":
        user = get_jwt_identity()
        blog = fetch_one_blog(post_id)
        if str(user) == blog["user_id"]:
            return custom_response(delete_blog(blog["id"]), 204)
    else:
        return "Method not allowed", 405

def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )