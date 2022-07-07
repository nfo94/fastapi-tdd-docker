### Python FastAPI App

![Continuous Integration and Delivery](https://github.com/nfo94/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)

Text summarizer app built with Python, FastAPI, Docker, PostgreSQL, Tortoise
ORM, aerich and Pytest, applying TDD.

#### To run the containers:

```bash
$ docker-compose up -d
```

#### To apply database migrations:

```bash
$ docker-compose exec web aerich upgrade
```

#### Running tests:

```bash
$ docker-compose exec web python -m pytest
```

#### Running test's coverage:

```bash
$ docker-compose exec web python -m pytest --cov="."
```

#### Running linting:

```bash
$ docker-compose exec web flake8 .
```

#### Running formatting:

```bash
$ docker-compose exec web black .
$ docker-compose exec web isort .
```
