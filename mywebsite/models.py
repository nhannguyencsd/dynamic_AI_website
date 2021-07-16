from mywebsite import db, login_manager
from flask import current_app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Home(db.Model):
    __tablename__ = 'homes' # if this line is not set, the default table name is home
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    greeting = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    about_me_overview = db.Column(db.String(200), nullable=False)
    about_me = db.Column(db.Text, nullable=False)
    task = db.Column(db.String(200), nullable=False)

    # show when print it
    def __repr__(self):
        return f"Home('id: {self.id}', 'about_me_overview: {self.about_me_overview}', 'date: {self.date}')"

#the extension flask_login give models to have some attributes and methods from class UserMixin
#For example:  is_authenticated, is_active, is_anonymous and get_ID
class User(db.Model, UserMixin):
    __tablename__ = 'users' # if this line is not set, the default table name is user
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(127), nullable=False)
    attempt = db.Column(db.Integer, default=0, nullable=False)
    image = db.Column(db.String(200), default='default.png', nullable=False)
    run_count = db.Column(db.Integer, default=0, nullable=False)
    run_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    projects = db.relationship('Project', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    # reset token during experies_second second
    def get_reset_token(self, expires_second=1800): #30*60
        s =  Serializer(current_app.config['SECRET_KEY'], expires_second)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s =  Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except: #invalid token or expired token in this case
            return None
        return User.query.get_or_404(user_id)

    # show when print it
    def __repr__(self):
        return f"User('username: {self.username}','email: {self.email}', 'attempt: {self.attempt}', 'image: {self.image}', 'run_count: {self.run_count}', 'run_date: {self.run_date}')"

class Project(db.Model):
    __tablename__ = 'projects' # if this line is not set, the default table name is project
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    image = db.Column(db.String(200), nullable=False, default='https://images.unsplash.com/photo-1566443280617-35db331c54fb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80')
    content = db.Column(db.Text, nullable=False)
    model_name = db.Column(db.String(100), nullable=False)
    need_input = db.Column(db.String(20), nullable=False)
    weight = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='project', cascade="all, delete-orphan", lazy=True)

    # show when print it
    def __repr__(self):
        return f"Project('title: {self.title}','date: {self.date}','category: {self.category}', 'image: {self.image}', 'model_name: {self.model_name}', 'need_input: {self.need_input}', 'weight: {self.weight}')"       

class Comment(db.Model):
    __tablename__ = 'comments' # if this line is not set, default table name is comment
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id= db.Column(db.Integer, db.ForeignKey('projects.id'))

    # show when print it
    def __repr__(self):
        return f"Comment('date: {self.date}')"



#this name is convention
@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(int(user_id))