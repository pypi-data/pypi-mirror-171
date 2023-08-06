Django Contact Us Email Sending application
============================================

Send feedback or contact with us

Additional Information
-----------------------

1. For sending the email use the host 'mailtrap.io'. So, First singup form the official mailtrap.io website


2. Then copy the configutation selecting the Django Framework like below </br>

EMAIL_HOST = 'smtp.mailtrap.io' </br>
EMAIL_HOST_USER = 'XXXXXXXXXXX' </br>
EMAIL_HOST_PASSWORD = 'XXXXXXXXXXX' </br>
EMAIL_PORT = '2525' </br>

Quick start
------------

1. Add "app1" to your INSTALLED_APPS setting like this::

        INSTALLED_APPS = [
            ...
            'app1',
        ]

2. Include the app1 URLconf in your project urls.py like this::

        path('', include('app1.urls')),


3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/
   to create a poll (you'll need the Admin app enabled).

