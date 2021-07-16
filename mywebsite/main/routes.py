from flask import render_template, flash, redirect, url_for, request, abort, current_app, Blueprint
from flask_login import current_user, login_required
from mywebsite import db, limiter 
from mywebsite.models import Project, Home
from mywebsite.main.forms import HomeForm

main = Blueprint('main', __name__) #string main is the directory main, __name__ is where it located

@main.route('/')
@main.route('/home')
def home():
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME'] #admin email(this email in enviroment file)
    return render_template('home.html', admin_email=admin_email, admin_task=admin_task, home=home)

@main.route('/home/create', methods=['GET', 'POST'])
@login_required
@limiter.limit('5 per day', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def create_home():
    #query to last one
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME'] #admin email(this email in enviroment file)
    # only admin update home page
    if current_user.email != admin_email:
        abort(403)
    # check form is valid on submit
    form = HomeForm()
    if form.validate_on_submit():
        home = Home(greeting=form.greeting.data, position=form.position.data, about_me_overview=form.about_me_overview.data, about_me=form.about_me.data, task=form.task.data)
        db.session.add(home)
        db.session.commit()
        flash('New home has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_home.html', title='About Me Create', form=form, admin_email=admin_email, admin_task=admin_task)

@main.route('/home/update', methods=['GET', 'POST'])
@login_required
@limiter.limit('5 per day', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def update_home():
    #query to last one
    admin = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = admin.task
    admin_email = current_app.config['MAIL_USERNAME'] #admin email(this email in enviroment file)
    # only admin update home page
    if current_user.email != admin_email:
        abort(403)
    # check form is valid on submit
    form = HomeForm()
    if form.validate_on_submit():
        # save admin in the form to database
        admin.greeting = form.greeting.data
        admin.position = form.position.data
        admin.about_me_overview = form.about_me_overview.data
        admin.about_me = form.about_me.data
        admin.task = form.task.data
        db.session.commit()
        flash('Home has been updated!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        # popup value from the admin database to the update home page
        form.greeting.data = admin.greeting
        form.position.data = admin.position
        form.about_me_overview.data = admin.about_me_overview
        form.about_me.data = admin.about_me
        form.task.data = admin.task
    return render_template('update_home.html', title='About Me Update', admin_email=admin_email,  admin_task=admin_task, form=form)

@main.route('/home/before_delete')
@login_required
@limiter.limit('5 per day', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def before_delete_home():
    admin_email = current_app.config['MAIL_USERNAME'] #admin email(this email in enviroment file)
    # only admin to do flowing steps
    if current_user.email != admin_email:
        abort(403)
    # query all
    homes = Home.query.all() #home must contain at least 1 instance bc I created an instance before deploy this website
    if len(homes) <= 1:
        flash("There is only one home page in the database. I'm not allowed myself to delete this home", 'warning')
        return redirect(url_for('main.home'))
    admin_task = homes[-1].task
    return render_template('before_delete_home.html', title='About Me Delete', admin_email=admin_email, admin_task=admin_task, homes=homes, uniform=True)

@main.route('/home/<int:home_id>/delete', methods=['GET','POST'])
@login_required
@limiter.limit('5 per day', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def delete_home(home_id):
    home = Home.query.get_or_404(home_id)
    if current_user.email != current_app.config['MAIL_USERNAME']:
        abort(403)
    if request.method == 'GET':
        flash("Since I was on GET DELETE, home has not been deleted!", 'warning')
        return redirect(url_for('main.home'))
    db.session.delete(home)
    db.session.commit()   
    flash('Home has been deleted!', 'success')
    return redirect(url_for('main.home'))

@main.route('/project')
def project():
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    ## page and sort_category query parmeters from url
    page = request.args.get('page', 1, type=int)
    sort_category = request.args.get('sort_category', 'All', type=str)
    if sort_category == 'All':
        projects = Project.query.order_by(Project.date.desc()).paginate(page=page, per_page=5) 
    elif sort_category == 'AI' or sort_category == 'Web' or sort_category == 'Electronic':
        projects = Project.query.filter_by(category=sort_category).order_by(Project.date.desc()).paginate(page=page, per_page=5) 
    else:
        abort(404)
    return render_template('project_overview.html', title='Project Page', admin_email=admin_email, admin_task=admin_task, uniform=True, projects=projects, sort_category=sort_category)
