# Shop Management System
##### Step1: Download shop_management.zip file  or Clone repo.
```
git clone https://github.com/ajaykumarr123/shop_management 
```
##### Step2: unzip shop_management.zip</br>

##### Admin(Shop Owner) </br>
```
username: ajay
password: ajay
```

* To create new admin(shop owner)</br>
  ```
  python3 manage.py createsuperuser
  ```
  ## Installation

1. Install python virtual environment


```bash
python -m pip install --user virtualenv
```

2. Go to the directory where project is saved and create a new virtual environment new_v using the following command:

```bash
python3 -m venv new_v
```

3. Activate the virtual environment

```bash
source new_v/bin/activate
```
4.Install django and django-crispy-forms

```bash
pip3 install Django==2.2 django-autofixture django-extensions django-phone-field
pip3 install celery==4.4.2 django-crispy-forms image django-rest-framework
```
5. Execute the following command to run the server:
```bash
python manage.py runserver
```
5. Open the following address in your browser
```bash
http://127.0.0.1:8000/
```
Now follow Instructions given at the end of [guide.pdf](https://github.com/ajaykumarr123/shop_management/blob/master/guide.pdf)
