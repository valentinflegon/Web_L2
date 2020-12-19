# Web_L2
Django

## pour lancer le projet il faut utiliser Virtualenv:

Installation: $ sudo apt-get install python3-pip python-virtualenv

Test: $ virtualenv --version
%15.1.0

Python version: $ python3 --version
%Python 3.6.0

On va créer l'environnement virtuel que l'on appelera venv-py35
$ virtualenv -p python3 venv-py35
%   Running virtualenv with interpreter /usr/bin/python3.5
    Using base prefix '/usr'
    New python executable in /home/thiel/Bureau/venv-py35/bin/python3.5
    Also creating executable in /home/thiel/Bureau/venv-py35/bin/python
    Installing setuptools, pkg_resources, pip, wheel...done.

$ ls -l venv-py35/
% total 0
  drwxrwxrwx 1 val val 4096 Dec 19 18:06 bin
  drwxrwxrwx 1 val val 4096 Dec 19 18:06 include
  drwxrwxrwx 1 val val 4096 Dec 19 18:06 lib
  drwxrwxrwx 1 val val 4096 Dec 19 18:06 share
  
Activer le venv: 
$ source venv-py35/bin/activate
 
(venv-py35) $ 
 
C'est bon l'environnement est activé ! 

La commande pour installer des packages s'appelle pip.
(venv-py35) $ pip list
% Package       Version
------------- -------
pip           20.3.3
pkg-resources 0.0.0
setuptools    51.0.0
wheel         0.36.2

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
    %...
    Django version 2.1.7, using settings 'my_site.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
   Ouvrir la page http://127.0.0.1:8000/

Si vous avez un "ModuleNotFoundError: No module named 'debug_toolbar'" 
faire -> pip install django-debug-toolbar 


Le serveur nous a affiché ce message :

  You have 15 unapplied migration(s). Your project may not work properly until
  you apply the migrations for app(s): admin, auth, contenttypes, sessions.
  Run 'python manage.py migrate' to apply them.

Appliquons les "migrations" :

  (venv-py35) my_site$ ./manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
  Running migrations:
    Applying ... OK

  (venv-py35) my_site$ ls -l

  $ ./manage.py runserver
  Performing system checks...
  
C'est bonnn ton site tourne 

https://user-images.githubusercontent.com/43956710/102696271-60cde580-422d-11eb-9f67-3d9dbb0e8516.jpg

![alt tag](https://user-images.githubusercontent.com/43956710/102696271-60cde580-422d-11eb-9f67-3d9dbb0e8516.jpg)
