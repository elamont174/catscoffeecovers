# Deployment

Site is deployed with [Heroku](https://www.heroku.com/) which is a cloud platform that lets developers create, deploy, monitor and manage apps.
The deployed site can be found [here](https://catscoffeecovers-448595c73efd.herokuapp.com/).
These steps assume that you have a Heroku account and are logged in. 

## Back-end deployment

**Creating an app**
1. Go to the Dashboard.
2. Click 'New' > 'Create new app'.
3. Choose a unique app name, choose the closest region and press 'Create app'.
4. Click on 'Settings' and then 'Reveal Config Vars'.
5. Add a key of 'DATABASE_URL' - the value will be the URL you were emailed when creating your database.
6. Return to your IDE (in this case, Gitpod was used).
7. Install dj_database_url and psycopg2 by typing the following into the terminal:
- pip3 install dj_database_url==0.5.0 psycopg2
8. In the 'settings.py' file, type "import dj_database_url" underneath "import for os" at the top
9. Change the 'DATABASES' section of your settings.py to the following:
-  if 'DEV' in os.environ:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
 else:
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
     print(connected)
- This will ensure that when you have an environment variable for DEV in your environment the code will connect to the sqlite database here in your IDE. Otherwise it will connect to your external database, provided the DATABASE_URL environment variable exist. 
10. Create an 'env.py' file with:
- import os
- os.environ['CLOUDINARY_URL'] = '(your Cloudinary URL here)'
- os.environ.setdefault("SECRET_KEY", "(a secret Secret Key)")
- os.environ['DEV'] = '1'
- os.environ['DATABASE_URL'] = "(your PostgreSQL URL here)"
11. Still in 'env.py', temporarily comment out the DEV environment variable to connect to the external database. 
12. Put the following into the terminal: python3 manage.py makemigrations --dry-run
13. If you get the "connected" message then your external database has connected. Remove the "print(connected)" statement from the DATABASES section.
14. Migrate the database models to your new database by typing thge following into your terminal:
- python3 manage.py migrate
15. Create a superuser for your new database by typing the following into your terminal:
- python3 manage.py createsuperuser
16. Install gunicorn and update your requirements in the terminal:
- pip3 install gunicorn django-cors-headers
- pip freeze --local > requirements.txt
17. Create a file in the root directory called 'Procfile' (no file extension).
18. Add the following to your Procfile and save it:
- release: python manage.py makemigrations && python manage.py migrate
- web: gunicorn your_project_name.wsgi
19. In settings.py update ALLOWED_HOSTS to include:
- ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']
20. In settings.py update INSTALLED_APPS to include:
- INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',
    ...
 ]
21. In settings.py update MIDDLEWARE to include:
- MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
     ...
 ]
22. Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:
- if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN'), 
     ]
 else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",

CORS_ALLOW_CREDENTIALS = True
23. In 'settings.py', set the JWT_AUTH_SAMESITE attribute to 'None': 
 JWT_AUTH_COOKIE = 'my-app-auth'
 JWT_AUTH_REFRESH_COOKE = 'my-refresh-token'
 JWT_AUTH_SAMESITE = 'None'
- Without this the cookies would be blocked
24. In 'settings.py', change the value of the SECRET_KEY:
- SECRET_KEY = os.getenv('SECRET_KEY')
25. In 'env.py', set a new value for the SECRET_KEY. 
*Use a completely new one for security reasons - not the one originally in 'env.py' or that has been in your git commits*
26. In 'settings.py', change the value of DEBUG:
- DEBUG = 'DEV' in os.environ
27. In 'env.py' comment back in the DEV variable. 
28. Update your requirements in the terminal:
- pip freeze --local > requirements.txt
29. Add, commit and push your code to GitHub.


**Deploying**
1. Go to the Heroku app Dashboard.
2. Click the 'Settings' tab.
3. Click 'Reveal Config Vars' and add these Config Vars:
- (KEY)CLOUDINARY_URL: (VALUE) Copy the Cloudinary URL from your env.py file without quotation marks.
- (KEY)SECRET_KEY: (VALUE) Make up a completely new Secret Key that is NOT the same as the one in settings or env - there are many online Secret Key generators you can search for. 
- (KEY)DISABLE_COLLECTSTATIC: (VALUE)1
4. Click the 'Deploy' tab.
5. In the Deployment method section, click "Connect to GitHub".
6. Search for the repo you want to connect and click 'Connect'.
7. Scroll down and click "Deploy Branch" in the Manual deploy section.
8. Your app has been deployed! You can find it in "Open app".

## Linking to Front-end

1. In "settings.py", in the ALLOWED_HOSTS list, copy your ‘... .herokuapp.com’ string.
2. Go to Heroku and click “Settings”.
3. Click “Reveal Config Vars”
4. Add the new key of ALLOWED_HOST with the value for your deployed Heroku application URL that we copied from settings.py
Back in settings.py, replace your ALLOWED HOSTS list '... .herokuapp.com' string we just copied with the ALLOWED_HOST environment variable.
ALLOWED_HOSTS = [
   os.environ.get('ALLOWED_HOST'),
   'localhost',
]

**Cloning a repository**
1. On GitHub.com, navigate to the repository you want to clone.
2. Click the "Code" button (found above the list of files).
3. Copy the URL for the repository.
4. Open Git Bash or your chosen terminal.
5. Navigate to the directory where you want to clone the repository.
6. Type: git clone "URL OF REPOSITORY YOU WANT TO CLONE"
7. Press Enter to create your local clone.

**Forking a repository**
1. 'Forking' the GitHub repository means creating a copy which can be viewed/changed without changing the original.
2. To fork a GitHub repository:
3. Login to GitHub and navigate to the repository you want to fork.
4. Click the "Fork" button (found above the Settings button).
5. You will now have a copy of the original repository in your GitHub account.

*Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Run the server: python3 manage.py runserver
- Stop the app once it's loaded: CTRL+C or ⌘+C
- Make any necessary migrations: python3 manage.py makemigrations
- Migrate the data to the database: python3 manage.py migrate
- Create a superuser: python3 manage.py createsuperuser