# ecommerce-backend
Ecommerce-Django-backend

## Setup Development Environment

    sudo apt-get -y update
    sudo apt-get -y install git python-pip
    sudo pip install virtualenv
    
   
 ## Clone the code
 
## Create Virtual Environment and Activate
 //python -m virtualenv virtualenv_name
  
 source virtualenv_name/scripts/activate
 
## Install Application Requirements

  pip install -r ./requirements.txt
  
## Run Application
cd backend/manage.py runserver

## To create tables
python manage.py makemigrations
python manage.py migrate
