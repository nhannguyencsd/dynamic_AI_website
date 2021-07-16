from flask import render_template, flash, redirect, url_for, request, abort, current_app, Blueprint
from flask_login import current_user, login_required
from mywebsite import db, limiter
from mywebsite.projects.forms import ProjectForm
from mywebsite.comments.forms import CommentForm
from mywebsite.ais.forms import AIForm
from mywebsite.models import Home, Project, Comment
from mywebsite.projects.utils import save_aidotpy, save_weight, is_new_day
from datetime import datetime, timedelta
import timeago
import os

projects = Blueprint('projects', __name__) #string projects is the directory projects, __name__ is where it located

@projects.route('/project/create', methods=['GET', 'POST'])
@login_required
@limiter.limit('5 per day', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def create_project():
    # about ai.py file
    is_aidotpy_failed = False
    try: 
        from mywebsite.ais import ai
    except: 
        is_aidotpy_failed = True
    # about admin
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    # only admin create project
    if current_user.email != current_app.config['MAIL_USERNAME']:
        abort(403)
    # check form is valid on submit
    form = ProjectForm()
    if form.validate_on_submit():
        # deal with ai.py file
        if form.aidotpy.data: #validate on submit with attach aidotpy file
            save_aidotpy_info = save_aidotpy(form.aidotpy.data)
            if save_aidotpy_info == 1:
                abort(405) #got to this point here means it will not create project with filename which is different than "ai.py"
            print('Project created with ai.py')
        else: #validate on submit without attach weight file
            print('Project created without ai.py')
        # deal with weight file
        if form.category.data == 'AI' and form.model_name.data == '': #handle for acidently when create AI project with submit model_name=''
            abort(405)
        weight_filename = ''
        if form.model_name.data != '':  #if model_name != '', it is AI project. If model_name == '', it is a Web/Electronic project
            weight_filename = 'no need weight'
            if form.weight.data: #AI model validate on submit with attach weight file
                save_weight_info = save_weight(form.weight.data, form.model_name.data)
                if save_weight_info == 1:
                    abort(405) #got to this point here means it will not update project with empty model name
                weight_filename = save_weight_info #at here weight_filename = model_name.pt or model_name.pth
        # save project in the form to database
        project = Project(category=form.category.data, title=form.title.data, image=form.image.data, content=form.content.data, model_name=form.model_name.data, need_input=form.need_input.data, weight=weight_filename,  author=current_user)
        db.session.add(project)
        db.session.commit()
        flash('Project has been been created!', 'success')
        return redirect(url_for('projects.project', project_id=project.id))
    return render_template('create_project.html', title='Create Project Page', admin_email=admin_email, admin_task=admin_task, form=form, is_aidotpy_failed=is_aidotpy_failed)

@projects.route('/project/<int:project_id>', methods=['GET', 'POST'])
@limiter.limit('1000 per day')
def project(project_id):
    # about ai.py file
    is_aidotpy_failed = False
    try: 
        from mywebsite.ais import ai
    except: 
        is_aidotpy_failed = True
    # about admin
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    #query to retreive a needed project 
    project = Project.query.get_or_404(project_id)
    #query comments
    comment_form = CommentForm() # page query parmeter from url
    page = request.args.get('page', 1, type=int)
    pagination_comments = Comment.query.filter_by(project_id=project.id).order_by(Comment.date).paginate(page=page, per_page=10)
    now = datetime.utcnow() # current time 
    readable_dates = [timeago.format(comment.date, now) for comment in pagination_comments.items] # timeago for comments
    readable_comments = zip(pagination_comments.items, readable_dates) # timeago for comments
    # create aiform at project page
    input = None
    output = None
    ai_form = AIForm()
    if ai_form.validate_on_submit() and request.form['submit'] == 'Run':
        #check time pass to new day
        start = current_user.run_date.replace(hour=0, minute=0, second=0, microsecond=0) #midnight of that date
        current = datetime.utcnow()
        if is_new_day(start=start, current=current): #to reset current_user.run_count
            current_user.run_count = 0
            current_user.run_date = datetime.utcnow()
            db.session.commit()
        # allow to run a model for 3 times   
        if current_user.run_count <= 2: #allow to run
            if current_user.email != admin_email: #increase count for regular user
                current_user.run_count += 1
            input = ai_form.input.data
            try:
                #get right model
                model_name = project.model_name
                model_class = getattr(ai, model_name)
                model_instance = model_class()
                # get the output for deep learning model or regular model(not deep learning model)
                weight_filename = model_name + '.pt'
                weight_path = os.path.join(current_app.root_path, 'static/weights', weight_filename)
                #check the type of model
                if os.path.isfile(weight_path):##it is deep learning model.
                    output = model_instance.get_result(input, weight_path)
                    # failure working with thread
                    if output == 'Thread failure':
                        abort(500)
                else: ##it is a regular model
                    output = model_instance.get_result(input)
                # come to this point if success return output with string type
                if isinstance(output, str):
                    times = 2 - current_user.run_count + 1
                    current_user.run_date = datetime.utcnow()
                    db.session.commit()
                    if times > 1:
                        flash(f'You have two more times for running any models today. Please see the result at the bottom of this page.', 'success')
                    elif times == 1:
                        flash(f'You have one more time for running any models today. Please see the result at the bottom of this page.', 'success')
                    else: 
                        midnight = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) #midnight of current date
                        wait_time = midnight + timedelta(days=1) - datetime.utcnow()
                        flash(f'You have reached the limit three times a day for running any models. Please wait in {str(wait_time).split(".")[0]} to have three more times again.', 'info')
                    return render_template('project_detail.html', title=project.title, admin_email=admin_email, admin_task=admin_task, project=project, comment_form=comment_form, pagination_comments=pagination_comments, readable_comments=readable_comments, uniform=True, is_aidotpy_failed=is_aidotpy_failed, ai_form=ai_form, input=input, output=output)
                else:
                    abort(500)
            except:
                abort(500)
        else: #not allow to run
            midnight = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) #midnight of current date
            wait_time = midnight + timedelta(days=1) - datetime.utcnow()
            flash(f'You have reached the limit three times a day for running any models. Please wait in {str(wait_time).split(".")[0]} to have three more times again.', 'info')
            return redirect(url_for('projects.project', project_id=project.id))
    #comment create at project page
    if comment_form.validate_on_submit() and request.form['submit'] == 'Comment':
        if current_user.is_authenticated:
            comment = Comment(content=comment_form.content.data, project=project, author=current_user)
            db.session.add(comment)
            db.session.commit()
            flash('Your comment has been submmited!', 'success')
        else:#I think it never hit it case
            flash('Login to comment!', 'info')
        return redirect(url_for('projects.project', project_id=project.id))
    return render_template('project_detail.html', title=project.title, admin_email=admin_email, admin_task=admin_task, project=project, comment_form=comment_form, pagination_comments=pagination_comments, readable_comments=readable_comments, uniform=True, is_aidotpy_failed=is_aidotpy_failed, ai_form=ai_form, input=input, output=output)

