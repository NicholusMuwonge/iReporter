[![Build Status](https://travis-ci.com/NicholusMuwonge/iReporter.svg?branch=ft-challenge-three)](https://travis-ci.com/NicholusMuwonge/iReporter)
[![Coverage Status](https://coveralls.io/repos/github/NicholusMuwonge/iReporter/badge.svg?branch=ft-challenge-three&service)](https://coveralls.io/github/NicholusMuwonge/iReporter?branch=ft-challenge-three)

[![Maintainability](https://api.codeclimate.com/v1/badges/95c6a67ee8716ddebf6b/maintainability)](https://codeclimate.com/github/NicholusMuwonge/iReporter/maintainability)




### About
<strong>IREPORTER<strong> is an application thats is used by someone to raise an issue to the authorities about corruption,and any other grievance to the authority in their communities

### Features
1. Create a redflag record (title, record_type,record geolocation)
2. Edit a specific redflag record's geolocation.
3. Get a specific redflag record
4. Delete a redflag record
5. Get all redflag records for that specific user
6. create intervention records 
7. get all interventions
8. get one intervention record
9. update an intervention record
10. admin can change status of both record types
11. to get a specific user's records
12. signup
13. to login a particular user



### Links

#### Gh-pages:  
https://nicholusmuwonge.github.io/iReporter/UI/index

This link points to the user interface template is hosted on gh-pages.

#### Heroku:    
https://appireporter.herokuapp.com/ - challenge-2
https://databasetests.herokuapp.com/ -challenge-3

This link points to the api that is hosted on Heroku.

### Getting Started 
The following will get you started
#### Prerequisites
You will need to install the following

```bash
- git : To clone, update and make commits to the repository
- python3: The base language used to develop the api
- pip3: The latest python package used to install project requirements
```
#### Installation
The ft-challenge-one folder houses the user interface. To access the user interface, open the index.html.
The ft-challenge-two folder contains the system backend services.
- To install the requirements, run:
- [Python](https://www.python.org/) A general purpose programming language
- [Pip](https://pypi.org/project/pip/) A tool for installing python packages
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)  A tool to create isolated Python environments


#### Development setup
- Create a virtual environment and activate it
    ```bash
     Create: virtualenv venv
     On windows: source /venv/scripts/activate
     On linux: /venv/bin/activate
     
    ```
- Install dependencies 
    ```bash
    pip3 install -r requirements.txt
    ```
- Run the application
    ```bash
    cd iReporter
    python run.py
    ```
- Thereafter you can access the system api Endpoints:

| End Point                                           | Verb |Use                                       |
| ----------------------------------------------------|------|------------------------------------------|
|`/api/v2/records/`                                   |GET   |Gets all records  regardless the type                |
|`/api/v2/auth/record/<int:record_no>`                    |GET   |Gets a specific redflag record  or intervention whose record_no they know already          |
|`/api/v2/records/`                                   |POST  |Creates a new redflag record or intervention record              |
|`/api/v2/record/<int:record_no>/status/`             |PUT   |Updates the status of a redflag record or an intervention record by someone with adminstration rights   |
|`/api/v2/records/<int:record_no>/delete/`            |DELETE|Deletes a specific redflag record or intervention whose record_no is well known by the user        |
|`/api/v2/auth/signup/`                               |POST  | Creates a new user to enable them get access to the application|
|`/api/v2/auth/login/`                                |POST  | Logs in User into the application provided they got an account already |
|`/api/v2/record_no/<int:record_no>/`                 |PUT   | User can change the geolocation of their redflags or Interventions     |
|`/api/v2/redflag/<int:record_no>/`                   |GET   | user who created redflags can access them                              |
|`/api/v2/redflags/`                                  |GET   | user who created redflags can access them as a whole                           |
|`/api/v2/redflag/<int:record_no>/`                   |DELETE| user who created redflags can delete a specific redflag                              |
|`/api/v2/redflag/update/<int:record_no>/`            |PUT| user who created redflags can update their geolocation using their record_no|
|`/api/v2/intervention/<int:record_no>/`              |GET   | user who created interventions can access them by their record_no       |
|`/api/v2/interventions/`                             |GET   | user who created interventions can access them all                        |
|`/api/v2/intervention/<int:record_no>/`              |DELETE| user who created interventions can DELETE a record they desire            |
|`/api/v2/redflag/update/<int:record_no>/`            |PUT| user who created interventions can update their record_geolocation     |
|`/api/v2/auth/users/<int:user_id>/records/`          |GET| one can access a particular user's records    |

#### Testing

- To run the tests, run the following commands

```bash
pytest tests/test.py --cov 
```
#### Screenshot built using
* Serving Flask app "run" (lazy loading)
* Environment: development
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 270-333-235
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


#### Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language
* HTML
* CSS
* [Postgres](https://www.postgresql.org/)- A database used to persist data to be used by the application

## Authors

<strong> MUWONGE NICHOLUS <strong>

## Acknowledgments

* My Family for supporting me and Andela bootcamp fellows and LFA's that made this possible for me.













