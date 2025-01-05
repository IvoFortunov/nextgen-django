from django.db import models
import uuid

class About(models.Model):
    description = models.TextField(null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank= True)
    social_instagram = models.CharField(max_length=200, null=True, blank= True)
    mobile = models.CharField(max_length=200, null=True, blank= True)
    email = models.EmailField(max_length=500, null=True, blank= True)
    address = models.CharField(max_length=200, null=True, blank= True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return 'about'
    
