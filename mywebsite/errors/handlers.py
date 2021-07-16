from flask import Blueprint, render_template, request, current_app

errors = Blueprint('errors', __name__) #string errors is the directory errors, __name__ is where it located

@errors.app_errorhandler(403) #instead of using decorator @errors.route using decorator @errors.app_errorhandler
def error_403(error):
    admin_email = current_app.config['MAIL_USERNAME']
    return render_template('errors/403.html', title="403 Error Page", admin_email=admin_email, uniform=True, no_footer=True), 403

@errors.app_errorhandler(404) #instead of using decorator @errors.route using decorator @errors.app_errorhandler
def error_404(error):
    admin_email = current_app.config['MAIL_USERNAME']
    return render_template('errors/404.html', title="404 Error Page", admin_email=admin_email, uniform=True, no_footer=True), 404

@errors.app_errorhandler(405) #instead of using decorator @errors.route using decorator @errors.app_errorhandler
def error_405(error):
    admin_email = current_app.config['MAIL_USERNAME']
    return render_template('errors/405.html', title="405 Error Page", admin_email=admin_email, uniform=True, no_footer=True), 405

@errors.app_errorhandler(429) #instead of using decorator @errors.route using decorator @errors.app_errorhandler
def error_429(error):
    admin_email = current_app.config['MAIL_USERNAME']
    print(request.endpoint)
    return render_template('errors/429.html', title="429 Error Page", admin_email=admin_email, uniform=True, no_footer=True), 429


@errors.app_errorhandler(500) #instead of using decorator @errors.route using decorator @errors.app_errorhandler
def error_500(error):
    admin_email = current_app.config['MAIL_USERNAME']
    return render_template('errors/500.html', title="500 Error Page", admin_email=admin_email, uniform=True, no_footer=True), 500