# Django 2.0 - Rest-API with Heroku Integration
A REST api written in Django for people with deadlines

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have Python and Heroku globally installed in your computer. If not, you can get python [here](https://www.python.org) and Heroku [here](https://devcenter.heroku.com/articles/heroku-cli).
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/gitgik/django-rest-api.git
    ```

* #### Steps
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd django-heroku-rest-api
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
            $ python manage.py createsuperuser
        ```
    5. Run It
    ```bash
        $ python manage.py runserver
    ```
    6. Test it Locally
   
        http://localhost:8000/users/
  
    7. Time to go remote!
    
    ```bash 
    $ heroku login 
    $ heroku create project 
    $ git push heroku master 
    $ heroku run python manage.py migrate 
    $ heroku run python manage.py createsuperuser 
    ```
    
    Your project should now be live at: 
    
    https://heroku_project_name.herokuapp.com/users/
    
    If you want to set your own project to support Heroku here is a detailed explanation:
    
    https://gist.github.com/agusalex/70146cb09381c0adc4b3a2f68d035cfa
