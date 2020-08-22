# Hello!

My REST API for "Connect" project.
_______________________________________________________

# Main idea:

*Connect* is a project to help media-people share their traffic, and sell/buy/exchange promotion.
Also have *Connect* implementation on Django3 MVC architecture. 
This project created mostly to improve my skills in Django REST and knowledge in REST services. 


# Instalation:

Pull repo, than:
        
        $ pip3 install -r requirements.txt

Than set 'local_settings.py', with DB, SMTP, SECRET_KEY and PATHS settings. 

Or stay on test_settings.py

# Last update:

Added logging to the project and implemeted logging of SQL queries into console:

        $ LOGGING = {
              ...
              'disable_existing_loggers': False
              ...
          }
in settings.py. Set 'True' to turn off.

JWT tokens supported.
