## Check and upgrade pip version
```
pip --version
pip install --upgrade pip
```
## Project setup
```
django-admin.py startproject api .
django-admin.py startapp sportsapi
```
## Check and install virtual environment
```
pip install pipenv
```
## Install dependencies from pipfile
```
pipenv install
```
## Set variables
```
edit .env\Scripts\activate script:
set database.engine=
set database.dbname=
set database.host=
set database.user=
set database.password=
set security.key=
```
## Activate virtual environment
```
pipenv shell
```

## Installation of MySQL Client 32-bits
```
pip install .\whl\mysql\mysqlclient-1.4.6-cp38-cp38-win32.whl
```
