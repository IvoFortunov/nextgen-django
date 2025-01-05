from django.db import models
import uuid
from users.models import Profile

class News(models.Model):
    author = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)  
    image = models.ImageField(null=True, blank=True, upload_to='news', default="news/default.jpg")
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created']
