# Welcome to OFF substitutes !  

## Introduction:  

This program will alow you to select a food product and it will automaticly find
better substitutes products.  
Currently the app language is only in French  

__How does it work ?__

OFF substitues download products using the API REST of Openfactfoods and record
them in a local Mysql database.  
You can select products, get substitutes and even save them in local database.  

## Requirements: 

To run OFF substitutes you need to install: 
  
Python 3.8 : https://www.python.org/downloads/  
Mysql https://www.mysql.com/fr/downloads/  
  
__YOU NEED TO HAVE A LOCAL DATABASE NAMED "db_p5" ON YOUR LOCAL MYSQL SERVER.__  
__You can run the sql script "db_p5.sql" to create the schema of it.__  
  
create virtual envirement using command (Windows Powershell):  
``py -m venv venv``  
Activate the virtual environment:  
``py -m venv\Scripts\Activate.ps1 ``  
Install the necessary modules:  
``pip install -r requirements.txt ``  
(to deactivate venv use :)  
``deactivate``  

For other commands (OS or terminal) please check:  
https://docs.python.org/fr/3/library/venv.html  
  
Change the settings of Mysql server parameters with your own ones in config 
file:  

```python 
#Mysql server configuration:
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "db_p5"  # (DO NOT CHANGE THIS PARAMETER)
```


## Run the App:

Run the file main.py  
NOTE: IF IT IS FIRST TIME YOU USE THE APP:  
At the Main menu, run option number 3 (reset database) to create the database
on your local machine.  
  

    Bienvenue dans OFF substitutes

    (NOTE: pour une première utilisation: sélectionner 3 pour créer la base de données)

    1 Quel aliment souhaitez-vous remplacer ?

    2 Retrouver mes aliments substitués

    3 Réinitialiser la base de données (SELECT THIS CHOICE FOR 1ST USE)

    4 Quitter le programme  

Enjoy !
