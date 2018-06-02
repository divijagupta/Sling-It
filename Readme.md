
![Logo](images/logo.png)

Sling It, a URL shortener that helps you generate short and crisp links which not only makes the link look much cleaner and allows customization, but also helps to keep a track of clicks and also monitor traffic behaviour


### Installation

- Create a virtual environment

    `virtualenv venv`


- Start virtual environment

    `source venv/bin/activate`


- Install requirements

    `pip install -r requirements.txt`


- Set your domain name in settings.py
   
    `MY_URL='www.localhost:8000/`


- Enable Debug for debugging

    Go to the `settings.py` file and set the variable `DEBUG` to True.


- Migrate DB

    `python manage.py makemigrations` and `python manage.py migrate` 


- Running test server, go to the folder with `manage.py` file and run:

    `python manage.py runserver`

    This will run the server at localhost:8000.


