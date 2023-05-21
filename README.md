# CinemaBookingSystem, steps to run the project

# make sure python is installed on computer, and python 'Path'is set in user environment variables
# open the cmd, change the directory to the project directory where the manage.py is in, example below
cd C:\Users\User\Desktop\csit314\CinemaBookingSystem

# optional --> create a virtual environment, 'myenv' is the name of the environment
py -m venv myenv

# optional --> run the virtual environment
myenv\scripts\activate

# Install the following dependencies by running the pip command provided
# Install Django
pip install django

# Install Crispy_form
pip install django-crispy-forms

# Install Bootstrap 5
pip install django-bootstrap-v5

# Install Crispy Boostrap 5
pip install crispy-bootstrap5

# Install xhtml2pdf
pip install xhtml2pdf

# Install pillow 
pip install Pillow

# Once done run the web application
python manage.py runserver
