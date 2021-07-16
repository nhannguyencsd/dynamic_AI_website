from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from mywebsite.configuration import configuration
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json

with open('/etc/config.json') as config_file:
        config = json.load(config_file)

# intances flask extensions
db =  SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager() #add somefunction to database model and handle sessions and background 
login_manager.login_view = 'users.login' #the login is the name of the route in mywebsite/routes
login_manager.login_message_category = 'primary'
mail = Mail()
limiter = Limiter(storage_uri=config.get('REDIS_URI'), key_func=get_remote_address, default_limits=["500 per day"])


#application factory
def create_app(configuration_name=config.get('CONFIGURATION_NAME') or 'development'):
    # flask instace and its config
    app = Flask(__name__) #app is an instance of Flask
    app.config.from_object(configuration[configuration_name]) #all variables in configuration pass to app.config
    # intances flask extensions
    # note that: the extension object does not initally get bound to the application so using init_app function
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)
    # blueprints
    from mywebsite.main.routes import main #main is a varible in mywebsite/main/routes.py
    from mywebsite.users.routes import users #users is a varible in mywebsite/users/routes.py
    from mywebsite.projects.routes import projects #projects is a varible in mywebsite/projects/routes.py
    from mywebsite.comments.routes import comments #comments is a varible in mywebsite/comments/routes.py
    from mywebsite.errors.handlers import errors #ais is a varible in mywebsite/ais/routes.py
    # register those blueprint into mywebsite package
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(projects)
    app.register_blueprint(comments)
    app.register_blueprint(errors)
    # returning app
    return app

