from django.db import models
import uuid
from users.models import Profile

class Program(models.Model):
    name = models.CharField(max_length =200)
    image = models.ImageField(null=True, blank=True, upload_to='programs', default="programs/default.jpg")
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
# Create your models here.
        
class ProgramImage(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="programs", null=True, blank=True)
    
    def __str__(self):
        return self.program.name
