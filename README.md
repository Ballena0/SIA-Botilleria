# SIA-Botilleria
Sistema de información administrativo para una botilleria

## Install 
After cloning

Create a virtual enviroment (virtualenv/pipenv)

Install packages
```pip install -r requirements.txt ```

## Generating the model 
```
python3 manage.py makemigrations
python3 manage.py migrate
```
#### Create user
``` 
python3 manage.py createsuperuser
``` 

#### Run
``` python3 manage.py runserver```
