# Employee Manager

A small and simple application to manage employees.


## Environment

- macOS Sierra `10.12.6`
- Python `3.6`
- Docker `18.03.1-ce-mac65 (24312)`


## How to run

If you are using Docker, simply execute:

```
make build && make up
```

If not, execute:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata user.json
python manage.py runserver 0.0.0.0:8000
```

Now you have this application running at http://localhost:8000 and admin http://localhost:8000/admin.

**Credentials to access the admin:**
- User: `admin`
- Password: `teste123`


## Running tests

Just execute:

```
make test
```

> Tests covers serializers and resources API.


## API documentation

Simple API that implements `list`, `created` and `delete`.

**Accepted/Returned:** `json`

### Endpoints

| Endpoint                | Method   | Response     | Fields                        |
| ----------------------- |:--------:| :-----------:| ----------------------------- |
| /employee               | `GET`    | `200`        |                               |
| /employee               | `POST`   | `201`, `400` | `name`, `email`, `department` |
| /employee/{employee_id} | `DELETE` | `204`, `404` |                               |

> All fields is required
