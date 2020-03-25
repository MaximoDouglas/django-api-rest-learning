# Django API REST sample projects
### Environment setup and project running
1. Enter ```./<project-name>``` folder;
2. Create a virtual environment with ```python3 -m venv <you-env-name>```;
3. Start the created virtual env with ```. <you-env-name>/bin/activate```;
4. Install django with ```pip install django```;
5. Install django rest framework with ```pip install djangorestframework```;
6. Create administration user with ```python manage.py createsuperuser --username=<yout-user-name> --email=<your-email>```. You will be asked to create a password for this user;
7. Make migrations with ```python manage.py makemigrations```;
8. Migrate with ```python manage.py migrate```;
9. Run the application with ```python manage.py runserver```;

## Projects
### pontos_turisticos
It is a project that creates an API RESTful for tourist attractions, with comments, ratings, address, etc. The objective of this project is to apply basics and intermediate concepts on [Django Rest Framework](https://www.django-rest-framework.org/). The architecture of this application can be generalized for pretty much any other small CRUD-like application and it is a good option to be used as example project.

# Deploy to Heroku
Minimal configuration to host a Django project at Heroku

## Create the project directory
* mkdir directory_name
* cd directory_name

## Create and activate your virtuanenv
* virtualenv -p python3 .vEnv
* . .vEnv/bin/activate

## Installing django
* pip install django

## Create the django project
* django-admin startproject myproject

## Creating the Git repository
* git init 
* Create a file called `.gitignore` with the following content:
```
# See the name for you IDE
.idea
# If you are using sqlite3
*.sqlite3
# Name of your virtuan env
.vEnv
*pyc
```
* git add .
* git commit -m 'First commit'

## Hidding instance configuration
* pip install python-decouple
* create an .env file at the root path and insert the following variables
- SECRET_KEY=Your$eCretKeyHere (Get this secrety key from the settings.py)
- DEBUG=True

### Settings.py
* from decouple import config
* SECRET_KEY = config('SECRET_KEY')
* DEBUG = config('DEBUG', default=False, cast=bool)

## Configuring the Data Base
* pip install dj-database-url

### Settings.py
* from dj_database_url import parse as dburl

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


## Static files 
pip install dj-static

### wsgi
* from dj_static import Cling
* application = Cling(get_wsgi_application())

### Settings.py
* STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

## Create a requirements-dev.txt
pip freeze > requirements-dev.txt

## Create a file requirements.txt file and include reference to previows file and add two more requirements
* -r requirements-dev.txt
* gunicorn
* psycopg2

## Create a file Procfile and add the following code
* web: gunicorn website.wsgi --log-file -

## Create a file runtime.txt and add the following core
* python-3.6.0

## Creating the app at Heroku
You should install heroku CLI tools in your computer previously ( See http://bit.ly/2jCgJYW ) 
* heroku apps:create app-name
Remember to grab the address of the app in this point

## Setting the allowed hosts
* include your address at the ALLOWED_HOSTS directives in settings.py - Just the domain, make sure that you will take the protocol and slashes from the string

## Heroku install config plugin
* heroku plugins:install heroku-config

### Sending configs from .env to Heroku ( You have to be inside tha folther where .env files is)
* heroku plugins:install heroku-config
* heroku config:push -a

### To show heroku configs do
* heroku config 

## Publishing the app
* git add .
* git commit -m 'Configuring the app'
* git push heroku master --force

## Creating the data base
* heroku run python3 manage.py migrate

## Creating the Django admin user
* heroku run python3 manage.py createsuperuser

## EXTRAS
### You may need to disable the collectstatic
* heroku config:set DISABLE_COLLECTSTATIC=1

### Changing a specific configuration
* heroku config:set DEBUG=True
