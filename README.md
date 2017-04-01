# OpenJournal
This is an open source project to create a journal web app using Django. Started at LAHacks 3/31/17 with an emphasis on test-driven development.

## Setting up the project locally
- Set up a virtualenv! `virtualenv env` in the root folder (same level as `.gitignore`)  
- Activate the virtualenv! `source env/bin/activate`  
- Install dependencies! `pip install -r requirements.txt`

## Set up Postgresql
- `createdb open_journal`  
- `psql open_journal`  
- [Commands to set up permissions](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
- Username and password are defined in `DATABASES` in `settings.py`

## Running server
- `python manage.py runserver`

## Running tests
- If getting error `Got an error creating the test database: permission denied to create database`, in `psql`: `ALTER USER name CREATEDB;`  
- Run server in a separate Terminal tab  
- `./manage.py test`  
- [Selenium Webdriver](http://www.seleniumhq.org/projects/webdriver/) is used to open up a browser (currently Google Chrome) and test the website's interactions... Please download the [driver](http://www.seleniumhq.org/download/) for Google Chrome

## Resources used
- [Full Stack Python](https://www.fullstackpython.com/)  
- [Test Driven Development with Python](http://www.obeythetestinggoat.com/)  
- [Django views automated testing with selenium](https://medium.com/@unary/django-views-automated-testing-with-selenium-d9df95bdc926)
