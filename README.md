COVID-19 CommCare API
---

### Setup Steps (~15 minutes)

1. Install [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html) for Python 3.6+.

### Development

Setup and enter the Python virtual environment.

```bash
$ pipenv shell --three
$ pipenv install --dev --skip-lock
```

Export the CommCare credentials to the environment.

```bash
$ export COMMCARE_USERNAME=...
$ export COMMCARE_PASSWORD=...
```

Run the [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) development server in the Python virtual environment.

```bash
$ ./dev-server.sh
```

You can view the OpenAPI exported docs at `localhost:8000/docs`.
