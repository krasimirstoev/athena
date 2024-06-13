from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
import hashlib

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    body = CKEditor5Field(config_name='extends')
    post_time = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            num = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    web = models.URLField(blank=True, null=True)
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

    def gravatar_url(self):
        email_hash = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{email_hash}'

class Page(models.Model):
    title = models.CharField(max_length=200)
    body = CKEditor5Field(config_name='extends')
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=200)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'

class SiteSettings(models.Model):
    blog_name = models.CharField(max_length=200, default="My Blog")
    blog_subtitle = models.CharField(max_length=300, blank=True, null=True)
    posts_per_page = models.PositiveIntegerField(default=5)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError('There is can be only one SiteSettings instance')
        return super(SiteSettings, self).save(*args, **kwargs)

    def __str__(self):
        return self.blog_name
