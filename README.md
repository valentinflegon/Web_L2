# Django


![alt tag](https://user-images.githubusercontent.com/43956710/102696271-60cde580-422d-11eb-9f67-3d9dbb0e8516.jpg)
![alt tag](https://user-images.githubusercontent.com/43956710/102696323-cae68a80-422d-11eb-9f0e-124f48cd05a7.jpg)

## pour lancer le projet il faut utiliser Virtualenv:

Installation: $ sudo apt-get install python3-pip python-virtualenv

Test: $ virtualenv --version
15.1.0

Python version: $ python3 --version
Python 3.6.0

On va créer l'environnement virtuel que l'on appelera venv-py35
$ virtualenv -p python3 venv-py35

$ ls -l venv-py35/

Activer le venv: 
$ source venv-py35/bin/activate
 
(venv-py35) $ 
 
C'est bon l'environnement est activé ! 

La commande pour installer des packages s'appelle pip.
(venv-py35) $ pip list

On regarde s'il existe une version plus récente de pip :
(venv-py35) $ pip install --upgrade pip


On installe d'autres modules avec pip dans le venv :
(venv-py35) $ pip install Django

On teste que le package fonctionne

(venv-py35) $ django-admin --version
  3.1.4
(venv-py35) $ python -c "import django; print(django.get_version())"
  3.1.4
  
Si on veut désinstaller des packages :
  (venv-py35) $ pip uninstall Django
  
Pour quitter le venv 
(venv-py35)$ deactivate

### Résumé : quick install de Django dans un venv et sauvegarde : 
   $ virtualenv -p python3 venv-py35 && source venv-py35/bin/activate &&
    pip install Django && deactivate && tar cfz venv-py35.tgz venv-py35/ &&
    echo "succés."


# Django: 
Documentation :
    https://www.djangoproject.com/
    https://docs.djangoproject.com/fr/2.1/intro/tutorial01/
Il faut être dans le venv pour utiliser Django 
  $ source venv-py35/bin/activate
  
Créer un projet:
 (venv-py35) $ django-admin startproject my_site
 
Tester le serveur: 
  (venv-py35) my_site$ ./manage.py runserver
   
   Ouvrir la page http://127.0.0.1:8000/

Si vous avez un "ModuleNotFoundError: No module named 'debug_toolbar'" 
faire -> pip install django-debug-toolbar 

Le serveur nous a affiché ce message :
  Run 'python manage.py migrate' to apply them.

Appliquons les "migrations" :
  (venv-py35) my_site$ ./manage.py migrate
 
  (venv-py35) my_site$ ls -l

  $ ./manage.py runserver
  Performing system checks...
  
C'est bonnnnnn ton site tourne !!!!!! 
Mais en local uniquement ..... 
On va voir comment le mettre en ligne avec Heroku

