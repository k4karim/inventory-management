# inventory-management
# Django Inventory Management webapp

# to run this web app on your local machine follow these steps

Create and activate virtual environment

pip install required packages/library

Download code zip file from github repo page and unzip it.

Go to server directory and run:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Your web app is live now on http://127.0.0.1:8000/

# to deploy it on heroku

1. Login to heroku

2. Create new webapp New > Create new app

3. cd to project directory (in cmd)

4. git init

5. heroku git:remote -a "heroku appname"
  
6. git add .
  
7. git commit -am "make it better"
  
8. git push heroku master
  
9. heroku run python manage.py migrate
  
10. Done

# dont worry about database settings. "django-heroku" package does all the magic
  
