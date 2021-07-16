from flask import redirect, url_for, request, abort, flash, current_app, Blueprint
from flask_login import current_user, login_required
from mywebsite import db
from mywebsite.models import Comment

comments = Blueprint('comments', __name__) #string comments is the directory comments, __name__ is where it located

#note that comment created in project route in the mywebsite/projects/routes.py
#but I can create comment route in this file by moving the code
#that take care create comment in mywebsite/projects/routes.py to this file

@comments.route('/comment/<int:comment_id>/update', methods=['POST'])
@login_required
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    project_id= comment.project_id
    if comment.author != current_user:
        abort(403)
    comment.content = request.form['forming']
    db.session.commit()
    return redirect(url_for('projects.project', project_id=project_id))

@comments.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    admin_email = current_app.config['MAIL_USERNAME']
    comment = Comment.query.get_or_404(comment_id)
    project_id= comment.project_id
    if current_user.email != admin_email and current_user != comment.author:
        abort(403)
    db.session.delete(comment)
    db.session.commit()   
    flash('That comment has been deleted!', 'success')
    return redirect(url_for('projects.project', project_id=project_id))