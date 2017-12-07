I'm using this repo as a way to learn django, python and virtual environments.

# Development

First of all, initialize and activate the virtual environment:

```
virtualenv -p python3 .env
source .env/bin/activate
```

Then make sure you have the dependencies installed:

```
pip install -r requirements.txt
```

To run the development server:

```
cd PyCoin
python manage.py runserver
```

This project uses a postgres database though, so make sure you have that setup first:

```
createdb pycoin
cd PyCoin
python manage.py migrate
```
