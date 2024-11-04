# Cryptocurrency-REST-API-Django

```python 
python3 -m pip3 install -r requirements.txt
```

run the following commands:
```
python3 manage.py makemigrations trackingAPI
python3 manage.py migrate
python3 manage.py runserver
```

and start Celery worker:
```
celery -A cryptocurrencytracking worker -l info
```