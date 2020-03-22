COVID-19 CommCare API
---

### Setup Steps (~15 minutes)

1. Download and install [docker](https://docs.docker.com/install/) for your OS.
2. Download and install [docker-compose](https://docs.docker.com/compose/install/) for your OS.
3. Install [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html) for Python 3.6+.

### Development

Start the database in the background using `docker-compose`.

```bash
$ docker-compose up -d postgres
```

Setup and enter the Python virtual environment.

```bash
$ pipenv shell --three
$ pipenv install --dev --skip-lock
```

Run the [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) development server in the Python virtual environment.

```bash
$ ./dev-server.sh
```

You can view the OpenAPI exported docs at `localhost:8000/docs`.

To stop everything, terminate the dev-server and run:

```bash
$ docker-compose down
```

