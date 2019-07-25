## About the project
This app is a pro bono project to help streetworkers, who help homeless people, work efficiently and share
information among themselves.

Main function of the app will be an interactive map with location points and information about the places gathered
from forms and displayed back to the users.

Currently I work on it as the only developer, doing also analysis of client needs.

## Instalation
```
pip install -r requirements.txt
install postgres and python-dotenv with sudo
```

Than export STREETWORK_PASS and ENV_ROLE.

## How to start the app

```
python manage.py runserver
```  

Database:
install postgis, create database with postgres and add extention postgis

## Current project state:
Admin can add a place location from a map
On a homepage there is a map with location points from db

## Next steps
Form to add new points from the homepage
Add a model and a form to gather information about the place
Add functionality to display information about the place when marker on the map is clicked
