# Installing and running the app

This is a short guide, how to install and run the the app in development environment.  
As a tool for dependency managment we strongly recommend you using Poetry (otherwise some make commands will not work).
To install latest Poetry on your system you can easily run the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Official documentation of Poetry can be found [here](https://python-poetry.org/docs/).

## 1. Installation

### 1.1 Cloning the repository and installing dependencies
First of all clone the repo:

```bash
git clone https://github.com/roaddust2/wait-web.git
cd wait-web
make install
```

To activate virtual environment in terminal simply use:

```bash
poetry shell
```

### 1.2 Set the values of the environment variables in the .env file
Create .env file in project directory:

```bash
touch .env
```

Then add the following variables:

```.env
# Django settings vars

DJANGO_SECRET_KEY=
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0


# Postgres vars
# For DATABASE_TYPE use postgres
# In development environment leave empty, sqlite3 will be used

DATABASE_TYPE=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

For generating DJANGO_SECRET_KEY use:

```bash
make secretkey
```

and then copy paste it in .env file.

## 3. Running a server

Insert the command:

```bash
make dev
```

App will be availible at 127.0.0.1:8000 on your browser
