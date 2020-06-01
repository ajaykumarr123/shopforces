from django import forms
from .models import leave_request

class leave_form(forms.ModelForm):

    class Meta:
        model = leave_request
        fields = ['date_time']
