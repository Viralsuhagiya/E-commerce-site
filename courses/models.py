from django.db import models

# Create your models here.
class Post(models.Model):
    course=models.CharField(max_length=15)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.course