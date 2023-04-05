# florens_api

Esta api es diseñada para la gestión de labores de enfermería con el fin de facilitar la ardua labor de este personal y que la misma pueda organizarse de manera 
mas optima, el enfoque de la solución va dirigido a ser ejecutado en dispositivos móviles donde las enfermeras pueden ver de manera mas sencilla toda información y
de manera precisa.

This api is designed for the management of nursing tasks in order to facilitate the hard work of this staff and that it can be organized in a way
More optimally, the focus of the solution is aimed at being executed on mobile devices where nurses can more easily see all the information and
in a precise way.

Technologies Used
Django DjangoREST Postgres AWS

Requirements
Python 3.11.0
Django 4.1.5
Django REST Framework 3.14.0
psycopg2 2.9.5
Getting Started
To run the application, follow these steps:

Clone the repository

  git clone https://github.com/greghades/florens_backend.git
Install the required dependencies by running

 pip install -r requirements.txt
Create a PostgreSQL database and configure the settings in settings.py with environment variables

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
Run the migrations by running

python manage.py migrate
Start the development server by running

python manage.py runserver
API Endpoints

/api/doc/: Endpoint with all endpoints in swagger
/api/redoc/: Other view  with all endpoints in swagger
Contributing

Contributions are welcome! Please open an issue or pull request for any changes or bug fixes. License

This project is licensed under the MIT License - see the LICENSE file for details.
