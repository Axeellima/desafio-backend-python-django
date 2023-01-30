CNAB Database

    CNAB Database aims to facilitate the registration, reading and location of data from CNAB files.

    Functionalities: CNAB file record per customer/store, customer/store listing with transaction history

    Technologies: Python, Django restframework, SQlite, drf spectacular

    Instalation:

        1° Step create your virtual environment in your terminal in the root folder of the project
        using "python -m venv venv" for more information access "https://docs.python.org/3/library/venv.html"

        2° Step install project dependencies using "pip install -r requirements.txt" in your terminal

        3° Step run "python manage.py makemigrations" and "python manage.py migrate" in your terminal for create a new database and crete the tables

        4° The application is ready to use, but attention is needed if you start the server on a port other than ":8000" make sure to change the request link in "_project.views"

        5° In terminal "python manage.py runserver"

    Application:

        commom-server-link = "http://localhost:8000/"

        Register CNAB: To upload and register your CNAB file, add the suffix "api/ to the server link to access the submission form. After submission you will get a success response from the server if everything goes well!

        List of stores and transactions: To list all stores and your transactions add the suffix "api/list/" to the server link.
