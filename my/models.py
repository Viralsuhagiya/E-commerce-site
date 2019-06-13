from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.
class News(models.Model):
    author= models.CharField(max_length=15)
    title=models.CharField(max_length=15)
    description=models.TextField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return  self.author

class Hobby(models.Model):
    hobby = models.CharField(max_length=15)

    def __str__(self):
        return self.hobby

class Gender(models.Model):
    gender = models.CharField(max_length=15)
    def __str__(self):
        return self.gender

class Registration(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    hobby = models.ManyToManyField(Hobby)
    # gender = models.OneToOneField(Gender,on_delete=models.CASCADE,primary_key=True)
    gender =  models.ForeignKey(Gender,on_delete=models.CASCADE)
    country = CountryField()
    image = models.ImageField(upload_to='my/images/',default="")
    def __str__(self):
        return  self.username



