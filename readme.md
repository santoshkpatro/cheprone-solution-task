# Steps to run the project in your system

Follow the steps

## Step 1
Clone the project to your local system

## Step 2
Open terminal in that folder

## Step 3
```bash
pip install -r requirements.txt
```

## Step 4
Making database ready
```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 5
Making a superuser
```bash
python manage.py createsuperuser
```
Complete the createsuperuser detail form

## Step 6
Starting server
```bash
python manage.py runserver
```

## All Done!!
visit [localhost:8000](localhost:8000)