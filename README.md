# flasktaskr
Flask Task manager from RealPython

Part 7 implented, ready to deploy



Deploying an app to Heroku is ridiculously easy:
1. Sign up for Heroku.
2. Log in and download the Heroku Toolbelt (cli).
3. Once installed, open your terminal and run the following command: heroku login .
You'll need to enter your email and password you used when you signed up for
Heroku.
4. Navigate to your project and activate the virtual environment.
5. Install gunicorn: pip install gunicorn .
6. Heroku recognizes the dependencies needed through a requirements.txt file. Make
sure to update you file: pip freeze > requirements.txt .
7. Create a Procfile. Open up a text editor and save the following text in it: web: python
run.py . Then save the file in your application's root or main directory as Procfile (no
extension, capital 'P'). The word "web" indicates to Heroku that the application will be attached
to HTTP once deployed to Heroku.
On your local machine, the application runs on port 5000 by default. On Heroku, the
application must run on a random port specified by Heroku. We will identify this port
number by reading the environment variable 'PORT' and passing it to app.run :



# run.py
import os
from project import app
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)


Set debug to False within the config file. Why? Again, debug mode provides a handy
debugger for when errors occur, which is great during development, but you never want
end users to see this. It's a security vulnerability, as it is possible to execute commands
through the debugger.


Deploy
When you PUSH to Heroku, you have to update your local Git repository. Commit your
updated code.

Create your app on Heroku:
$ heroku create

Deploy your code to Heroku:
$ git push heroku master

Add a PostgreSQL database:
$ heroku addons:create heroku-postgresql:hobby-dev

Check to make sure your app is running:
$ heroku ps

View the app in your browser:
$ heroku open

If you see errors, open the Heroku log to view all errors and output:
$ heroku logs

