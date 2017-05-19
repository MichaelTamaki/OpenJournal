# OpenJournal  
This is an open source project to create a journal web app using Django. User accounts are tied to their Facebook profiles and can only view journal entries that are their's or public entires by other people. Started at LAHacks 3/31/17. Originally deployed to AWS Elastic Beanstalk, but later moved to Heroku.

## Setting up the project locally  
- Set up a virtualenv! `virtualenv env` in the root folder (same level as `.gitignore`)  
- Activate the virtualenv! `source env/bin/activate`  
- Install dependencies! `pip install -r requirements.txt`
- To be able to use Python Social Auth, set up an arbitrary host for `127.0.0.1`  
  - Open `/etc/hosts/`  
  - Add `127.0.0.1 www.openjournal.development.com`  
  - When opening your browser, navigate to alias
- The secret keys in `settings.py` are avaliable in a secret file `secret.py`, ask Michael for it!

## Set up Postgresql  
- `createdb open_journal`  
- `psql open_journal`  
- Commands to set up persmissions
  - `CREATE DATABASE open_journal;`  
  - `CREATE USER name WITH PASSWORD '';`  
  - `ALTER ROLE name SET client_encoding TO 'utf8';`
  - `ALTER ROLE name SET default_transaction_isolation TO 'read committed';`
  - `ALTER ROLE name SET timezone TO 'UTC';`
  - `GRANT ALL PRIVILEGES ON DATABASE open_journal TO name;`  
  - Exit: `\q`  
- Username and password are defined in `DATABASES` in `settings.py` (replace with name)  

## Running server  
- Set `DEBUG = True`  
- `python manage.py runserver`  
- Navigate to `www.openjournal.development.com:8000`  
- For now, Facebook authentification only works on the live website... Sorry!  

## Running tests  
- If getting error `Got an error creating the test database: permission denied to create database`, in `psql`: `ALTER USER name CREATEDB;`
- `./manage.py test`  

## Deployment to Heroku
- Add the secret key to the commit, but make sure not to push to Github, only Heroku! (until I find a better way to do it)  
- `git add -f secret.py`  
- `git commit -m "secret!"`  
- `git push heroku master`  
- `git reset HEAD~1`  
- To play with the database: `heroku run python manage.py shell`  

## Resources used  
- [Full Stack Python](https://www.fullstackpython.com/)  

## Technologies  
- Django  
- Postgresql  
- Python Social Auth  
- Heroku
