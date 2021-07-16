from flask import render_template, flash, redirect, url_for, request, session, current_app, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mywebsite import db, bcrypt, limiter
from mywebsite.users.forms import (RegistrationForm, LoginForm, AccountForm,
                                   RequestResetForm, ResetPasswordForm)
from mywebsite.models import Home, User, Comment
from mywebsite.users.utils import save_image, delete_image, send_thread_reset_email
from datetime import datetime
import timeago


users = Blueprint('users', __name__) #string users is the directory users, __name__ is where it located


@users.route('/register', methods=['GET', 'POST'])
def register():
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    if current_user.is_authenticated:
        return redirect(url_for('main.project'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"You've been successfully created account!", 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register Page', admin_email=admin_email, admin_task=admin_task, form=form, footer=True)

@users.route('/login',  methods=['GET', 'POST'])
# @limiter.limit('100 per day;50 per hour', exempt_when= lambda : current_user.is_authenticated) #also the limit of login GET depend on the limit of another routes
def login(): #Note about login: GET -> POST-> REDIRECT
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    #save previous url after hit login with method=GET
    if request.method == 'GET':
        session['url'] = request.referrer
    #redirect to project route after authenticate user
    if current_user.is_authenticated:
        return redirect(url_for('main.project'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.attempt < 5 and bcrypt.check_password_hash(user.password, form.password.data):
            #Guess: login_user -> login_manager ->  UserMixin 
            # -> is_authenticated, is_active, is_anonymous and get_ID take 2 parameters (user, login_manager.user_loader)
            login_user(user, remember=form.remember.data)
            user.attempt = 0
            db.session.commit()
            flash(f"You've been successfully logged in!", 'success')
            next = request.args.get('next')
            if next: #redirect to the next page if next existed
                return redirect(next) #next page
            else: #redirect to the previous page(previous url) if next not existed
                previous = session.get('url') 
                if previous:
                    return redirect(previous)
                else: #come to this point because the user paste the login address to url bar in the browser
                    return redirect(url_for('main.project'))
        else:
            count = 0
            if user: # increase login attempt when login failed for the user in the database
                user.attempt += 1
                if user.attempt >= 5:
                    user.attempt = 5
                db.session.commit()
                count = user.attempt
            if count <= 4: #login FAIL
                flash('Login unsuccessful. Please check your email and password', 'danger')
            else: #login FAIL
                flash('This account has been blocked for security reasons', 'danger')
                flash('If you own this account, please click on Reset Password', 'warning')
    return render_template('login.html', title='Login Page', admin_email=admin_email, admin_task=admin_task, form=form)


@users.route('/logout')
def logout():
    logout_user()
    flash(f"You've been successfully logged out!", 'success')
    return redirect(url_for('users.login'))

@users.route('/account', methods=['GET', 'POST'])
@login_required
@limiter.limit('200 per day;120 per hour', exempt_when= lambda : current_user.email == current_app.config['MAIL_USERNAME'])
def account():
    # about admin
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    #check validated on submit
    form = AccountForm()
    if form.validate_on_submit(): #post method
        current_user.username = form.username.data
        current_user.email = form.email.data
        is_saved = False
        if form.image.data:
            old_image_file = current_user.image
            image_file = save_image(form.image.data)
            current_user.image = image_file
            is_saved = True
        db.session.commit()
        if is_saved:#delete old image after it update new image
            delete_image(old_image_file)
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET': #get method
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='images/user/' + current_user.image)
    return render_template('account.html', title='Account Page ', admin_email=admin_email, admin_task=admin_task, image=image, form=form)

@users.route('/view_comments/<username>')
def view_user_comments(username):
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    pagination_comments = Comment.query.filter_by(author=user).order_by(Comment.date.desc()).paginate(page=page, per_page=10)
    now = datetime.utcnow() # current time 
    readable_dates = [timeago.format(comment.date, now) for comment in pagination_comments.items] # timeago for comments
    readable_comments = zip(pagination_comments.items, readable_dates) # timeago for comments
    return render_template('view_user_comments.html', title='User Comments Page', admin_email=admin_email, admin_task=admin_task, user=user, pagination_comments=pagination_comments, readable_comments=readable_comments, uniform=True)

# step1 of reset password: request 
# request take innput from form. it means take email
# by query that input email got the user in database
# since got a user in database call send_reset_email
@users.route('/reset_password', methods=['GET', 'POST'])
@limiter.limit('10 per day') #10 because try to avoid spam email
def reset_request():
    home = Home.query.order_by(Home.id.desc()).first_or_404()
    admin_task = home.task
    admin_email = current_app.config['MAIL_USERNAME']
    if current_user.is_authenticated:
        return redirect(url_for('main.project'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()
        try:
            send_thread_reset_email(user)
        except:
            abort(500)
        flash('An email has been sent with a link to reset your password', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Request Password Page', admin_email=admin_email, admin_task=admin_task, form=form)


# step 3 of reset password: verify token and enter new password
#input step 3 form the link in send email from step 2
#when click on valid link it, this route will verify the token 
# if it is an invalid token, then it redirect to reset_request route
# if it is a valid token, then it render templater for enter new password
@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.project'))
    user = User.verify_reset_token(token) #it's defined in models.py
    if user is None:
        flash('That token is invalid or expired', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        user.attempt = 0
        db.session.commit()
        flash(f"You've been successfully updated password!", 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password Page', form=form)