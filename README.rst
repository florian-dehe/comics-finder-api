Comics Finder API
=================

Comics Finder REST API build with the Django REST Framework

Install
-------
``poetry install``

Run Dev
-------
``poetry run ./comics_finder_api/manage.py runserver``

Run Production
-----
``cd comics_finder_api``
``poetry add gunicorn``
``poetry run gunicorn --env DJANGO_SETTINGS_MODULE=comics_finder_api.settings_prod ./comics_finder_api/wsgi.py``
