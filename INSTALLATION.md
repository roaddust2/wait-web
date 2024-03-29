# Installing and running the app

This is a short guide, how to install and run the the app in development environment.  
As a tool for dependency managment we strongly recommend you using Poetry (otherwise some make commands will not work).
To install latest Poetry on your system you can easily run the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Official documentation of Poetry can be found [here](https://python-poetry.org/docs/).

## Installation
### Variables

  ```.env
  # Django settings vars
  
  DJANGO_SECRET_KEY=
  DJANGO_DEBUG=True
  DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
  
  
  # Postgres vars
  
  POSTGRES_DB=
  POSTGRES_USER=
  POSTGRES_PASSWORD=
  POSTGRES_HOST=
  POSTGRES_PORT=
  ```

### Steps

  ```bash
  # Clone the repository and install dependencies
  git clone https://github.com/roaddust2/wait-web.git
  cd wait-web
  make install

  # To activate virtual environment in terminal simply use
  poetry shell

  # Create basic postgres database

  # Create .env file and add environment variables
  touch .env

  # For generating DJANGO_SECRET_KEY use
  make secretkey # and then copy paste it in .env file.

  # Apply migrations
  make migrate

  # Create superuser
  poetry run python3 manage.py createsuperuser

  # Start application
  make dev

  # App will be availible at 127.0.0.1:8000 on your browser
  ```
