# Shop Management System
  A Web App developed in Django to manage the entire shop efficiently by providing functionalities such as-
Inventory Management, buy/sell items, Shopping History , Approve/reject leave request,update profile etc
##### Step1: Clone repo.
```
git clone https://github.com/ajaykumarr123/shop_management 
```

  ## Installation

1. Install python virtual environment


```bash
sudo apt-get install python3-venv  
```

2. Create a new virtual environment and activate it.
```bash
mkdir djangoenv
python3 -m venv djangoenv
source envv/bin/activate
```
3.Install django and django-crispy-forms
```bash
pip3 install Django==2.2 django-autofixture django-extensions django-phone-field
pip3 install celery==4.4.2 django-crispy-forms image django-rest-framework
  ```
4.To create new admin(shop owner)</br>
 ```bash
 python3 manage.py createsuperuser
  ``````
5. Execute the following command to run the server:
```bash
python3 manage.py runserver
```
6. Open the following address in your browser
```bash
http://127.0.0.1:8000/
```

Now follow Instructions given inside [Guide.pdf](https://github.com/ajaykumarr123/shop_management/blob/master/Guide.pdf)
