from mywebsite import create_app
from werkzeug.serving import run_simple #to fix the issue of default choice
app = create_app()

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)#alias(default choice) want to be change for every time change the code but debug=True leave the code when using production which is DANGER 
    run_simple(application=app, hostname='0.0.0.0', port=5000, use_debugger=False, use_reloader=True, threaded=True) #to fix the issue of default choice