from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True) #get current actual time

    def __str__(self) -> str:
        return f"{self.title}"
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.strftime("%d/%m/%Y %H:%M ")
        }