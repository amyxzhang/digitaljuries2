## Development

- `cd digitaljuries2`
- Activate `virtualenv djvm`
- `source djvm/bin/activate`

## Pre-requirements
`pip install virtualenv`
`pip install Django==1.9.1`
`pip install django-annoying==0.8.5`
`pip install django-tracking2==0.4.0`
`python manage.py migrate`

## Run experiment

`python manage.py runserver`
Django server will run at http://127.0.0.1:8000/