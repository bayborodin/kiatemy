# Kiatemy CRM

[![Build Status](https://travis-ci.org/bayborodin/kiatemy.svg?branch=master)](https://travis-ci.org/bayborodin/kiatemy)

Open source CRM built with Django and React.

**Disclaimer**: the project is sooo pre-alpha.

## Motivation and main idea

Our ambitious goal is to create the CRM of dreams that will combine all the advanced ideas in the field of customer relationship management along with the basic principles of open source software.


## Contributing

We would love you to contribute to our project. It's simple:

1. Create an issue with bug you found or proposal you have.
2. Create a pull request. Make shure all checks are green.
3. Fix review comments if any.
4. Be awesome.

### Useful commands for dev purpose
* Make migrations:
```sh
docker-compose run backend sh -c "python manage.py makemigrations"
```
* Run tests:
```sh
docker-compose run backend sh -c "python manage.py test && flake8"
```
