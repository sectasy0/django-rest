# Django REST API - Interview Task

## Installation

#### docker-compose

```sh
docker-compose up
```

#### without docker-compose

```sh
python -m venv venv
source venv/bin/activate
pip install REQUIREMENTS.TXT

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

```

#### Create superuser
```sh
python manage.py createsuperuser
```

## Usage example

#### Get authentication token

```sh
http POST https://restapp-intv.herokuapp.com/api/v1/auth/token/login username=admin password=test123
```

```
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 57
Content-Type: application/json

{
    "auth_token": "4ab10fa5d044c8ea5b748140ef25b36afe6ad12f"
}

```

#### Upload an image

```sh
http --form PUT https://restapp-intv.herokuapp.com/api/v1/image/upload/ "Authorization: token <your token here>" format="jpg" file@path/to/file.png
```

```sh
HTTP/1.1 200 OK
Allow: PUT, OPTIONS
Content-Length: 57
Content-Type: application/json

{
    "datail": "created"
}

```

#### Get your images

```sh
http GET https://restapp-intv.herokuapp.com/api/v1/images/ "Authorization: token <your token here"
```

```sh
HTTP/1.1 200 OK
Allow: PUT, OPTIONS
Content-Length: 57
Content-Type: application/json

[
    {
        "image": "/uploads/admin_27FCCB5CBD6D.png",
        "pk": 1
    }
]

```


#### Get one image

```sh
http GET https://restapp-intv.herokuapp.com/api/v1/image/<image_id> "Authorization: token <your token here"
```

```sh
HTTP/1.1 200 OK
Allow: PUT, OPTIONS
Content-Length: 57
Content-Type: application/json

{
    "image": "/uploads/admin_27FCCB5CBD6D.png",
    "pk": 1
}

```

#### Create expiration link

```sh
http PUT https://restapp-intv.herokuapp.com/api/v1/image/shared/ "Authorization: token <your token here>" expires=500 protected_data=test1234
```

```sh
HTTP/1.1 200 OK
Allow: PUT, OPTIONS
Content-Length: 57
Content-Type: application/json

{
    "data": {
        "private_data": <json private data>
    },
    "expires": "2021-05-13T21:00:43.969093",
    "url": "/api/v1/shared/37f20a05f05f"
}
```

#### Get your links

```sh
http GET https://restapp-intv.herokuapp.com/api/v1/image/shared/ "Authorization: token <your token here>" expires=500 protected_data=test1234
```

```sh
[
    {
        "data": "protected_data",
        "expires": "2021-05-13T20:19:27.740107Z",
        "url": "/api/v1/shared/2f22e15ba98e"
    },
    {
        "data": "{'private_data': 'test123'}",
        "expires": "2021-05-13T19:00:43.969093Z",
        "url": "/api/v1/shared/37f20a05f05f"
    }
]
```

#### Get link

```sh
http GET https://restapp-intv.herokuapp.com/api/v1/image/shared/2f22e15ba98e "Authorization: token <your token here>"
```

```sh
{
    "data": "{'private_data': 'test123'}",
    "expires": "2021-05-13T19:00:43.969093Z",
    "url": "/api/v1/shared/37f20a05f05f"
}
```
