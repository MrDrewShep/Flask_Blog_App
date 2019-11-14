from models.blog import Blog, BlogSchema
from datetime import datetime

blog_schema = BlogSchema()

def create_blog(data, user):
    new_post = Blog(
        title=data["title"],
        content=data["content"],
        user_id=user,
    )
    try:
        new_post.save()
        message = "Blog post saved successfully"
        return message, 200
    except Exception as e:
        return str(e), 400

def fetch_blog():
    x = Blog.get_all_blogs()
    blog_posts = blog_schema.dump(x, many=True)
    return blog_posts

def edit_blog(post_id, data):
    x = Blog.get_one_blog(post_id)
    updated = x.update(x, data)
    new_blog = blog_schema.dump(updated)
    return new_blog

def delete_blog(post_id):
    x = Blog.get_one_blog(post_id)
    x.delete()
    return "Deleted"

def fetch_one_blog(post_id):
    x = Blog.get_one_blog(post_id)
    blog_posts = blog_schema.dump(x)
    return blog_posts