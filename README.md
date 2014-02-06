SimpleDjangoBlog
================

Simple blog engine using django


Dependencies
------------
  * **django-admin-bootstrapped**
    pip install django-admin-bootstrapped
  * **psycopg2**
    pip install psycopg2


Usage
-----
Install the database (configure the connection in blog_project/settings.py)
    python manage.py syncdb

Run server:
    python manage.py runserver
    
The client-side
    http://localhost:8000/blog

The admin-side
    http://localhost:8000/admin
