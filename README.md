[![Build Status](https://travis-ci.com/NicholusMuwonge/iReporter.svg?branch=ft-challenge-two)](https://travis-ci.com/NicholusMuwonge/iReporter)
[![Coverage Status](https://coveralls.io/repos/github/NicholusMuwonge/iReporter/badge.svg?branch=ft-challenge-two&service)](https://coveralls.io/github/NicholusMuwonge/iReporter?branch=ft-challenge-two)

[![Maintainability](https://api.codeclimate.com/v1/badges/95c6a67ee8716ddebf6b/maintainability)](https://codeclimate.com/github/NicholusMuwonge/iReporter/maintainability)




### About
<strong>IREPORTER<strong> is an application thats supposed to be used by some one to raise an issue to the authorities about corruption,and any other grievance to the authority.

### Features
1. Create a redflag record (title, record_type,record geolocation)
2. Edit a specific redflag record's geolocation.
3. Get a specific redflag record
4. Delete a redflag record
5. Get all redflag records for that specific user


### Links

#### Gh-pages:  
https://nicholusmuwonge.github.io/iReporter/UI/index

This link points to the user interface template is hosted on gh-pages.

#### Heroku:    
https://appireporter.herokuapp.com/

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
|`/api/v1/records`                                    |GET   |Gets all redflag records                  |
|`/api/v1/records/<int:record_no>`                    |GET   |Gets a specific redflag record            |
|`/api/v1/records`                                    |POST  |Creates a new redflag record              |
|`/api/v1/<int:record_no>/records`                    |PUT   |Updates the status of a redflag record    |
|`/api/v1/<int:record_no>/records`                    |DELETE|Deletes a specific redflag record         |

#### Testing

- To run the tests, run the following commands

```bash
pytest --cov 
```

#### Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language
* HTML
* CSS

## Authors

<strong> MUWONGE NICHOLUS <strong>

## Acknowledgments

* My Family for supporting me and Andela bootcamp fellows and LFA's that made this possible for me.













