from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # to paginate all posts instead of using query.all() use paginate method
    # posts = Post.query.all()
    # requesting page no from URL, default set as 1, type=int ensures if anyhting other than int is given then error is raised
    page = request.args.get('page', 1, type=int)
    # 5 posts per page
    # posts = Post.query.paginate(page=page, per_page=5)
    # using order by to show latest post first on the page
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts) #not passing any title so default used


@main.route("/about")
def about():
    return render_template('about.html', title='About') #passing a title explicitly