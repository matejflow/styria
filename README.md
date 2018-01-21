These are instruction for installing Styria Test assignment in development environment.

## Preparing Python environment

Read `INSTALL.md` for more info on how to setup development environment

If you want to change development variables: `basic_django/settings/development.conf`


## CUSTOM COMMANDS

1) movie_scrapper
~~~
python manage.py movie_scrapper
~~~

2) user_seeder - creates test_user, test_staff, test_admin with p: test.123
~~~
python manage.py seed_users
~~~


## OTHER NICE COMMANDS
From `setup.cfg`

1) sort imports and fix common errors in python files
~~~
./autoclean-bash
~~~

2) custom flake8
~~~
flake8
~~~


## ABOUT THE PROJECT

- Used Django 2.0 and PostgreSQL for setup
- For linting pylint, pycodestyle, and mypy for type hinting (`mypy.ini`)
- Added user protected pages, admin panel not fully implemented (missing data and views)
- Test not done, would have used pytest and vcr.py for request testing
- Layout done with SASS
- custom pagination implementation
- required widget is done with cache filled on scrapper command, added to context to remove need for querying data all the time, since this would be probably done as daily cron job (scraping)
- visible widget implementation done part of Django tags, available anywhere

- with additional time would also scrape for celebs and their roles in movies,
- search functionality, sort functionalities, celeb views, user pages, user watchlist
- admin panel with more data
