# Flask api backend and frontend vue3 with pinia
Integration with Flask-Cors,Flask-SQLalchemy, wtforms in backend and vue3 witn pinia tailwind 

### Before install requirements
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|──────app/
| |────controllers/
| | |────auth_controller.py
| | |────dashboard_controller.py
| | |────default_controller.py
| | |────permission_controller.py
| | |────role_controller.py
| | |────user_controller.py
| |────forms/
| | |────permission_form.py
| | |────role_form.py
| | |────user_form.py
| |────frontend/
| |────models/
| | |────permission_model.py
| | |────permission_roles_model.py
| | |────role_model.py
| | |────user_model.py
| | |────user_role_model.py
| |────routes/
| | |────user_routes.py
| | |────base_routes.py
| | |────dashboard_routes.py
| | |────role_routes.py
| | |────user_routes.py
| |────seeders/
| | |────permission_seeder.py
| | |────role_seeder.py
| | |────user_seeder.py
| |────commands.py
| |────config.py
| |────extensions.py
|──────seeds/
| |────master_seeder.py
|──────run.py
```

## Getting Started
### Run migration config
```
$ flask db init
```
```
$ flask db migrate
```
```
$ flask db upgrade
```
### Prepare Frontend (/app/frontend/)
```
$ npm install
```
```
$ npm run build
```
For devs can run:
```
$ npm run dev
```

### Run api path (/)
```
$ python run.py
```

## Changelog
- Version 1.0 : basic Api Flask for with vue3 as frontend
