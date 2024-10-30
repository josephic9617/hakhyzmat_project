# Hakhyzmat project

This project written on python 3.12.1. Used Postgres for db.

## Step by step running

1. Install requirements:

    Run `pip install -r requirements.txt` in your terminal.

2. Create database and update settings:

    Create a new Postgres database and add credentials to `settings.py` file.

3. Make migrations:

    Run `python manage.py makemigrations` and `python manage.py migrate` to create db schema.

4. Run the server:

    Run `python manage.py runserver` to start the development server.

5. Open in browser:

    Open `http://localhost:8000` in your browser and use username: admin and password: 123 to log in.

