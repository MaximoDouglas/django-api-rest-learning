# django-api-rest-learning
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
