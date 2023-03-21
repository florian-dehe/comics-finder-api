# Comics Finder API

Comics Finder REST API build with the Django REST Framework

## Install locally

### Install

```bash
poetry install
```

### Run Dev

```bash
poetry run ./comics_finder_api/manage.py migrate
poetry run ./comics_finder_api/manage.py runserver
```

### Run Production

```bash
cd comics_finder_api
poetry add gunicorn
poetry run ./manage.py migrate --settings=comics_finder_api.settings.prod
poetry run gunicorn --env DJANGO_SETTINGS_MODULE=comics_finder_api.settings.prod comics_finder_api.wsgi
```

## Docker image

```bash
docker build . -t <img-name>
```

## Environment Variables

If you run it locally, put these variables into `<root>/comics_finder_api/.env`

```conf
DEBUG=off
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=svelte

# HTTPS
CSRF_COOKIE_SECURE=on
SESSION_COOKIE_SECURE=on
SECURE_SSL_REDIRECT=on
SECURE_HSTS_SECONDS=on
SECURE_HSTS_INCLUDE_SUBDOMAINS=on
SECURE_HSTS_PRELOAD=on
```


