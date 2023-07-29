#Test progect for itworkin

## To run this project need to:

- create working directory `mkdir name_of_folder` command on linux terminal
- navigate to that directory
- clone repository: `git clone https://github.com/jjuchara/it_workin_test_case.git`
- install [**Poetry**](https://python-poetry.org/docs/) for install dependencys
- type `poetry install` for installation
- create postgresql server with database name: **_python_db_** or change db name in /app/core/db 6 line to whatever you want
- run alembic commands to generate migrations:
  ```shell
    alembic revision --autogenerate -m "Auto migrations"
    alembic upgrade head
  ```
  - start server from cloned repo root `python main.py`
  - open browser with **_localhost:8000/docs_** to play with API