@projects.route('/project/<int:project_id>/update', methods=['GET', 'POST'])
@login_required
@limiter.limit('5 per day', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def update_project(project_id):
    # about ai.py file
    is_aidotpy_failed = False
    try: 
        from mywebsite.ais import ai
    except: 
        is_aidotpy_failed = True
    # about admin
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    # only admin update a project
    if current_user.email != admin_email:
        abort(403)
    #query to retreive the one that need to be updated
    project = Project.query.get_or_404(project_id) 
    # check form is valid on submit
    form = ProjectForm()
    if form.validate_on_submit():
        # deal with ai.py file
        if form.aidotpy.data: #validate on submit with attach aidotpy file
            save_aidotpy_info = save_aidotpy(form.aidotpy.data)
            print('Project updated with ai.py')
        else: #validate on submit without attach weight file
            print('Project updated with no ai.py')
        # deal with weight file
        if form.category.data == 'AI' and form.model_name.data == '': #handle for acidently when create AI project  with submit model_name=''
            abort(405)
        weight_filename = ''
        if form.model_name.data != '':  #if model_name != '', it is AI project. If model_name == '', it is a Web/Electronic project
            weight_filename = 'no need weight'
            if form.weight.data: #AI model validate on submit with attach weight file
                save_weight_info = save_weight(form.weight.data, form.model_name.data)
                if save_weight_info == 1:
                    abort(405) #got to this point here means it will not update project with empty model name
                weight_filename = save_weight_info #at here weight_filename = model_name.pt or model_name.pth
            else: #AI model validate on submit without attach weight file
                if project.weight != 'no need weight': #for deep learning model summit  without choose weight file
                    weight_filename = form.model_name.data + '.pt'
                    weight_path = os.path.join(current_app.root_path, 'static/weights', weight_filename)
                    if not os.path.isfile(weight_path):#check if model_name change on update project
                        weight_filename = f'There is no {weight_filename}'
        # save project in the form to database
        project.category = form.category.data
        project.title = form.title.data
        project.image = form.image.data
        project.content = form.content.data
        project.model_name = form.model_name.data
        project.need_input = form.need_input.data
        project.weight = weight_filename
        db.session.commit()
        flash('Project has been updated!', 'success')
        return redirect(url_for('projects.project', project_id=project.id))
    elif request.method == 'GET':
        # popup value from the project database to the update project page
        form.category.data = project.category
        form.title.data = project.title
        form.image.data = project.image
        form.content.data = project.content
        form.model_name.data = project.model_name
        form.need_input.data = project.need_input
    return render_template('update_project.html', title='Update Project Page', admin_email=admin_email, admin_task=admin_task, form=form, is_aidotpy_failed=is_aidotpy_failed, weight_filename=project.weight)

@projects.route('/project/<int:project_id>/delete', methods=['GET','POST'])
@login_required
@limiter.limit('5 per day', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    if current_user.email != current_app.config['MAIL_USERNAME']:
        abort(403)
    if request.method == 'GET':
        flash("Since I was on GET DELETE, project has not been deleted!", 'warning')
        return redirect(url_for('projects.project', project_id=project.id))
    db.session.delete(project)
    db.session.commit()   
    flash('Project has been deleted!', 'success')
    return redirect(url_for('main.project'))