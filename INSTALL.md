These are instruction for installing Styria Test assignment in development environment.

## Preparing Python environment

0) Install system dependencies

~~~
$ sudo apt-get install build-essential git python3 python3-venv python3-dev\
postgresql-server-dev-all libpq-dev postgresql postgresql-contrib
~~~

1) Clone the repository:

~~~
git clone https://{{YOUR_USERNAME}}@github.com/astralwolf/styria.git
~~~

1a) Installing Python 3.5 on older machines
~~~
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5
~~~

2) prepare Python virtual environment

~~~
pyvenv .venv
source .venv/bin/activate
pip install -U pip pip-tools wheel
deactivate
source .venv/bin/activate
pip install -r requirements_dev.txt
#pip-sync requirements_dev.txt
~~~

2a) If error on pyvenv command, run following:
~~~
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
~~~

2b) If error with pip-sync command:
~~~
pip install --upgrade setuptools
#pip install --upgrade distribute
#sudo apt-get install --reinstall python-pkg-resources
#wget https://bootstrap.pypa.io/ez_setup.py -O - | python
~~~

## Prepare PostgreSQL

1) Use PostgreSQL tools to create user, role and database

~~~
$ sudo -u postgres psql
postgres=# ALTER USER postgres PASSWORD 'postgres';
postgres=# CREATE DATABASE styria WITH ENCODING='UTF8' OWNER=postgres CONNECTION LIMIT=-1;
~~~

2) Make Migrations and Build DB

~~~
source .venv/bin/activate
python manage.py migrate
python manage.py createcachetable
python manage.py seed_users
~~~
