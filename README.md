#### DAY 0
1. Create project folder
   * $ mkdir projects
   * $ cd projects
   * $ mkdir my_website
   * $ cd my_website
2. Initialize track log
   * $ git init
   * $ ls -la
   * $ touch README.md
3. Create virtual enviroment and install flask
   * $ python3 -m venv flask_env
   * $ ls -la
   * $ source flask_env/bin/activate
   * $ pip list
   * $ pip install flask
   * $ pip list
   * $ git status
   * $ git add -A
   * $ git commit -m 'Create folder, track log, virtual enviroment in day 0'
   * $ git status
   * $ git log
------------------
#### DAY 1
1. Run simple flask app
    * $ touch mywebsite.py
    * code in that mywebsite.py
    * $ export FLASK_APP=mywebsite.py
    * $ flask run
    * OPEN IP address link in terminal or enter localhost:500 in browser
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Run simple flask app in day 1 part 1'
    * $$ git status
    * $$ git log
2. Run simple flask app update with change using enviroment variable
    * $ Ctrl-C
    * $ export FLASK_DEBUG=True
    * $ flask run
    * browser to localhost:5000
    * $ code in mywebsite.py
    * refresh the webpage
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Run simple flask app in day 1 part 2'
    * $$ git status
    * $$ git log
3. Run simple flask app update with change without using enviroment variable
    * code in mywebsite.py
    * $ Ctrl-C
    * $ python mywebsite.py
    * add home route to mywebsite.py
    * browser to localhost:5000/home
    * add about route to mywebsite.py
    * browser to localhost:5000/about
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Run simple flask app in day 1 part 3'
    * $$ git status
    * $$ git log
------------------
#### DAY 2
1. Start using template
    * code in mywebsite.py    
    * $ mkdir templates
    * $ touch templates/home.html
    * $ touch templates/about.html=
    * code in home.html
    * code in about.html
    * $ python mywebsite.py
    * browser to localhost:5000/home and localhost:5000/about then view page source for each route
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Use flask template in day 2 part 1'
    * $$ git status
    * $$ git log
2. Pretend use database by using dummy variable and use jinja
    * creat posts varibale in mywebsite.py
    * add title in about route in mywebsite.py
    * code in home.html and about.html
    * browser to home route and about route
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Use dummy variables and jinja in day2 part 2'
    * $$ git status
    * $$ git log
3. Refractor template using template inheritance
    * $$ touch templates/layout.html
    * create block in that layout.html
    * code in home.html and about.html
    * browser to home route and about route
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Refractor template using template inheritance in day 2 part 3'
    * $$ git status
    * $$ git log
4. Use Bootstrap after applying template inheritance
    * go to get started of getboostrap.com
    * at starter template copy link tag and scripts tag to layout.html
    * code in layout.html
    * browser to home route and about route
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Use bootstrap after applying template inheritance in day 2 part 4'
    * $$ git status
    * $$ git log
