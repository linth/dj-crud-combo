# dj-crud-combo
django application uses the function-based view, the class-based view, and rest-framework for CRUD functionalility.

## 1. clone project
```
$ git clone https://github.com/linth/dj-crud-combo.git
```

## 2. enter virtual environment
```
$ source dj_crud/env/Scripts/activate 
```

## 3. install packages
```
$ pip install -r dj_crud/requirement.txt
```

## 4. migrate your database.
```
$ python manage.py migrate
```

## 5. create a superuser by django cli
```
$ python manage.py createsuperuser
```
enter account/password what you want.


## 6. execute your django web service
```
$ python manage.py runserver
```
