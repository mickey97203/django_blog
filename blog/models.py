from django.db import models
from django.contrib.auth.models import User
from login.models import MyUser
from datetime import datetime
import pytz

VISIBLE = (
   (0, 'All'),
   (1, 'Only Logged Users'),
)

class Category(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100)
  
  def __str__(self):
    return self.title

class Tag(models.Model):
  title = models.CharField(max_length=80)
  slug = models.SlugField(max_length=100)

  def __str__(self):
    return self.title

class Post(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=100)
  category = models.ManyToManyField(Category, blank=True)
  tags = models.ManyToManyField(Tag, blank=True)
  author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
  content = models.TextField()
  image = models.ImageField(upload_to='images', blank=True)
  published_date = models.DateTimeField(auto_now_add=True)
  visible = models.IntegerField(choices=VISIBLE, default=0)

  class Meta:
    ordering = ['-published_date']
    

  def __str__(self):
    return self.title

  @property
  def publish(self):
    utc = pytz.UTC
    return self.published_date <= utc.localize(datetime.now())
    






