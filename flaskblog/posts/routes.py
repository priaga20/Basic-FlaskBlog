# putting ( ) allows us to break the line if it is getting too long
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


# also accepting get and post request to this route
@posts.route("/post/new", methods=['GET', 'POST'])
# to add a new post user must be logged in so adding this @login_required decorator 
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    # passing legend as a parameter bcoz using same template for creating and updating a post
    # so that title displayed accurately for each
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


# flask gives us the ability to add variables to our routes
# so creating a route where post id is actually a part of the route 
# can put this variable into the URL itself
# if user goes to post 1 then post_id will be 1 and so on.
# we are acceptng post id and that's gonna be an integer so making it more specific
@posts.route("/post/<int:post_id>")
def post(post_id):
    # using get method bcoz getting something by id 
    # but here using get_or_404 which means get the post with post_id but if it doesn't exist then return 404 i.e. page doesn't exist
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        # maually aborting and returning a error response
        # http response for a forbidden route
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        # no need of db.session.add() bcoz already in DB we are just updating the existing entry
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':  # populating form with values only if it's a GET request
        # initially when user goes to update post displaying already existing title and content into form
        # so that easy for user to make changes
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')

# only POST request for this route
@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
