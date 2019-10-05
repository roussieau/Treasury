# Treasury
This web application facilitates the management of banking transactions and dinners in a shared housing.
## The features
- Registration / unsubscription at dinners.
- It is no longer possible to change your choice from 4 pm on the day of the dinner.
- It is possible to declare guests.
- It is possible to declare any transaction, involving one or more people.
- It is possible to use a common bank account that is used as a kitty.
- Or simply in tricount mode.

## Installation
You need to run the project in a virtual environment. Personally I use **pipenv** 
```pip3 install pipenv```.  
Now you can clone the project install the dependencies  
```git clone https://github.com/roussieau/Treasury.git  
cd Treasury
pipenv --three  
pipenv install  
pipenv shell  
```
Initialize the database and launch the project.  
```  
python manage.py migrate  
python manage.py runserver
```
