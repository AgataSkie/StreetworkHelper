## About the project
This app is a pro bono project to help streetworkers, who help homeless people, work efficiently and share
information among themselves.

Main function of the app will be an interactive map with location points and information about the places gathered
from forms and displayed back to the users.

Currently I work on it as the only developer, doing also analysis of client needs.

## Instalation
Python 3.6 and postgres are required
```
pip install -r requirements.txt
```

Than export STREETWORK_PASS and ENV_ROLE.

## How to start the app

```
python manage.py runserver
```  
go to 127.0.0.1:8000/places to check if the app has started.

Then run:
```
python manage.py makemigrations
python manage.py migrate
```
You can then crate superuser with:
```
python manage.py createsuperuser
```
an access 127.0.0.1:8000/admin to add/change places
and homepage 127.0.0.1:8000/places to see added points on a map.

## Current project state:
- A place location can be added from django-admin
- Hhomepage shows a map with location points from db

## Next steps
- Form to add new points from the homepage
- Add a model and a form to gather information about the place
- Add functionality to display information about the place when marker on the map is clicked
- Users and permission levels
