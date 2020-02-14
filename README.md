## Check and upgrade pip version
```
pip --version
pip install --upgrade pip
```
## Check and install virtualenv
```
pip install --user virtualenv
```
## Create virtual environment
```
virtualenv .env
```
## Set virtual environment variables
```
edit .env\Scripts\activate script:
set database.connectionstring=
```
## Activate virtual environment and install requirements
```
.env\Scripts\activate
pip install -r requirements.txt
```
## Project setup
```
django-admin.py startproject api .
django-admin.py startapp sportsapi
```