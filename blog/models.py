from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        help_text="A short label, generally used in URLs.", default='', max_length=100)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    content = RichTextUploadingField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
