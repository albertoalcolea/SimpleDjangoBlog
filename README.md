SimpleDjangoBlog
================

Simple blog engine using django


Dependencies
------------
 * **django-admin-bootstrapped**
 * **psycopg2**

I suggest using [virtualenv](https://pypi.python.org/pypi/virtualenv) and [pip](https://pypi.python.org/pypi/pip)

    pip install django-admin-bootstrapped

    pip install psycopg2


Usage
-----
Install the database (configure the connection in blog_project/settings.py)

    python manage.py syncdb

Run the development server:

    python manage.py runserver
    
Client-side

    http://localhost:8000/blog

Admin-side

    http://localhost:8000/admin