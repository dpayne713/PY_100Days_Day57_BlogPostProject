from flask import Flask, render_template
from post import Post
import datetime as dt
app = Flask(__name__)
posts = Post()

global_data = {
    "year": dt.datetime.now().year,
    "location": "Nashville"
}

@app.route('/')
def home():
    all_posts = posts.blog_posts
    return render_template("index.html", posts=all_posts, global_data=global_data)

@app.route('/posts/<num>')
def post(num):
    return render_template("post.html", post=posts.post_by_id(num), global_data=global_data)

if __name__ == "__main__":
    app.run(debug=True)