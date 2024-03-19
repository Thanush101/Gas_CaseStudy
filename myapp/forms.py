# myapp/forms.py

from django import forms
from .models import ServiceRequest 

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']  # it will take the details of the request