# florens_api

Esta api es diseñada para la gestión de labores de enfermería con el fin de facilitar la ardua labor de este personal y que la misma pueda organizarse de manera 
mas optima, el enfoque de la solución va dirigido a ser ejecutado en dispositivos móviles donde las enfermeras pueden ver de manera mas sencilla toda información y
de manera precisa.

This api is designed for the management of nursing tasks in order to facilitate the hard work of this staff and that it can be organized in a way
More optimally, the focus of the solution is aimed at being executed on mobile devices where nurses can more easily see all the information and
in a precise way.

### Technologies Used

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)    



Requirements
------------

-  Python 3.11.0
-  Django 4.1.5
-  Django REST Framework 3.14.0
-  psycopg2 2.9.5

## Getting Started


To run the application, follow these steps:

**Clone the repository**
```bash
 https://github.com/iranmederos/florens_api.git
```

**Install the required dependencies by running**
```bash
 pip install -r requirements.txt
```
**Create a PostgreSQL database and configure the settings in settings.py with environment variables**
```bash
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}
```
**Run the migrations by running** 
 ```bash
 python manage.py migrate
```
**Start the development server by running**
 ```bash
python manage.py runserver
```
   

API Endpoints

    /api/doc/: Endpoint with all endpoints in swagger
    /api/redoc/: Other view  with all endpoints in swagger
