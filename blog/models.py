from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django import forms


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(help_text="A short label, generally used in URLs.",default='', max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date_posted']
    
    def save(self):
        slug = self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
    
   




