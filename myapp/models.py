from django.db import models
from django.contrib.auth.models import User

# class ServiceRequest(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)  #  customers are users
#     request_type = models.CharField(max_length=100)
#     details = models.TextField()
#     attachment = models.FileField(upload_to='attachments/')
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     resolved_at = models.DateTimeField(null=True, blank=True)
    
    
#     def __str__(self):
#         return f"{self.request_type} - Submitted by {self.customer.username}"
    

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # customers are users
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    request_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - Submitted by {self.customer.username}"