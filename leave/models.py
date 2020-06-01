from django.db import models
from django.contrib.auth.models import User

status_choices =(
    ('pending','pending'),
    ('approved','approved'),
    ('rejected','rejected'),
    ('cancelled','cancelled'),
)

class leave_request(models.Model):
    emp = models.ForeignKey(User,null=True, on_delete=models.CASCADE,related_name="ap1")

    date_time = models.CharField(max_length = 100)
    status = models.CharField(max_length = 20 ,default='pending',choices=status_choices)
    adm_cmts = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.date_time
