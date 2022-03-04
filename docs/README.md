# Moringa Assessment CRUD Application

## Table of Contents

- [Background](#background)
- [Minimum Requirements](#minimum-requirements)
- [Quickstart](#quickstart)
- [Database SetUp](#database-setup)
- [Database Migration](#database-migration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Background
This application is a CRUD (Create Read Update Delete) application that utilizes the Django's MVT (Models View Templates) architecture. In the application I used the Class-Based-Views (CBV) due to the enhanced flexibility brought about by them as compared to functional views. Using CBV should be applied by extra caution as it does not apply to most scenarios.

## Minimum Requirements
This project supports Ubuntu Linux 20.04 and its previous stable releases and Mac OS. It not tested for Windows OS.

- [Python3](https://www.python.org/downloads/)
- [Django 4.0.3](https://www.djangoproject.com/)
- [PostgreSQL 14.2+](http://www.postgresql.org/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com/downloads)

## Quickstart
```bash
$ git clone https://github.com/OkothPius/MoringaAssessment.git
$ cd MoringaAssessment
$ sudo apt install python3-pip python3-django
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Database SetUp
```bash
$ sudo su - postgres
$ psql
CREATE DATABASE moringa;
CREATE USER moringa_user WITH PASSWORD <your_password>;
ALTER ROLE moringa_user SET client_encoding TO 'utf8';
ALTER ROLE moringa_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE moringa_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE moringa TO moringa_user;
```

## Database Migration
```bash
$ python3 manage.py migrate
$ python3 manage.py makemigrations
$ python3 manage.py sqlmigrate 0002
$ python3 manage.py runserver
```

## Deployment
We'll deploy our application to Heroku. Heroku is a cloud hosting platform that uses Amazon Web Services (AWS) infrastructure with rapid scaling capabilities, offering flexible deployment services for all kinds of applications. Its ease of use makes it particularly suitable for fast development cycles.

```bash
$ git init
$ heroku login
$ heroku create <your_app_name>
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set SECRET_KEY=<your_secret_key>
$ heroku config:set DATABASE_NAME=moringa
$ heroku config:set DATABASE_USER=moringa_user
$ heroku config:set DEBUG_VALUE=True
$ heroku run python manage.py migrate
$ heroku open #the app should be served in your browser
```

### Contributing
Want to improve the template? Fork the repo, add your changes and send a pull request.

## License

[MIT](LICENSE) © Okoth Pius
