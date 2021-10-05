# Setup

- Clone project: `git clone url`
- Create virtual env (install pipenv if not installed): `cd tesis-tati && pipenv install`
- Spawn pipenv shell: `pipenv shell`
- Migrate DB: `cd tesis_tati && python manage.py migrate`
- Create super user for admin site: `python manage.py createsuperuser`
- Collect static assets: `python manage.py collectstatic`
- Install certbot and install ssl certificates for the site
- Run gunicorn server: `gunicorn --certfile=/ssl/fullchain1.pem --keyfile=/ssl/privkey1.pem --ssl-version=3 --workers=2 tesis_tati.wsgi -b 0.0.0.0:8001"`