5. Use url_for function
    * [download bootstrap files](https://github.com/twbs/bootstrap/releases/download/v4.5.0/bootstrap-4.5.0-dist.zip)
    [download jquery](https://code.jquery.com/jquery-3.5.1.min.js)
    * extract them all then you see these file:
      * bootstrap.min.css
      * bootstrap.min.js
      * jquery-3.5.1.min.js
    * $$ mkdir -p static/styles/vendor
    * copy bootstrap.min.css to static/styles/vendor
    * $$ mkdir -p static/scripts/vendor
    * copy bootstrap.min.js and jquery-3.5.1.min.js to static/scripts/vendor
    * modify link and script html with url_for fuction in layout.html
    * browser home and route.html
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Use url_for function in day 2 part 5'
    * $$ git status
    * $$ git log
6. Design my website that look better
    * rename about.html to project.html, code in mywebsite.py
    * [download fontawesome](https://use.fontawesome.com/releases/v5.14.0/fontawesome-free-5.14.0-web.zip)
    * after extract zip file, copy fontawesome-free-5.14.0-web to static/styles/vendor
    * add fontawesome link and icon tag to layout.html
    * browse to home route and project route
    * mkdir static/images
    * [download free image1](https://pixabay.com/vectors/laptop-computer-portable-pc-2298286/)
    * [download free image2](https://pixabay.com/vectors/statistic-wordpress-web-data-1820320/)
    * [download free image3](https://undraw.co/illustrations)
    * photoshop first two images into a single image and save as about.png, rename third image to project.svg
    * make avarta image and name avarta.png
    * copy all 4 renamed images to static/images
    * add block top in layout.html and block top in home.html
    * code mywebsite.py
    * code layout.html
    * code home.html and project.html
    * code block content in project.html
    * add footer in layout.html
    *  [download free icon1](https://www.iconfinder.com/icons/670432/in_linked_linkedin_media_social_icon) and rename to contact1.svg
    *  [download free icon2](https://www.iconfinder.com/icons/3185260/circle_design_email_gmail_mail_material_message_icon) and rename to contact2.png
    *  [download free icon3](https://www.iconfinder.com/icons/1298743/git_github_logo_social_icon) and rename to contact3.png
    * copy contact1.svg, contact2.png and contact3.png to /static/images
    * $ touch static/styles/main.css
    * code that main.css and link for main.css in layout.html
    * browse home route and project route 
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Design my website look better in day 2 part 6'
    * $$ git status
    * $$ git log
------------------
#### DAY 3
1. Create RegistrationForm/LoginForm and their routes
    * Fix overlaping design and some minor issue
        * convert project.svg to project.png and link with correct name in project.html
        * use url_for in every href attribute
    * $$ source flask_env/bin/activate
    * $$ pip install flask-wtf
    * $$ pip install email_validator
    * $$ touch forms.py
    * code that forms.py file
    * to prevent modyfying cookies and cross-site request forgery attacks, add secret key to mywebsite.py
    * $$ python
    * $$ import secrets 
    * $$ secrets.token_hex(16)
    * $$ Ctrl-D
    * copy that secret key to app.config['SECRET_KEY'] in mywebsite.py
    * create register route and login route in mywebsite.py
    * $$ touch templates/register.html
    * $$ touch templates/login.html
    * code form in those register.html and login.html
    * code flash in mywebsite.py and layout.html file
    * code in register route and login route in mywebsite.py
    * code in main.css
    * browse all routes
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Create RegistrationForm/LoginForm and their routes in day 3'
    * $$ git status
    * $$ git log
------------------
#### DAY 4
1. Create RegistrationForm/LoginForm and their routes
    * $$ pip install flask-sqlalchemy
    * Initial databse in mywebsite.py
    * Create User model, Post model and Comment model in mywebsite.py
2. Create user datatbase in terminal
    * $$ python
    * $$ from mywebsite import db
    * $$ db.create_all()
    * $$ from mywebsite import User, Post, Comment
    * $$ user_1 = User(username='Nhan', email='nhan@demo.com', password='password')
    * $$ db.session.add(user_1)
    * $$ user_2 = User(username='Thinh', email='thinh@demo.com', password='password')
    * $$ db.session.add(user_2)
    * $$ db.session.commit()
    * $$ User.query.all()
    * $$ User.query.first()
    * $$ User.query.filter_by(username='Nhan').all()
    * $$ User.query.filter_by(username='Nhan').first()
    * $$ user = User.query.filter_by(username='Nhan').first()
    * $$ user
    * $$ user.id
    * $$ user = user.query.get(1)
    * $$ user
    * $$ user.posts
    * $$ user.comments
    * $$ Ctrl-l
3. Create post datbase in terminal
    * $$ post_1 = Post(title='First title', category='First category', content='First post content', user_id=user.id)
    * $$ post_1
    * $$ post_2 = Post(title='Second title', category='Second category', content='First post content', user_id=user.id)
    * $$ db.session.add(post_1)
    * $$ db.session.add(post_2)
    * $$ db.session.commit()
    * $$ user.posts
    * $$ for post in user.posts:
            print(post.category)
    * $$ post = Post.query.first()
    * $$ post
    * $$ post.user_id
    * $$ post.author
    * $$ Ctrl-l
4.  Create post datbase in terminal
    * $$ user = user.query.get(2)
    * $$ user
    * $$ comment_1 = Comment(content='First comment content', user_id=user.id)
    * $$ comment_1
    * $$ comment_2 = Comment(content='Second comment content', user_id=user.id)
    * $$ db.session.add(comment_1)
    * $$ db.session.add(comment_2)
    * $$ db.session.commit()
    * $$ user.comments
    * $$ for comment in user.comments:
            print(comment.content)
    * $$ comment = comment.query.first()
    * $$ comment
    * $$ comment.user_id
    * $$ comment.author
5. Delete database and create new database
    * $$ db.drop_all()
    * $$ db.create_all()
    * $$ User.query.all()
    * $$ Post.query.all()
    * $$ Comment.query.all()
    * $$ Ctrl-D
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Work with databse in terminal in day 4'
    * $$ git status
    * $$ git log
------------------
#### DAY 5
1. Package Structure, avoid circular import of basic method 
    * $$ touch models.py
    * move all models in mywebsite.py to models.py 
    * code in models.py
    * code in mywebsite.py
    * $$ git add -A
    * $$ git commit -m 'Package Structure, avoid circular import of basic method in day 5 part 1'
    * $$ git status
    * $$ git log
2. Package Structure, avoid circular import of basic method fail to create database 
    * $$ rm site.db
    * $$ python
    * $$ from mywebsite import db
    * $$ Ctrl-D
    * the reason that fail because __main__ in models.py cannot import db  because __main__ in models.py which is models module not mywebsite module that contains db
    * $$ git add -A
    * $$ git commit -m 'Package Structure, avoid circular import of basic method in day 5 part 1 with expected failure import db in day 5 part 2'
    * $$ git status
    * $$ git log
3. Package Structure, avoid circular import of best method which not run mywebsite directly  
    * Instead of Packgage Structure in title of part 1 and part 2, it is Import Structure
    * $$ mkdir mywebsite
    * $$ touch mywebsite/__init__.py
    * move all files/directories into mywebsite directory except mywebsite.py, flask_env directory and __pycache__ directoy
    * move code between top and db variable in mywebsite.py to mywebsite/__init__ file
    * $$ touch mywebsite/routes.py
    * move everything except if __main__ part in mywebsite.py to routes.py
    * rename mywebsite.py to run.py
    * code in mywebsite/__init__.py
    * import app in run.py
    * code in mywebsite/routes.py
    * code in models.py
    * python run.py
    * browse all routes
    * $$ python
    * $$ from mywebsite import db
    * $$ from mywebsite.models import User, Post, Comment
    * $$ db.create_all()
    * $$ User.query.all()
    * $$ Ctrl-D
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Package Structure, avoid circular import of best method which not run mywebsite directly in day 5 part 3'
    * $$ git status
    * $$ git log
------------------
#### DAY 6
1. Hash password in command line
    * $$ pip install flask-bcrypt
    * $$ python
    * $$ from flask_bcrypt import Bcrypt
    * $$ bcrypt = Bcrypt()
    * $$ bcrypt
    * $$ bcrypt.generate_password_hash('mypassword')
    * $$ bcrypt.generate_password_hash('mypassword').decode('utf-8')
    * $$ bcrypt.generate_password_hash('mypassword').decode('utf-8')
    * $$ hashed_password = bcrypt.generate_password_hash('mypassword').decode('utf-8')
    * $$ bcrypt.check_password_hash(hashed_password, 'yourpassword')
    * $$ bcrypt.check_password_hash(hashed_password, 'mypassword')
2. Hash password in application
    * code bcrpyt in mywebsite/__init__.py file 
    * modify register in mywebsite/routes.py
    * browse to register route
    * create account in register route
    * check the created account in terminal
    * $$ python
    * $$ from mywebsite import db
    * $$ user = User.query.first()
    * $$ user
    * $$ user.password
    * $$ Ctrl-D
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Hash password in application on day 6 part 2'
    * $$ git status
    * $$ git log
3. Prevent exits user create an account
    * browse register route then create an account with same information to previous one
    * modify RegistrationForm in mywebsite/models.py
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Prevent exits user create an account on day 6 part 3'
    * $$ git status
    * $$ git log
4. User authentication using flask-login extension
    * $$ pip install flask-login
    * add login_manager to mywebsite/__init__.py file
    * add user_loader decorator in models.py
    * add UserMixin to User model in mywebsite/models.py
    * modify the login route in mywebsite/routes.py
    * browser login route enter the credential
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'User authentication using flask-login extension on day 6 part 4'
    * $$ git status
    * $$ git log
5. User authentication with proper login and logout using current_user
    * add current_user in mywebsite/routes.py at register route and login route
    * import logout in mywebsite/routes.py
    * create logout route in mywebsite/routes.py
    * modify mywebsite/templates/layout.html files to toggle login and logout
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'User authentication with proper login and logout using current_user on day 6 part 5'
    * $$ git status
    * $$ git log
6. Create a account route for accessing after logged in
    * create a account route in mywebsite/routes.py
    * $$ touch mywebsite/templates/account.html
    * code in that account.html
    * add account url_for in mywebsite/template/layout.html\
    * browse login and enter email and password then click on account link
    * logout then type localhost:5000/account
    * to fix the [logout then type localhost:5000/account] using login_required
    * add login_required in mywebsite/routes at account route
    * add login_manager.login_view in mywebsite/__init__.py file
    * modify mywebsite/templates/layout.html files to toggle about route
    * browse to login route, account route, logout route and home route
    * enter localhost:5000/acccount and login
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Create an account route for accessing after logged in on day 6 part 6'
    * $$ git status
    * $$ git log
------------------
#### DAY 7
1. User account page
    * $$ mkdir mywebsite/static/images/admin
    * move all images in mywebsite/static/images to mkdir mywebsite/static/images/admin
    * modify code that relate to admin image
    * $$ mkdir mywebsite/static/images/user
    [download free icon](https://www.iconfinder.com/icons/5925671/avatar_profile_user_icon) and renameto default.png
    * copy default.png to mywebsite/static/images/user
    * add image variable in account route of mywebsite/routes.py then pass image to mywebsite/templates/account.html
    * change attribute nn-me to nn-avarta in home.html, account.html and main.css
    * add AccountForm to mywebsite/forms.py
    * add form in account route of mywebsite/routes.py
    * add account form in mywebsite/templates/account.html
    * browse to account route and update username and email
    * import FileField and FileAllowed in mywebsite/forms.py and code in AccountForm
    * update mywebsite/templates/account.html
    * create save_image in mywebsite.py
    * these steps below for resize user image
    * $$ pip install Pillow
    * import PIL to mywebsite/routes.py
    * modify save_image function in that routes.py
    * browse to account route
    * these steps below for delete image
    * add delete_image function 
    * browse to account route and update
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'User account page on day 7'
    * $$ git status
    * $$ git log
------------------
#### DAY 8
0. Once update model in mywebsite/models, create new database
    * rename user_image in User model to image in mywebsite/models
    * rename date_posted in Post and Comment model to date in mywebsite/models
    * change all files that contains old column name of User and Post models
    * add image column to Post model in mywebsite/models.py
    * $$ python
    * $$ from mywebsite import db
    * $$ db.drop_all()
    * $$ db.create_all()
    * $$ Ctrl-D
1. Create Post Page
    * code PostForm to the mywebsite/forms.py
    * deletle posts variable in mywebsite/routes.py
    * add posts variable in project route of mywebsite/routes.py
    * create post/create route in mywebsite/routes.py
    * $$ touch mywebsite/templates/create_post.html
    * modify mywebsite/templates/create_post.html
    * modify mywebsite/templates/project.html
    * browse all routes and localhost:5000/post/create with admin account and regular account
2. Update and delete post page
    * add new route post in mywebsite/routes.py
    * $$ touch mywebsite/templates/post.html
    * code in that post.html
    * update href of title in mywebsite/templates/project.html
    * update .nn-footer and .nn-first-page in mywebsite/styles/main.css
    * create update_post and delete_post routes in mywebsite/routes.py
    * $$ touch mywebsite/templates/update_delete_post.html
    * code in that update_delete_post.html
    * fix footer and body class in mywebsite/template/layout.html
    * delete tag that contain nn-space class in mywebsite/templates/register and login
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Update and delete post page on day 8 part 2'
    * $$ git status
    * $$ git log
3. Create commment below post content in post page
    * modify Comment model and Post model
    * $$ python
    * $$ from mywebsite import db
    * $$ db.drop_all()
    * $$ db.create_all()
    * $$ Ctrl-D
    * Create CommentForm in mywebsite/forms.py
    * add comments to post route in mywebsite/routes.py
    * import timeago and datetime to post route in mywebsite/routes.py 
    * render comment part in mywebsite/templates/post.html
    * add IMPORTANT PRVIOUS URL at login route in mywebsite/routes.py
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Create commment below post content in post page on day 8 part 3'
    * $$ git status
    * $$ git log
4. Update and delete commment below post content in post page
    * rename mywebsite/templates/update_delete_post.html to mywebsite/templates/update_post.html
    * change update_delete_post.html to update_post.html at update_post in mywebsite/routes
    * create macro delete_post_popup in mywebsite/templates/post.html
    * create update_post and delete_post routes in mywebsite/routes.py
    * fix and edit and update button of comment part in mywebsite/templates/post.html
    * create macro comment_popup in mywebsite/templates/post.html
    * browse the website, update and edit comment
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Update and delete commment below post content in post page on day 8 part 4'
    * $$ git status
    * $$ git log
 ------------------
#### DAY Extra
1. Modify database for using AI because change schema database
    * add aidotpy field to PostForm in mywebsite/forms.py in order to upload  ai.py file to the server
    * add weight field to PostForm in mywebsite/forms.py to upload weight file to server
    * add weight column to Post model in mywebsite/models.py to have the filename of weight file in the server
    * add AIForm with contains input field and submit field in the mywebsite/forms.py
    * $$ python
    * $$ from mywebsite import db
    * $$ db.drop_all()
    * $$ db.create_all()
    * $$ pip install torch torchvision
    * $$ Ctrl-D
    * update mywebsite/templates/create_post.html
    * update mywebsite/templates/update_post.html
    * browse website and create admin account, user account, post, and comment 
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Modify database for using AI on day extra part 1'
    * $$ git status
    * $$ git log
2. Deal with aidotpy field and weight field in the new database
    * create ai.py to mywebsite dir file that contain all ai models later on
    * now code HORSE2ZEBRA model in ai.py
    * $$ mkdir mywebsite/static/weights
    * copy HORSE2ZEBRA.pt to mywebsite/static/weight dir
    * use try and except code block to import ai in the top of mywebiste/routes
    * pass is_aidotpy_failed variable in post route of mywebsite/routes
    * render is_aidotpy_failed in mywebsite/templates/post.html
    * add try and except block import ai at post route in mywebsite/routes.py
    * rename form variable to comment_form in at post route in mywebsite/routes.py
    * creatte aiform at post post route in mywebsite/routes.py
    * rename all form to comment_form in mywebsite/templates/post.html
    * render aiform in mywebsite/templates/post.html
    * create save_dotpy function and save_weight function above creat_post and update_post route in mywebsite/routes
    * modify create_post route and  and update_post route in mywebsite/routes in oder to fully create a post or update a post when browsing
    * modify mywebsite/templates/update_post.html, mywebsite/templates/create_post.html in order to show the status of ai.py and current weight filename using
    * mywebsite/templates/post.html in order to show run button or not run when having failure ai.py
3. Produce output at model route. It work but not perfect
    * delete the POST past of input form of the mywebsite/routes.py
    * change action value form '#' to '{{url_for('model', weight=post.id')}}' in input form of the mywebsite/templates/post.html 
    * create a model route in mywebsite/route.py to implement the POST part of input form and getting the output
    * browse the website to run model ai
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Produce the base output of ai model but not perfect on day extra part 2 and part 3 '
    * $$ git status
    * $$ git log
4. Redesign Post model to make proper way create a post, update a bost and proper way to load model route.This one has alot of work!!!
    * add ask_update field, mode and_name field field in the PostForm in mywebsite/forms
    * add model_name column in the Post model in mywebsite/models
    * modify field weight column in the Post model in mywebsite/models
    * $$ python
    * $$ from mywebsite import db
    * $$ db.drop_all()
    * $$ db.create_all()
    * browse website and register, login 
    * render model_name field in mywebsite/templates/create_post.html
    * render ask_update field and model_name field  in mywebsite/templates/update_post.html
    * modify create_post and update_post route in mywebsite/routes acording the change in  mywebsite/templates/create_post.html and update_post.html
    * code script tag below jQuery scirpt tag at the bottom of mywebsite/template/layout.html and add class/id names in mywebsite/templates/creat_post.html and update_post.html in order to make the proper view in create post page and update post page
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Finish AI work on day extra part 4' 
    * $$ git status
    * $$ git log
 ------------------
#### DAY 9
1. Use paginate in a terminal
    * $$ python
    * $$ from mywebsite.models import Post
    * $$ posts = Post.query.paginate()
    * $$ dir(posts)
    * $$ posts.per_page
    * $$ posts.page
    * $$ for post in posts.items: print(post)
    * $$ posts = Post.query.paginate(page=2)
    * $$ posts.page
    * $$ for post in posts.items: print(post)
    * $$ posts = Post.query.paginate(per_page=5)
    * $$ posts.per_page
    * $$ posts.page
    * $$ for post in posts.items: print(post)
    * $$ posts = Post.query.paginate(per_page=5, page=2)
    * $$ posts.per_page
    * $$ posts.page
    * $$ for post in posts.items: print(post)
    * $$ posts.total
    * $$ Ctrl-D
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Learn how to use pagination on day 9 part 1' 
    * $$ git status
    * $$ git log
2. Use pagination in Post object
    * open mywebiste/routes.py at project routes,
    add query parameter page from url 
    change posts = Post.query.paginate(page=page, per_page=5) 
    * change mywebsite/templates/project.html acording to the change of posts variable
    * open browser then go to project page
    * on the project page add ?page=2 in the address bar to see the second page
    * $$ python
    * $$ from mywebsite.models import Post
    * $$ posts = Post.query.paginate(page=6, per_page=2)
    * $$ for page in posts.iter_pages(): print(page)
    * $$ for page in posts.iter_pages(left_current=1, right_current=2, left_edge=1, right_edge=1): print(page)
    * add page_number in mywebsite/templates/project.html to loop over page 
    * $$ Ctrl-D
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Use pagination in Post object on day 9 part 2' 
    * $$ git status
    * $$ git log
3. Add some useful functions to query a Post object
    * change mywebsite/templates/project.html in order ton link page move to the center of the page
    * open mywebiste/routes.py at project routes,
    change posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=5) to display new post on the top old ones
    * change href from google to url_for("project", category=post.category) in mywebsite/templates/project.html
    * fix a minor past from the other day about run button(in mywebsite/templates/post.html) show up for Web and Electronic when guest visit the post page
    * browse the website
    * $$ Ctrl-D
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Add some useful functions to query a Post object on day 9 part 3' 
    * $$ git status
    * $$ git log
4. Paginate all about Comment object
    * open mywebiste/routes.py at post route,
    add query parameter page from url 
    change posts = Post.query.paginate(page=page, per_page=10) and change how query Comment objects with pagination
    * change mywebsite/templates/post.html acording to the change of pagination_comments variable
    * open browser then go to post page

    * on the project page add ?page=2 in the address bar to see the second page
    * $$ python
    * $$ from mywebsite.models import Post
    * $$ posts = Post.query.paginate(page=6, per_page=2)
    * $$ for page in posts.iter_pages(): print(page)
    * $$ for page in posts.iter_pages(left_current=1, right_current=2, left_edge=1, right_edge=1): print(page)
    * add page_number in mywebsite/templates/project.html to loop over page 
    * $$ Ctrl-D
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Use pagination all about Comment object on day 9 part 4' 
    * $$ git status
    * $$ git log
5. Create view comment page for paticular user when clicking on username in post page at comment part
    * Create new route view_user_comments below delete_comment route in mywebsite/routes.py
    * $$ touch mywebsite/templates/view_user_comments.html
    * code in that view_user_comments.html
    * nested h6 tag contains comment.author.username by a tag in comment part of mywebsite/templates/post.html 
    * change color in main.css and some html files
    * browse the post page and view user comment page 
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Create view comment page for paticular user when clicking on username in post page on day 9 part 5' 
    * $$ git status
    * $$ git log
 ------------------
#### DAY 10
1. Use TimedJSONWebSignatureSerializer in terminal
    * $$ python
    * $$ from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
    * $$ s = Serializer('secret', 30)
    * $$ token = s.dumps({'user_id': 1}).decode('utf-8')
    * $$ token
    * $$ s.loads(token)
    * if call s.loads(token) after 30s it says Signature expired 
    * $$ s.loads(token)
2. Reset password using token 
    * import app and TimedJSONWebSignatureSerializer into mywebsite/models.py 
    * add get_reset_token() method to User model in mywebsite/models.py
    * add verify_reset_token() method to User model in mywebsite/models.py
    * Create RequestResetForm and ResetPasswordForm in mywebiste/forms.py in order to user enter information to reset password
    * import RequestResetForm and ResetPasswordForm into mywebsite/routes.py
    * create reset_request route in mywebsite for user use it to request reset password by enter the email that register before
    * $$ touch mywebsite/templates/reset_request.html 
    * code in that reset_request.html file to render form for guest/user enter email and submit
    * open browser and go to localhost:5000/reset_password
    * create reset_token route in mywebsite/routes.py for reset password or redirect to reset_request route
    * $$ touch mywebsite/templates/reset_token.html 
    * code that reset_token.html to to render form for guest/user enter new password and submit
    * create send_reset_email() function above reset_request route in mywebsite/routes.py
    * $$ pip install flask-mail
    * import Mail by extension flask_mail into mywebsite/__init__.py 
    * code configuration for mail and setup enviroment for save email address and email password usualy enviroment varibale located in ~/.bashrc
    * $$$ cd ~
    * $$$ nano .bashrc
    * $$$ export EMAIL_ADDRESS='my_email_address'
    * $$$ export EMAIL_PASSWORD='my_email_password'
    * save that .bashrc file
    * $$$ source .bashrc
    * create instance mail in mywebsite/__init__.py file
    * import instace maiil to mywebsite/routes.py
    * import Message from flask_mail to mywebsite/routes.py
    * add a link reset password to the mywebsite/templates/login.html
    * go to https://myaccount.google.com/lesssecureapps to change less secure apps
    * browse all routes that added in this part
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Reset password using token on day 10 part 1 and part 2' 
    * $$ git status
    * $$ git log
 ------------------
#### DAY 11
1. Blueprints for main
    * $$ mkdir mywebsite/main
    * $$ touch mywebsite/main/__init__.py
    * $$ touch mywebsite/main/forms.py
    * $$ touch mywebsite/main/routes.py
    * inside mywebsite/main/routes.py create main blueprint
    * cut home and project route in mywebsite/routes.py and paste those routes to mywebsite/main/routes.py .After that change app to main in mywebsite/main/routes.py
    * later on another day I create AdminForm inside mywebsite/main/forms.py
    * fix the importing libraries in mywebsite/main/routes.py
2. Blueprints for users
    * $$ mkdir mywebsite/users
    * $$ touch mywebsite/users/__init__.py
    * $$ touch mywebsite/users/forms.py
    * $$ touch mywebsite/users/routes.py
    * $$ touch mywebsite/users/utils.py
    * cut RegistrationForm, LoginForm, AccountForm, RequestResetForm and ResetPasswordForm in mywebsite/forms.py and paste those forms to mywebsite/users/forms.py
    * inside mywebsite/users/routes.py create users blueprint
    * cut register, login, logout, account, view_user_comments, reset_request and reset_token route in mywebsite/routes.py and paste those routes to mywebsite/users/routes.py. After that change app to users in mywebsite/users/routes.py
    * cut save_image, delete_image and send_reset_email function in mywebsite/routes and pase those function to mywebsite/users/utils.py
    * fix the importing libraries in mywebsite/users/forms.py
    * fix the importing libraries in mywebsite/users/routes.py
    * fix the importing libraries in mywebsite/users/utils.py
3. Blueprints for posts
    * $$ mkdir mywebsite/posts
    * $$ touch mywebsite/posts/__init__.py
    * $$ touch mywebsite/posts/routes.py
    * $$ touch mywebsite/posts/forms.py
    * $$ touch mywebsite/posts/utils.py
    * cut PostForm in mywebsite/forms.py and paste that form to mywebsite/posts/forms.py
    * inside mywebsite/posts/routes.py create posts blueprint
    * cut create_post, post, update_post, and delete_post route in mywebsite/routes.py and paste those routes to mywebsite/posts/routes.py. After that change app to posts in mywebsite/posts/routes.py
    * cut save_aidotpy,and save_weight function in mywebsite/routes and pase those function to mywebsite/posts/utils.py
    * fix the importing libraries in mywebsite/posts/forms.py
    * fix the importing libraries in mywebsite/posts/routes.py
    * fix the importing libraries in mywebsite/posts/utils.py
3. Blueprints for comments
    * $$ mkdir mywebsite/comments
    * $$ touch mywebsite/comments/__init__.py
    * $$ touch mywebsite/comments/forms.py
    * $$ touch mywebsite/comments/routes.py
    * cut CommentForm in mywebsite/forms.py and paste that form to mywebsite/comments/forms.py
    * inside mywebsite/posts/routes.py create posts blueprint
    * cut update_comment and delete_comment route in mywebsite/routes.py and paste those routes to mywebsite/comments/routes.py. After that change app to comments in mywebsite/comments/routes.py
    * fix the importing libraries in mywebsite/comments/forms.py
    * fix the importing libraries in mywebsite/comments/routes.py
4. Blueprints for ais
    * $$ mkdir mywebsite/ais
    * $$ touch mywebsite/ais/__init__.py
    * $$ touch mywebsite/ais/forms.py
    * $$ touch mywebsite/ais/routes.py
    * move mywebsite/ai.py to mywebsite/ais/
    * cut AIForm in mywebsite/forms.py and paste that form to mywebsite/ais/forms.py
    * inside mywebsite/ais/routes.py create ais blueprint
    * cut model route in mywebsite/routes.py and paste that route to mywebsite/ais/routes.py. After that change app to ais in mywebsite/ais/routes.py
    * fix the importing libraries in mywebsite/ais/forms.py
    * fix the importing libraries in mywebsite/ais/routes.py
    * check the importing libraries in mywebsite/ais/ai.py
5. Register main, users, posts, commments and ais blueprint to mywebsite package
    * MUST DELETE mywebsite/forms.py
    * MUST DELETE mywebsite/routes.py
    * in mywebsite/__init__.py file import users, posts, comments and ais variables which in the mywebsite/itsname/routes.py then register them by using app.register_blueprint() function in mywebsite/__init__.py
    * in visual studio code search url_for in the entire mywebsite directory by using Ctrl-Shift-F. Then change the route_name in url_for with this format "blueprint_name.route_name"
    * change the value login_manager.login_view to users.login in mywebsite/__init__.py
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Blueprint the whole website on day 11 part 1, 2, 3, 4 and 5' 
    * $$ git status
    * $$ git log
6. Organize app configuration 
    * $$ touch mywebsite/configuration.py
    * move app.config in mywebsite/__init__.py to mywebsite/configuration.py then make enviroment variables in ~/.bashrc for them
    * import Configuration class to mywebsite/__init__.py then pass all variable in Configuration to app.config
    * browse the website
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Organize app configuration on day 11 part 6' 
    * $$ git status
    * $$ git log
7. Create application factory in order to create different instances with different configurations
    * add create_app function to mywebiste/__init__.py
    * code in that creat_app function
    * since using create_app function, flask provides current_app import to add create_app function
    * replace all 'from mywebsite import app' to "from flask import current_app" in anyfile except mywebsite/__init__.py and ../run.py
    * replace all "app" to "current_app" in anyfile except mywebsite/__init__.py and ../run.py
    * replace "from mywebsite import app" to "from mywebsite import create_app" in ../run.py then set app = create_app()
    * browse the website
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Create application factory on day 11 part 7' 
    * $$ git status
    * $$ git log
 ------------------
#### DAY 12
1. Create errors blueprint
    * create package errors by creating errors directory in mywebsite then create __init__.py file under mywebsite/errors
    * touch mywebsite/errors/handlers.py
    * code blueprint errors in that handlers.py file
    * create error_403, error_404, error_405, error_500 route in mywebsite/errors/handlers.py
    * create errors/403.html, errors/404.html, errors/405.html, errors/500.html
    * register errors blueprint to the mywebsite/__init__.py
    * browse the website
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Create errors blueprint on day 12 part 1' 
    * $$ git status
    * $$ git log
 ------------------
#### DAY Improve
1. Improve sending email using thread
    * create send_async_reset_email in mywebsite/users/utils.py to 
    * create send_thread_reset_email in mywebsite/users/utils.py to send email with multiple threads
    * import send_thread_reset_email to mywebsite/users/routes.py and call send_thread_reset_email at reset_request route 
    * browse the website to the reset password page
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Improve sending email using thread on day improve part 1' 
    * $$ git status
    * $$ git log
2. Improve loading weight for any deep leanring model
    * create thread for function load_state_dict in mywebsite/ais/ai.py
    * modify code at model route in mywebsite/ais/routes.py
    * browse to model page 
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Improve loading weight for any deep leanring model on day improve part 2' 
    * $$ git status
    * $$ git log
3. Improve model page, replace nhanguyencsd@gmail.com, use flask-limiter and autoreload app
    * $$ touch mywebsite/templates/model.html
    * code that model.html
    * use limiter in mywebsite/__init__.py then the default limiteer decorator apply to all routes.I also custom limiter decorator in model route, creat_post, update post, delete_post, login, account route, reset_request route
    * browse the website
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Improve model page, replace nhanguyencsd@gmail.com and use flask-limiter and autoreload app on day improve part 3' 
    * $$ git status
    * $$ git log
    * fix the limiter in reset_request route
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'fix the limiter in reset_request route on day improve part 3' 
    * $$ git status
    * $$ git log
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'fix the limiter in reset_request route 2nd time and view_comment page on day improve part 3' 
    * $$ git status
    * $$ git log
4.  Improve delete post(all comments linked to a post get deleted when the post is deleted), add 5 attempts for login and truncate the content each post in project page 
    * $$ export FLASK_APP=run.py
    * $$ flask shell
    * $$ from mywebsite import db
    * $$ db.drop_all()
    * $$ db.create_all()
    * add cascade="all, delete-orphan"  to the comments relationship inside Post model in mywebsite/models.py
    * add attempt column to User model in in mywebsite/models.py
    * modify username, emial, password field of mywebsite/users/forms.py
    * code 5 attempts for login inside login route and reset_token route 
    in mywebiste/users/routes.py 
    * browse the website
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Improve delete post(all comments linked to a post get deleted when the post is deleted), add 5 attempts for login and truncate the content each post in project page on day improve part 4' 
    * $$ git status
    * $$ git log
5. Improve Error Page
    * recode footer in mywebsite/template/layout.html
    * recode error handling in mywebsite/errors/handlers.py
    * recode all templates in mywebsite/template/errors
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Improve Error Page on day improve part 5' 
    * $$ git status
    * $$ git log
6. Move input and output page to post page
    * move code from mywebsite/ais/routes.py to mywebsite/posts/routes.py in post route
    * move code mywebsite/templates/model.py to mywebsite/templates/post.html and modify a little bit
    * replace action="{{ url_for('ais.model', model_name=post.model_name) }}" to action="" in mywebsite/templates/post.html
    * Delete mywebsite/ais/routes.py and mywebsite/templates/models.py
    * remove anything about ais blueprint in mywebsite/__init__.py
    * replace href='https://www.google.com' to href="{{ url_for('main.project', sort_category=post.category, page=1) }}" in mywebsite/template
    * browse to post page
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Move input and output page to post page on day improve part 6' 
    * $$ git status
    * $$ git log
7. Set up 5 times to run a model for everyday and create dynamic home page
    * add run_count and run_date columns to User model in mywebsite/models.py
    * create Admin model in mywebsite/models.py
    * $$ export FLASK_APP=run.py
    * $$ flask shell
    * $$ from mywebsite import db
    * $$ db.drop_all()
    * $$ db.create_all()
    * add is_new_day function to mywebsite/posts/utils.py
    * import is_new_day function in mywebsite/posts/utils.py and handle 5 times to run a model inside mywebsite/posts/routes.py
    * Create Home model in mywebiste/models.py and HomeForm in mywebsites/main/forms.py
    * $$ export FLASK_APP=run.py
    * $$ flask shell
    * $$ from mywebsite import db
    * $$ from mywebsite.models import Home
    * $$ home = Home(greeting="I'm Nhan", position="a data learner", about_me_overview="this is place to put my about me overview", about_me="this is place to put my about me", task="this is place to put my task")
    * $$ db.session.add(home)
    * $$ db.session.commit()
    * $$ Home.query.all()
    * recode home route in mywebiste/main/routes.py
    * create new create_home, update_home , before_delete_home and delete_home routes in mywebiste/main/routes.py and add flask limiter for those routes
    * create and code in  create_home.html, update_home.html and before_delete_home.html routes in mywebiste/templates
    * modify mywebsite/templates/layout.html based on task
    * recode all routes that have footer which contain home task
    * browse to register, login, create post AI category
    * browse to post page to run AI model
    * brose to home page to create, update, and delete home
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Set up 5 times to run a model for everyday and create dynamic home page on day improve part 7' 
    * $$ git status
    * $$ git log 
8. Use Redis storage backend for flask-limited
    * overview redis in terminal
    * $$ sudo apt-get install redis-server
    * $$ redis-cli
    * $$ clear
    * $$ PING 
    * $$ ECHO 'Hello World'
    * $$ SET foo 100
    * $$ GET foo
    * $$ INCR foo
    * $$ GET foo
    * $$ DECR foo
    * $$ GET foo
    * $$ EXISTS foo
    * $$ GET foo
    * $$ DEL foo
    * $$ EXISTS foo
    * $$ GET foo
    * $$ SET student:name John
    * GET student:name
    * CONFIG GET databases
    * INFO keyspace
    * KEYS * 
    * GET student:name
    * combine redis and flasklimiter on mywebsite application
    * pip install redis
    * $$ nano ~/.bashrc
    * $$ set  REDIS_URI enviroment in ~/.bashrc
    * $$ source ~/.bashrc
    * create REDIS_URI in mywebsite/Configuration
    * set storage_uri=storage_uri=Configuration.REDIS_URI into Limiter function in mywebsite/__init__.py
    * minor step remove most all print statments
    * browser the website click 2 times on homepage and 3 times on Project link
    * $$ redis-cli
    * $$ KEYS *
    * $$ GET LIMITER/something
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Use Redis storage backend for flask-limited on day improve part 8' 
    * $$ git status
    * $$ git log 
9. Improve css, use main.js and replace me.png to me.svg
    * change all custom keyword in all files to nn
    * modify skills class in main.css
    * use jQuery handle class nn-inner-skill
    * $$ touch mywebsite/static/scripts/main.js
    * cut all code jQuery in mywebsite/templates/layout.html then paste to mywebsite/static/scripts/main.js
    * [download free icon](https://www.flaticon.com/svg/static/icons/svg/3231/3231409.svg) and rename to me.png then copy it to mywebsite/static/images/admin
    * browse all pages
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Improve css and using Jquery on day improve part 9' 
    * $$ git status
    * $$ git log 
10. Work on production database
    * oveview postgresql in terminal
    * $$ sudo -i -u postgres
    * $$  psql --help
    * $$ psql
    * $$ \du
    * $$ CREATE USER nhannguyencsd;
    * $$ \du
    * $$ DROP USER nhannguyencsd;
    * $$ \du
    * $$ CREATE ROLE nhannguyencsd WITH SUPERUSER CREATEROLE CREATEDB REPLICATION BYPASSRLS LOGIN ENCRYPTED PASSWORD 'my_secret_password';
    * $$ \l
    * $$ CREATE DATABASE production_database;
    * $$ \l
    * $$ DROP DATABASE production_database;
    * $$ \l
    * $$ CREATE DATABASE production_database;
    * $$ CREATE DATABASE development_database;
    * $$ \l
    * $$ GRANT ALL PRIVILEGES ON DATABASE production_database TO nhannguyencsd;
    * $$ GRANT ALL PRIVILEGES ON DATABASE development_database TO nhannguyencsd;
    * $$ \l
    * $$ Ctrl-D
    * add  __tablename__ in mywebsite/models.py to prevent same table name(psql default has table name user) 
    * modify Configuration class in mywebsite/configuration.py
    * create DevelopmentConfiguration and 
    ProductionConfiguration class in mywebsite/configuration.py
    * modify code in mywebsite/__init__.py based on above changes
    * $$ pip install psycopg2-binary
    * $$ export FLASK_APP=run.py
    * $$ flask shell
    * $$ from mywebsite import db
    * $$ db.drop_all()
    * $$ db.create_all()
    * $$ from mywebsite.models import Home
    * $$ home = Home(greeting="I'm Nhan", position="a data learner", about_me_overview="this is place to put my about me overview", about_me="this is place to put my about me", task="this is place to put my task")
    * $$ db.session.add(home)
    * $$ db.session.commit()
    * $$ Home.query.all()
    * browse the website
    * $$$ sudo -i -u postgres
    * $$$ psql
    * $$$ \c production_database
    * $$$ \dt
    * $$$ SELECT * FROM homes;
    * $$$ SELECT * FROM posts;
    * $$$ SELECT * FROM comments;
    * $$$ SELECT * FROM users;
    * browse the website then create admin/regular account, login, update home, create post, create comments
    * $$$ SELECT * FROM homes;
    * $$$ SELECT * FROM posts;
    * $$$ SELECT * FROM comments;
    * $$$ SELECT * FROM users;
    * $$$ show data_directory;
    * $$ git status
    * $$ git add -A
    * $$ git commit -m 'Work on production database on day improve part 10' 
    * $$ git status
    * $$ git log 
 ------------------
#### DAY 13
1. Move my_website from my Workstation to my laptop
    * copy all file my_website from my Workstation to my laptop then full boostrap directory instead bootstrap.min.css
    * delete old mywebsite/flask_env
    * $ python3 -m venv flask_env
    * $ source flask_env/bin/activate
    * $ pip list
    * $ python run.py
    * then install all dependencies from day 0 to day 13
    * setup enviroment variables like day 0 to day 12 in ~/.bashrc
    * $ source ~/.bashrc
    * $ sudo apt-get install redis-server
    * $ redis-cli
    * $ Ctrl-C
    * $$ sudo apt-get install postgresql-12
    * $$ sudo -i -u postgres
    * $$ psql
    * $$ CREATE ROLE nhannguyencsd WITH SUPERUSER CREATEROLE CREATEDB REPLICATION BYPASSRLS LOGIN ENCRYPTED PASSWORD 'my_secret_password';
    * $$ CREATE DATABASE production_database;
    * $$ CREATE DATABASE development_database;
    * $$ \l
    * $$ GRANT ALL PRIVILEGES ON DATABASE production_database TO nhannguyencsd;
    * $$ GRANT ALL PRIVILEGES ON DATABASE development_database TO nhannguyencsd;
    * $$ \l
    * $ export FLASK_APP=run.py #note that create database home for production_database and development_database by modify in mywebsite/__init__.py file
    * $ flask shell
    * $ from mywebsite import db
    * $ db.create_all()
    * $ from mywebsite.models import Home
    * $ home = Home(greeting="I'm Nhan", position="a data learner", about_me_overview="this is place to put my about me overview", about_me="this is place to put my about me", task="this is place to put my task")
    * $ db.session.add(home)
    * $ db.session.commit()
    * $ Home.query.all()
    * $ Ctrl-D
    * $ python run.py
    * browse the website, create admin/regular account, login, post, comment, logout and reset email page
    * $$ \c production_database
    * $$ SELECT * FROM users;
    * Ctrl-C
    * $$ git status
    * $$ git add -A
    * $$ git commit -m ' Move my_website from my Workstation to my laptop on day 13 part 1' 
    * $$ git status
    * $$ git log
2. Deploy on linode: create account, choose a plan, login with root password/login with limited user/login with ssh key, prevent authentication with password, install firewall, transfer my_website to the server, install dependencies , install postgres and redis-server, create database, nginx
    * for deploy/my_website on local machine fix some issues about the reponsive design, adjustment flash message, align input in reset password page, add class nn-small-text in main.css, the order of comments when edit, display none when submit the button(create new home, update this home, delete eists homes, create post,  update post, run, comment, update comment by using class nn-one-click and JQuery), instead of use variables in ~/.bashrc use varibale in /etc/config.json by creating a /etc/config.json file, and using thread when running app
    * create account and login on clound.linode.com
    * click on create -> linode -> ubuntu -> Dallas -> plan 40
        -> Nhan Nguyen -> my root password -> Backup -> Create
    * open 2 terminal: up terminal for server, bottom terminal for local machine 
    * click on Nhan Nguyen -> Networking -> copy SSH access -> pass that into terminal server(ssh root@my_ip) -> yes -> enter my root password 
    * convention: @ for server terminal, $ for local machine
    * @ apt update && apt upgrade 
    * @ hostnamectl set-hostname NhanNguyen
    * @ hostname
    * @ nano /etc/hosts
        * write ip SSH acess to that file below localhost
        * write hostname "NhanNguyen" same line with the line of IP SSH access
        * then Ctrl-X and Y
    * create limited user good for security reason
    * @ adduser nhannguyencsd 
        * enter my password
        * fill out my information
    * @ adduser nhannguyencsd sudo
    * @ exit
    * $ ssh nhannguyencsd@my_ip
        * then enter my password for nhannguyencsd user
    * @ mkdir .ssh
    * $ ssh-keygen -b 4096
        * leave all option empty except enter my passphrase
    * $ scp ~/.ssh/id_rsa.pub nhannguyencsd@my_ip:~/.ssh/authorized_keys
        * enter my password for user nhannguyencsd on the server
    * @ ls .ssh
    * @ sudo chmod 700 ~/.ssh/
    * @ sudo chmod 600 ~/.ssh/*
    * @ exit
    * $ ssh nhannguyencsd@my_ip
    * @ sudo nano /etc/ssh/sshd_config
        * set "PermitRootLogin no"
        * set "PasswordAuthentication no"
    * @ sudo systemctl restart sshd
    * @ sudo apt install ufw
    * @ sudo ufw default allow outgoing
    * @ sudo ufw default deny incoming
    * @ sudo ufw allow 
    * @ sudo ufw allow ssh
    * @ sudo ufw allow 5000
    * @ sudo ufw enable
    * @ sudo ufw status
    * $ cd Documents/apply_job/my_website/
    * $ source flask_env/bin/activate
    * $ pip freeze
    * $ pip freeze > requirements.txt
    * $ mkdir ~/Documents/apply_job/deploy
    * copy ~/Documents/apply_job/my_website to ~/Documents/apply_job/deploy then it should be ~/Documents/apply_job/deploy/my_website
    * inside ~/Documents/apply_job/deploy/my_website delete flask_env, 
    .git, __pycache__ directories, all image except default.png in static/images/user, .pt files and README.md file
    * $ cd ~
    * $ scp -r ~/Documents/apply_job/deploy/my_website nhannguyencsd@my_ip:~/
    * @ ls
    * @ sudo apt install python3-pip
    * @ sudo apt install python3-venv
    * @ python3 -m venv my_website/flask_env
    * @ cd my_website
    * @ ls
    * @ source flask_env/bin/activate
    * @ pip list
    * @ pip install -r requirements.txt
    * @ pip list
    * @ sudo apt-get install redis-server
    * @ redis-cli
    * @ Ctrl-C
    * @ sudo apt-get install postgresql-12
    * @ sudo -i -u postgres
    * @ psql
    * @ CREATE ROLE nhannguyencsd WITH SUPERUSER CREATEROLE CREATEDB REPLICATION BYPASSRLS LOGIN ENCRYPTED PASSWORD 'my_secret_password';
    * @ \du
    * @ CREATE DATABASE production_database;
    * @ CREATE DATABASE development_database;
    * @ \l
    * @ GRANT ALL PRIVILEGES ON DATABASE production_database TO nhannguyencsd;
    * @ GRANT ALL PRIVILEGES ON DATABASE development_database TO nhannguyencsd;
    * @ \l
    * @ Ctrl-D
    * @ export FLASK_APP=run.py
    * @ flask shell
    * @ from mywebsite import db
    * @ db.create_all()
    * @ from mywebsite.models import Home
    * @ home = Home(greeting="I'm Nhan", position="a data learner", about_me_overview="this is place to put my about me overview", about_me="this is place to put my about me", task="this is place to put my task")
    * @ db.session.add(home)
    * @ db.session.commit()
    * @ Home.query.all()
    * @ Ctrl-D
    * @ python run.py
    * open browser enter my_ip_address
    * before install nginx(runs on port 80) and guniconr(gunicorn runs on port 8000), need nginx server the stactic files and gunicon server other files
    * @ sudo apt install nginx
    * @ pip install gunicorn
    * update configure file for nginx
        * @ sudo rm  /etc/nginx/sites-enabled/default
        * @ sudo nano /etc/nginx/sites-enabled/mywebsite
            * set server: listen, server_name, location
            * set forwart all of the other traffic to gunicorn by proxy_pass to localhost port 8000(gunicorn), include and proxy_redirect
    * @ sudo ufw allow http/tcp #for allow http/tcp means allow for nginx on port 80
    * @ sudo ufw delete allow 5000  # no longer need port 5000 which is a default flask port 
    * @ sudo ufw enable # to enable rules that add or delete allow port
    * @ sudo systemctl restart nginx # restart nginx to update from its configuaration in the  above
    * browse the website with my_ip, my_ip/static/something_want_to_see to see how nginx work but gunicorn doesn't work yet
    * @ gunicorn -w 9 run:app # 9 because 2*4 + 1 and 4 because having 4 cpus on the server ,run because run.py, app because app is the application in run.py
    * browse the website with my_ip, it will be work, now both nginx and gunicorn are worked
    * @ Ctrl-C
    * browse the website with my_ip , it doesn't because Ctrl-C kills the gunicorn
    * setup gunicorn auto start and auto restart if it crashed by using supervisor 
    * @ sudo apt install supervisor
    * set up configuration in supervisor
        * @ sudo nano /etc/supervisor/conf.d/mywebsite.conf
            * set program, directory, command, user
            * set autostart, autorestart, stopasgroup, killasgroup, stderr_logfile
            * @ sudo mkdir -p /var/log/mywebsite
            * @ sudo touch /var/log/mywebsite/mywebsite.err.log
        * @ sudo supervisorctl reload
        * try enviroment varibale in different way
            * @ sudo touch /etc/config.json
            * @ sudo nano  /etc/config.json 
                * set all variables like enviroment variables like day 1-13
            * modify my_webisite/mywebsite/configuration.py based on the server /etc/config.json
        * @ sudo supervisorctl reload
        * browse the website
    * @ sudo nano /etc/nginx/nginx.conf # to fix the default size nginx 2M when upload the file
        * inside http object set client_max_body_size 50M;
        * @ sudo systemctl restart nginx to restart nginx
    * browse all pages
    * $ git status
    * $ git add -A
    * $ git commit -m 'Guide for deploying website on day 13 part 2'
    * $ git status
    * $ git log
 ------------------
#### DAY 14
* [DNS Manager](https://www.linode.com/docs/platform/manager/dns-manager/)
* register domain name on namecheap
* set domain name  on linode
* on the namecheap/domain list at nhancs.com click customDNS for addinglinode name server
* on the linode/DNS manager add a domain zone and some basic DNS records 
* on linode add A/AAAA Record 
    * set hostname: blank
    * set ip address: my_ip
    * TTL : Default
* on linode add another A/AAAA Record 
    * set hostname: www
    * set ip address: my_ip
    * TTL : Default
* set reverse_DNS(turn ip address to domain name) under linodes/NhanNguyen/Networking/IPv4/Edit RDNS: www.nhancs.com
* browse the website with domain name www.nhancs.com and nhancs.com
* browse the website with my_ip address
* $ git status
* $ git add -A
* $ git commit -m 'Guide for setup domain name on day 14'
* $ git status
* $ git log
 ------------------
#### DAY 15
* go to https://certbot.eff.org/ then set running: Nginx and on: Ubuntu20.04 then follow a instruction
* ssh myusername@my_ip
* @ sudo apt update
* @ sudo snap install core; sudo snap refresh core
* @ sudo apt-get remove certbot
* @ sudo snap install --classic certbot
* add wwww.nhancs.com and nhancs.com  to server_name in nginx-configuration
    * @ sudo nano /etc/nginx/sites-enabled/mywebsite
    * add 2 domain names above to that file
* @ sudo certbot --nginx
* @ cat /etc/nginx/sites-enabled/mywebsite
* @ sudo nginx -t
* @ sudo ufw allow https #allow https
* @ sudo systemctl restart nginx
* @ sudo certbot renew --dry-run
* @ sudo crontab -e
    * option 1
* enter wwww.nhancs.com and nhancs.com in the url bar of a browse
* $ git status
* $ git add -A
* $ git commit -m 'Guide for getting https certificate on day 15'
* $ git status
* $ git log

    


    
    














    




