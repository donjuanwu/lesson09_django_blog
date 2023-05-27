### Django Commands
1. Install Django 
- `pip install Django`
2. Create a startproject
- `django-admin startproject mysite`
3. run Django server
- `python manage.py runserver`
4. run test on blogging app with verbosity
- `python manage.py -v 1 test blogging`
5. migrate changes to database for app blogging
- `python manage.py makemigrations blogging`
6. apply changes to database
- `python manage.py migrate`
7. Create superuser
- `python manage.py createsuperuser`
   username: doncd
   doncdang@hotmai.com
   pw: leyla2004
8. Create an app calling polling
- `python manage.py startapp polling`
9. Start a Django shell
- `python manage.py shell`
10. Run a test
- `python manage.py test blogging`