from django.db import models
from django.utils import timezone

class TeamMembers(models.Model):
    MEMBER_TYPE = [
        ('MG', 'Manager'),
        ('DR', 'Director'),
        ('IN', 'Investor'),
        ('EM', 'Employee'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField
    profile_image = models.ImageField(upload_to='newApp/')
    date_added = models.DateTimeField(default=timezone.now)
    member_type = models.CharField(max_length=2, choices=MEMBER_TYPE)
    
    def __str__(self):
        return self.name